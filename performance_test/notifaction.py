# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  notifaction.py
@CreateTime     :  2020/4/17 14:43
------------------------------------
"""
import uuid

from locust import HttpLocust, TaskSet, task, between


class UserBehaviour(TaskSet):

    @task(1)
    def get_userscope_props(self):
        uc = uuid.uuid1()
        url = f'/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications?url_scheme=growing.638b52710867187c&u={uc}&cs={uc}'
        with self.client.get(url=url, catch_response=True) as r:
            if r.status_code == 200:
                r.success()
            r.connection.close()


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(0.2, 0.4)