# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  config.py
@CreateTime     :  2020/3/20 18:10
------------------------------------
"""
import os

from pyhocon import ConfigFactory

root_dir = os.path.abspath(os.path.dirname(__file__))
cfg = ConfigFactory.parse_file(f'{root_dir}/application.conf')


class Config(object):
    SECRET_KEY = cfg.SECRET_KEY
    SQLALCHEMY_DATABASE_URI = cfg.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = cfg.SQLALCHEMY_TRACK_MODIFICATIONS