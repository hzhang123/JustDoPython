# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  toolbox.py
@CreateTime     :  2020/7/13 14:16
------------------------------------
"""
from flask import Blueprint, render_template, request
from flask_restful import Api

from config import cfg

boolbox_blueprint = Blueprint('toolbox', __name__)
boolbox_api = Api(boolbox_blueprint)


@boolbox_blueprint.route('/index')
def index():
    h5_demo = {
        "vdsEnv": cfg.web_h5_demo.vdsEnv,
        "vdsVersion": cfg.web_h5_demo.vdsVersion,
        "h5Env": cfg.web_h5_demo.h5Env,
        "h5Version": cfg.web_h5_demo.h5Version,
        "accountId": cfg.web_h5_demo.accountId
    }

    return render_template('toolbox/index.html', h5_demo=h5_demo)


@boolbox_blueprint.route('/h5_test')
def h5_test():
    """
    通过页面传入变量切换指定版本的测试Demo
    accountId：项目ID string not null
    无埋点：
        vdsEnv:string not null
        vdsVersion: int not null
    弹窗：
        h5Env:string not null
        h5Version:int not null
    :return:
    """
    #
    # 1. product: saas cdp
    # 2. type: web h5
    # 2. h5Env: release k8s-qa product
    # 3. h5Version: 1.1 ...
    args = request.args.to_dict()

    # 无埋点vdsJs, 目前先不修改

    # web&h5 h5Js链接拼接
    h5_js = f"{cfg.web_h5_demo.static_host}/sdk/marketing/test/{args['h5Env']}/{args['h5Version']}/"
    if args['product'] == 'saas':
        # saas 区分两个文件
        if args['type'] == 'web':
            h5_js += "access.js"
        elif args['type'] == 'h5':
            h5_js += "h5.js"
    if args['product'] == 'cdp':
        # cdp web与h5使用一个依赖
        h5_js += "gtouch.js"

    env = {
        "accountId": args['accountId'],
        "vdsJs": "assets.giocdn.com/2.1/gio.js",
        "h5Js": h5_js,
    }
    return render_template('toolbox/h5_test.html', title='H5测试Demo', env=env, args=args)
