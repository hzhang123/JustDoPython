# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  scheduler_task.py
@CreateTime     :  2020/4/26 16:55
------------------------------------
"""
import html
import importlib
import json
import os

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.base import STATE_STOPPED
from dingtalkchatbot.chatbot import DingtalkChatbot
from flask import render_template, Blueprint, flash, jsonify, request, redirect, url_for

from blog import db, scheduler
from blog.tmp import jobs_templates
from blog.forms import SchedulerTaskForm
from blog.models import SchedulerHttpTask

scheduler_task = Blueprint('scheduler_task', __name__)


@scheduler_task.route('/index')
def index():
    return render_template('scheduled_job/index.html')


@scheduler_task.route('/task/add', methods=['GET', 'POST'])
def add():
    form = SchedulerTaskForm()
    if form.validate_on_submit():
        st = SchedulerHttpTask(
            name=form.name.data,
            team=form.team.data,
            service=form.service.data,
            url=form.url.data,
            method=form.method.data,
            body=form.body.data,
            assertion=form.assertion.data,
            expected=form.expected.data
        )
        st.status = 'activated'
        db.session.add(st)
        db.session.commit()
        flash('添加成功')
        return redirect(url_for('scheduler_task.index'))
    return render_template('scheduled_job/add_task.html', form=form)


@scheduler_task.route('/task/remove', methods=['GET', 'POST'])
def remove():
    job_ids = json.loads(request.get_data(as_text=True))
    for job_id in job_ids:
        db.session.query(SchedulerHttpTask).filter(
            SchedulerHttpTask.id == job_id
        ).update(
            {
                SchedulerHttpTask.status: 'deleted'
            }
        )
    db.session.commit()
    return jsonify({'code': 200})


@scheduler_task.route('/tasks')
def tasks():
    info = request.values
    limit = info.get('limit', 10)  # 每页显示的条数
    offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点

    jobs = db.session.query(SchedulerHttpTask).filter(
        SchedulerHttpTask.status.in_(['activated', 'draft'])
    ).order_by(
        SchedulerHttpTask.id.asc()
    ).all()

    data = []
    for job in jobs:
        data.append(job.to_json())

    return jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})


@scheduler_task.route('/refresh')
def refresh_jobs():
    # 删除所有的jobs
    scheduler.remove_all_jobs()
    # 更新jobs文件
    jobs = db.session.query(SchedulerHttpTask).filter(SchedulerHttpTask.status == 'activated').all()
    rows = []
    for job in jobs:
        rows.append(job.to_json())
    jobs_content = render_template("scheduled_job/jobs.html", rows=rows)
    root_dir = os.path.abspath(os.path.dirname(__file__)).split('JustDoPython')[0]
    tmp_dir = f'{root_dir}/JustDoPython/blog/tmp/'
    file = f'jobs_templates.py'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    with open(f'{tmp_dir}{file}', 'w') as f:
        f.writelines(html.unescape(jobs_content))
    # 重新导入
    importlib.reload(jobs_templates)
    # 查询当前激活的jobs
    for job in jobs:
        func_name = f'job_{job.id}'
        scheduler.add_job(getattr(jobs_templates, func_name), 'interval', seconds=50)

    # 定时任务的监控
    scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    if scheduler.state == STATE_STOPPED and len(jobs) > 0:
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
    return str(scheduler.state)


def job_listener(event):
    if event.exception:
        job = scheduler.get_job(event.job_id)
        job = db.session.query(SchedulerHttpTask).filter(SchedulerHttpTask.id == int(job.name.split('_')[1])).one()
        print(str(job.name))
        send_to_dingding(f'API: {str(job.name)}')
    else:
        # 执行成功
        pass


def send_to_dingding(msg):
    webhook = '机器人链接'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_text(msg=msg)
