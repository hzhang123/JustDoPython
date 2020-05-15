# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  class_test.py
@CreateTime     :  2020/4/27 13:18
------------------------------------
"""

from httprunner.api import HttpRunner

from cases import CaseStatus


def job_1():
    pass


if __name__ == '__main__':
    # runner = HttpRunner(failfast=True, save_tests=True)
    # case_debug_dir = root_dir + 'blog/tests/debug/'

    # summary = runner.run("/Users/growingio/PycharmProjects/JustDoPython/blog/tests/debug/")
    # print(summary)
    print(CaseStatus.CREATED)
