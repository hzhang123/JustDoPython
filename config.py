# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  config.py
@CreateTime     :  2020/3/20 18:10
------------------------------------
"""

class Config(object):
    SECRET_KEY = 'hzhang123'
    SQLALCHEMY_DATABASE_URI = 'postgresql://hzhang:123456@192.168.2.101:5432/stars'
    SQLALCHEMY_TRACK_MODIFICATIONS = False