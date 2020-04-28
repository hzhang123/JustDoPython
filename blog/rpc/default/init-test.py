# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  userscope_props.py.py
@CreateTime     :  2020/4/8 17:25
------------------------------------
"""

from locust import HttpLocust, TaskSet, task, between


class UserBehaviour(TaskSet):

    @task(1)
    def get_userscope_props(self):
        url = '/stat/userScope/props?ignoreCache=true'
        json = {
            "ai": "test_push_1",
            "userScope": "cs1:99999999",
            "attrs": "vstr_gio_push_package,vstr_gio_push_channel,vstr_gio_push_token,vstr_gio_push_device_brand,vstr_gio_notification_enabled",
            "startIndex": SetIndex.index,
            "endIndex": SetIndex.index + SetIndex.step
        }

        with self.client.post(url=url, json=json, catch_response=True) as r:
            if r.status_code == 200:
                r.success()
            r.connection.close()

        # 主动关闭方会保留TIME_WAIT两个MSL，Linux一个MSL为30s
        # self.client.close() 断开整个会话
        # r.connection.close() 断开客户端连接
        # headers={‘Connection‘:‘close‘} 告诉客户端是关闭还是保持连接
        SetIndex.set_index()


class SetIndex:
    index = 0
    step = 1000
    _end = 280000

    @classmethod
    def set_index(cls):
        if cls.index > cls._end:
            cls.index = 0
        else:
            cls.index += cls.step


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(0.2, 0.4)
