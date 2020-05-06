# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  __init__.py.py
@CreateTime     :  2020/3/20 11:25
------------------------------------
"""
import os

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
# 导入配置文件
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

root_dir = os.path.abspath(os.path.dirname(__file__)).split('JustDoPython')[0] + 'JustDoPython/'

# app初始化
app = Flask(__name__)
# 配置配置文件
app.config.from_object(Config)

# 数据库初始化，建立数据库关系
db = SQLAlchemy(app)
# 绑定app和数据库
migrate = Migrate(app, db)

scheduler = BackgroundScheduler()
scheduler_fude = BackgroundScheduler()
scheduler.start()
scheduler_fude.start()

# 登录模块初始化
login = LoginManager(app)
# 增加登录限制
login.login_view = 'login'

# 初始化bootstrap
bootstrap = Bootstrap(app)

from blog import routes, models