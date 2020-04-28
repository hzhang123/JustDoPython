# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  fabric_per.py
@CreateTime     :  2020/4/12 19:09
------------------------------------
"""

from fabric.api import run


class BaseScript(object):

    @classmethod
    def check_local_dir(cls):
        pass

    @classmethod
    def check_remot_dir(cls):
        pass

    @classmethod
    def git(cls, url: str):
        pass

class PerformanceScript(object):

    @classmethod
    def look(cls):
        run('ls -l')
