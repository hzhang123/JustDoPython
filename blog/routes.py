# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  routes.py
@CreateTime     :  2020/3/20 11:27
------------------------------------
"""
from flask import render_template

from blog import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'hzhang'}
    posts = [
        {
            'author': {'username': '刘'},
            'body': '这是模板模块中的循环例子～1'

        },
        {
            'author': {'username': '忠强'},
            'body': '这是模板模块中的循环例子～2'
        }
    ]
    return render_template('index.html', title='hzhang', user=user, posts=posts)
