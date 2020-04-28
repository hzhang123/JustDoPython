# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  day_some.py
@CreateTime     :  2020/4/9 19:21
------------------------------------
"""

from fabric.api import env, run
from fabric.tasks import execute


# #执行shell时候如果会有错误，比如说找不到文件之类，需要加上
# with settings(warn_only=True):
#
# #需要保持进程（比如说启动tomcat之类），需要加上pty=False
# run('sh -x start-up.sh', pty=False)
from days_100.fabric_per import PerformanceScript


def get_dir():
    env.hosts = ['root@192.168.2.101']
    # env.port = '22'
    # env.user = 'root'
    # env.passwords = {
    #     'root@192.168.2.101:22': '123456'
    # }

    execute(PerformanceScript.look)

if __name__ == '__main__':
    get_dir()
