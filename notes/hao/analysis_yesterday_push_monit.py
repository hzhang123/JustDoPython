# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  analysis_yesterday_push_monit.py
@CreateTime     :  2020/6/22 13:56
------------------------------------
"""
import os
import time

import psycopg2
import requests
import pandas as pd
from dingtalkchatbot.chatbot import DingtalkChatbot
from pyhocon import ConfigFactory


if __name__ == '__main__':
    # 初始化配置文件
    conf = ConfigFactory.parse_file(f'{os.path.abspath(os.path.dirname(__file__))}/../conf/push-monit.conf')

    host = conf.zeppelin.host
    # 登录获取cookie
    data = {"userName": conf.zeppelin.username, "password": conf.zeppelin.password}
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url=f'{host}/api/login', params=header, data=data)
    cookies = r.cookies

    # 获取zeppelin任务输出内容
    r = requests.get(url=f'{host}{conf.zeppelin.push_notebook_path}', cookies=cookies,)
    # 判断任务是否执行成功
    results = r.json()['body']['results']
    if results['code'] != 'SUCCESS':
        exit()
    # 提取内容到列表
    data = results['msg'][0]['data']
    lines_data = data.split("start print result:")[-1].split("end print result:")[0]
    lines = [ele.split(',') for ele in lines_data.split("\n") if len(ele) > 0]
    hbase_data = pd.DataFrame(lines, columns=['rule_id', 'dim', 'time', 'dvalue', 'cnt'])

    # 获取所有的弹窗规则并数据库查询相关数据
    rules = hbase_data['rule_id'].drop_duplicates()
    #
    growing_conn = psycopg2.connect(
        host=conf.db_basic.host,
        port=conf.db_basic.port,
        database=conf.db_names.growing,
        user=conf.db_basic.user,
        password=conf.db_basic.password)

    events_conn = psycopg2.connect(
        host=conf.db_basic.host,
        port=conf.db_basic.port,
        database=conf.db_names.events,
        user=conf.db_basic.user,
        password=conf.db_basic.password)

    push_messages = pd.read_sql_query(
        f'''
        select
            t3.name as project_name,
            t1.ai as project_ai,
            t1.name as push_name,
            t1.state,
            t4.user_num
        from
            push_messages t1
            join push_rules t2 on t1.id = t2.message_id
            join projects t3 on t1.ai = t3.keyid
            join user_segmentations t4 on split_part(t1.audience_id, ':', 2) :: int = t4.id
        where
            t2.start_at between TIMESTAMP 'today' - interval '1 days 8 hours' 
            and TIMESTAMP 'today' - interval '8 hours' 
            and t1.type = 'push'
        group by project_name, project_ai, push_name, t1.state, t4.user_num;
        ''',
        growing_conn
    )

    customs_event = pd.read_sql_query(
        f'''
        select
            'g' || id as rule_id,
            project_id,
            case
                when key = 'gio_push_message_sent' then '消息发送'
                when key = 'gio_push_message_arrived' then '消息送达'
                when key = 'gio_push_message_clicked' then '消息点击'
            end as event_name,
            'var_' || key as event_key,
            ai as project_ai
        from
            custom_events
        where
            'g' || id :: text in {str(tuple(rules))}
            and status = 'activated';
        ''',
        events_conn
    )
    growing_conn.close()
    events_conn.close()

    # 数据关联操作
    all_data = pd.merge(
        pd.merge(push_messages, hbase_data, left_on='push_name', right_on='dvalue'),
        customs_event,
        on=['rule_id', 'project_ai']
    )

    # messages = '项目名称\t推送名称\t今日分群人数\t消息发送设备数\t消息送达设备数\t点击数\t送达率\t点击率'
    messages = []
    for push_name in all_data['push_name'].drop_duplicates():
        push_message = all_data.query(
            f'''
            push_name == '{push_name}'
            '''
        )
        # 组织名称
        # 推送名称
        # 今日分群人数
        # 发送人数
        push_message_sent_cnt = round(float(push_message.query(
            f'''
            event_key == 'var_gio_push_message_sent'
            '''
        )['cnt'].sum()), 4)
        # 送达人数
        push_message_arrived_cnt = round(float(push_message.query(
            f'''
            event_key == 'var_gio_push_message_arrived'
            '''
        )['cnt'].sum()), 4)
        # 点击人数
        push_message_clicked_cnt = round(float(push_message.query(
            f'''
            event_key == 'var_gio_push_message_clicked'
            '''
        )['cnt'].sum()), 4)

        if push_message_sent_cnt == 0:
            sent_per = '0%'
        else:
            sent_per = '{:.2f}%'.format(push_message_arrived_cnt / push_message_sent_cnt * 100)
        if push_message_arrived_cnt == 0:
            arrived_per = '0%'
        else:
            arrived_per = '{:.2f}%'.format(push_message_clicked_cnt / push_message_arrived_cnt * 100)

        message = []
        message.append(push_message['project_name'].values[0])
        message.append(push_name)
        message.append(push_message['user_num'].values[0])
        message.append(push_message_sent_cnt)
        message.append(push_message_arrived_cnt)
        message.append(push_message_clicked_cnt)
        message.append(sent_per)
        message.append(arrived_per)
        messages.append(message)

    context = f'''
    {conf.dingding.prefix}
    报告日期:{time.strftime('%Y-%m-%d')}
    昨日数据:
    '''
    for message in messages:
        context += f'''
        {message[0]}\t{message[1]}\t今日分群人数:{message[2]}
        消息发送设备数:{message[3]}\t消息送达设备数:{message[4]}\t点击数:{message[5]}\t送达率:{message[6]}\t点击率:{message[7]}
        '''
    xiaoding = DingtalkChatbot(conf.dingding.webhook)
    xiaoding.send_text(context)
