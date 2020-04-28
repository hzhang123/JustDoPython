# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  class_test.py
@CreateTime     :  2020/4/27 13:18
------------------------------------
"""
from apscheduler.schedulers.blocking import BlockingScheduler

from tmp import jobs_templates

if __name__ == '__main__':

    scheduler = BlockingScheduler()

    func = getattr(jobs_templates, 'job_4')
    func()
    scheduler.add_job(f'jobs_templates.job_4', 'interval', seconds=5)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass

