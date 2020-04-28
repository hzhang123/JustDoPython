# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  locusts.py
@CreateTime     :  2020/4/16 13:50
------------------------------------
"""
import json

import os
import os.path
import platform
import time

import psutil
from flask import Blueprint, request, render_template, jsonify

from .rpc.master import cmd_queue, result_queue, lock, logger

locust_script = './blog/rpc/default/init-test.py'  # Locust master script file
script_filename = '../default/init-test.py'  # default script file name of client if don't select file from web
locust_status = 'stop'
p = None

locust_hive = Blueprint('locust_hive', __name__)


@locust_hive.route('/index')
def index():
    return render_template('locust_hive/index.html')


@locust_hive.route('/test/slave', methods=['POST', 'GET'])
def locust_slave():
    if request.method == 'GET':
        info = request.values
        limit = info.get('limit', 10)  # 每页显示的条数
        offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        data = [
            {
                'id': 1,
                'hostname': 'MacBookdeMacBook-Pro-3',
                'ip': '10.10.2.1',
                'username': 'root',
                'desc': '主信任机器'
            },
            {
                'id': 2,
                'hostname': 'MacBookdeMacBook-Pro-4',
                'ip': '10.10.2.2',
                'username': 'apps',
                'desc': ''
            }
        ]
        return jsonify({'total': 2, 'rows': data[int(offset):(int(offset) + int(limit))]})


@locust_hive.route('/master', methods=['GET', 'POST'])
def master():
    with lock:
        global locust_status, p, locust_script, script_filename
        context = {
            'filelist': [],
            'hello': 'Clients list OK!',
            'script': '',
            'text': '',
            'clients': refresh_clients()
        }
        if request.method == 'POST':
            json_data = json.loads(request.get_data(as_text=True))
            if json_data['command'] in ['start_locust', 'stop_locust']:
                if locust_status == 'running':
                    # 停止Locust Master
                    if p is not None:
                        logger.info("Server: try to stop the locust master!")
                        if p.poll() is None:
                            try:
                                # 先停止子进程再停止自身进程，Popen在容器中启动会有两个进程，一个是shell进程，另一个是应用进程
                                procs = p.children(recursive=True)
                                for proc in procs:
                                    if platform.system() == "Windows":
                                        proc.send_signal(0)
                                    else:
                                        proc.terminate()
                                    proc.wait()
                                if platform.system() == "Windows":
                                    p.send_signal(0)
                                else:
                                    p.terminate()
                                p.wait()
                                p = None
                                logger.info("Server: locust master stopped!")
                            except:
                                pass
                    if p is None:
                        context['hello'] = 'Locust master has been stopped!'
                        logger.info("Server: locust master is stopped!")
                        locust_status = 'stop'
                        # 通知各客户端停止压测
                        for client in context['clients']['clients']:
                            stop(client['id'])
                        context['clients'] = refresh_clients()
                else:
                    # 启动Locust的Master模式
                    p = psutil.Popen(f'locust -f {locust_script} --master --no-reset-stats', shell=True,
                                     stdout=None,
                                     stderr=None)
                    time.sleep(1)
                    if p.poll() is not None:
                        # 判断Locust进程是否启动失败并给出提示
                        if p.poll() != 0:
                            logger.info("Server: failed to start locus master...")
                            context[
                                'hello'] = f'Failed to start locust master! Please check script file: {locust_script}'
                            p = None
                    else:
                        # 成功启动Locust的Master模式进程
                        logger.info(f'Locust Master process PID:{p.pid}')
                        logger.info("Server: locust master is running...")
                        context['hello'] = 'Locust master has been running!'
                        locust_status = 'running'

            return locust_status


@locust_hive.route('/slave', methods=['GET', 'POST'])
def slave():
    """
    slave
        state
            ready
            running
            bolck
        command
            ready
            start
            stop

    :return:
    """
    with lock:
        global locust_status, p, locust_script, script_filename
        context = {
            'filelist': [],
            'hello': 'Clients list OK!',
            'script': '',
            'text': '',
            'clients': refresh_clients()
        }
        if request.method == 'POST' and context['clients']['num'] > 0:
            members = json.loads(request.get_data(as_text=True))
            #  and context['clients']['num'] <= 0
            health_client_ids = [client['id'] for client in context['clients']['clients']]
            clients = [member for member in members if member['id'] in health_client_ids]
            for client in clients:
                if client['type'] == 'run':
                    if client['command'] == 'ready':
                        file_name = client['fileName']
                        num = client['num']
                        context['hello'] = run(client['id'], num, file_name)
                        context['clients'] = refresh_clients()
                        for c in context['clients']['clients']:
                            if c['id'] == client['id']:
                                if c['slave_num'] == 0:
                                    context['hello'] = f'''Client {client["id"]} run error, 
                                    please check you script file {file_name} is valid!'''
                                else:
                                    context['hello'] = f'Client {client["id"]} run OK, script file is {file_name}!'
                    else:
                        # 停止客户端压测进程
                        context['hello'] = stop(client['id'])
                        context['clients'] = refresh_clients()
                    break
                # 获取客户端的脚本文件列表
                elif client['type'] == 'filelist':
                    file_list = get_filelist(client['id'])
                    if file_list['id'] == client['id']:
                        context['filelist'].append(file_list)
                    break
                # 清除客户端脚本文件夹
                elif client['type'] == 'clear':
                    context['hello'] = clear_folder(client['id'])
                    break
                # 发送压测脚本到客户端
                elif client['type'] == 'send':
                    if len(client['files']) > 0:
                        # 将所选脚本文件内容发给客户端，文件控件可以多选
                        for script_file in client['files']:
                            if os.path.exists(script_file) and script_file.endswith('.py'):
                                with open(script_file, 'r') as f:
                                    script = f.read()
                                context['hello'] = send_script(client['id'], os.path.basename(script_file), script)
                            else:
                                context['hello'] = "File name should be end with .py!"
                    else:
                        # 将页面上编辑后的脚本内容发送给客户端，前提为未选择文件
                        context['hello'] = send_script(client['id'], request.POST.get('filename', None),
                                                       request.POST.get('text%s' % client['id'], None))
                    break
                # 编辑压测脚本(如果多选，则只编辑列表中最后一个文件)
                elif client['type'] == 'edit':
                    if request.FILES.get(client['id'], None):
                        script_file = request.FILES.get(client['id'], None)
                        context['script'] = script_file.read()
                        context['text'] = client['id']
                        context['filename'] = script_file.name
                    break
                # 获取客户端系统资源利用率
                # if json_data['mon_clients']:
                #     # 系统监控信息
                #     psinfo = []
                #     for c in context['clients']['clients']:
                #         psinfo.append(get_psinfo(c['id']))
                #     context['psinfos'] = psinfo
                #     context['mon_flag'] = "Checked"
                #     context['hello'] = "Clients's monitor data refresh OK！"
                # else:
                #     pass

        context['locust'] = locust_status
        host = request.host
        context['host'] = host.split(':')[0]
        return context['clients']


# 等待结果消息队列返回数据
def wait_result():
    retry = 0
    result = None
    while result_queue.empty():
        time.sleep(1)
        retry = retry + 1
        if retry > 10:
            logger.info('Web server: retry max times, no clients response;')
            break
        logger.info('Web server: command response is none, get in next 1s...')
    while not result_queue.empty():
        result = result_queue.get()
    return result


# 刷新客户端列表
def refresh_clients():
    logger.info('Web server: send new command - [get_clients]')
    cmd_queue.put({'type': 'get_clients'})
    clients = []
    q = wait_result()
    if q:
        if q != '0':
            logger.info('Web server: command - [get_clients] - Got response!')
            print(q)
            clients = q
    return {'num': len(clients), 'clients': clients}


# 发送压测脚本到客户端
def send_script(client_id, filename, script):
    logger.info('Web server: send new command - [send_script(%s)]' % client_id)
    cmd_queue.put({'type': 'sent_script', 'client_id': client_id, 'filename': filename, 'script': script})
    q = wait_result()
    if q:
        if q == 'OK':
            logger.info('Web server: command - [send_script(%s)] - Got response!' % client_id)
            return 'Script send to %s successful!' % client_id
    return 'Script send to %s failed!' % client_id


# 启动客户端压测进程
def run(client_id, num, filename):
    logger.info('Web server: send new command - [run locust slave(%s)]' % client_id)
    cmd_queue.put({'type': 'run', 'client_id': client_id, 'filename': filename, 'num': num})
    q = wait_result()
    if q:
        if q == 'OK':
            logger.info('Web server: command - [run locust slave(%s)] - Got response!' % client_id)
            return 'Client %s run successful!' % client_id
    return 'Client %s run failed!' % client_id


# 停止客户端压测进程
def stop(client_id):
    logger.info('Web server: send new command - [stop locust slave(%s)]' % client_id)
    cmd_queue.put({'type': 'stop', 'client_id': client_id})
    q = wait_result()
    if q:
        if q == 'None':
            logger.info('Web server: command - [stop locust slave(%s)] - Got response!' % client_id)
            return 'Client %s stop successful!' % client_id
    return 'Client %s stop failed!' % client_id


# 获取客户端压测脚本文件列表
def get_filelist(client_id):
    logger.info('Web server: send new command - [get file list(%s)]' % client_id)
    cmd_queue.put({'type': 'get_filelist', 'client_id': client_id})
    q = wait_result()
    if q:
        if q['client_id'] == client_id:
            if q['file_list']:
                logger.info('Web server: command - [get file list(%s)] - Got response!' % client_id)
                return {'id': client_id, 'file_list': q['file_list']}
    return {'id': client_id, 'file_list': ''}


# 获取客户端系统资源状态
def get_psinfo(client_id):
    logger.info('Web server: send new command - [get ps info(%s)]' % client_id)
    cmd_queue.put({'type': 'get_psinfo', 'client_id': client_id})
    q = wait_result()
    if q:
        if q['client_id'] == client_id:
            logger.info('Web server: command - [get ps info(%s)] - Got response!' % client_id)
            return {'id': client_id, 'psinfo': q['psinfo']}
    return {'id': client_id, 'psinfo': ''}


# 清除客户端压测脚本文件夹
def clear_folder(client_id):
    logger.info('Web server: send new command - [clear folder(%s)]' % client_id)
    cmd_queue.put({'type': 'clear_folder', 'client_id': client_id})
    q = wait_result()
    if q:
        if q['client_id'] == client_id:
            if q['clear_folder'] == 'OK':
                logger.info('Web server: command - [clear folder(%s)] - Got response!' % client_id)
                return 'Client %s script folder cleared!' % client_id
    return 'Failed to clear client %s script folder!' % client_id


# 参考停止子进程代码，暂时不用
def reap_children(timeout=3):
    global p
    "Tries hard to terminate and ultimately kill all the children of this process."

    def on_terminate(proc):
        print(("process {} terminated with exit code {}".format(proc, proc.returncode)))

    procs = p.children()
    # send SIGTERM
    for proc in procs:
        proc.terminate()
    gone, alive = psutil.wait_procs(procs, timeout=timeout, callback=on_terminate)
    if alive:
        # send SIGKILL
        for proc in alive:
            print(("process {} survived SIGTERM; trying SIGKILL" % p))
            proc.kill()
        gone, alive = psutil.wait_procs(alive, timeout=timeout, callback=on_terminate)
        if alive:
            # give up
            for proc in alive:
                print(("process {} survived SIGKILL; giving up" % proc))
