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


if __name__ == '__main__':
    runner = HttpRunner(failfast=True, save_tests=False)

    summary = runner.run("/Users/growingio/PycharmProjects/JustDoPython/blog/tests/testcase/")
    print(summary)
