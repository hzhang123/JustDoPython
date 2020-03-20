# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  __init__.py.py
@CreateTime     :  2020/3/20 11:25
------------------------------------
"""
from flask import Flask

# 导入配置文件
from config import Config

app = Flask(__name__)

# 配置配置文件
app.config.from_object(Config)

from blog import routes