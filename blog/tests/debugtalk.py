# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  debugtalk.py
@CreateTime     :  2020/4/29 15:28
------------------------------------
"""


def to_str_contains(check_value, expect_value):
    """
    check_value对象 -> str
    eg: "test" 包含在 "['test1', 'haha']"
    """
    assert expect_value in str(check_value)


def to_str_contained_by(check_value, expect_value):
    """
    check_value对象 -> str
    eg: "['test1', 'haha']" 包含在 "['test1', 'haha', 3]"
    """
    assert str(check_value) in expect_value
