# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  notifaction.py
@CreateTime     :  2020/4/17 14:43
------------------------------------
"""
import os
import queue

import pandas
from locust import between
from locust import task
from locust.contrib.fasthttp import FastHttpUser


class WebsiteUser(FastHttpUser):

    host = 'https://messages-release.growingio.com'

    queueData = queue.Queue()
    dir = os.path.split(os.path.realpath(__file__))[0]
    df = pandas.read_csv(f'{dir}/data/visit_id.csv')
    for u in df.u.values:
        queueData.put(
            {"u": u}
        )

    wait_time = between(0.2, 0.4)

    @task(1)
    def get_notifactions(self):
        try:
            file_line = self.queueData.get()
            self.queueData.put_nowait(file_line)

            data = dict({
                "url_scheme": "growing.638b52710867187c",
            }, **file_line)
            url = f'/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications'
            r = self.client.get(path=url, data=data)
            print(r.json())
            assert r.status_code == 200
        except queue.Empty:
            print('no data exist')
            exit(0)
