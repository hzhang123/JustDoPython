# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  cases.py
@CreateTime     :  2020/4/30 19:53
------------------------------------
"""
import json
import os
import shutil
import time

from dingtalkchatbot.chatbot import DingtalkChatbot
from flask import Blueprint, render_template, jsonify, request
from flask_restful import Api, Resource, reqparse, fields, marshal, marshal_with
from httprunner.api import HttpRunner

from blog import db, root_dir, scheduler_fude, scheduler
from blog.models import TestCases
from my_har_parser import MyHarParser

cases_blueprint = Blueprint('cases', __name__)
cases_api = Api(cases_blueprint)

parser = reqparse.RequestParser()
parser.add_argument(
    'name', type=str, required=True, help='用例名称不能为空')
parser.add_argument(
    'service', type=str, required=True, help='所属服务不能为空')
parser.add_argument(
    'team', type=str, required=True, help='开发团队不能为空')
parser.add_argument(
    'case_json', type=dict, required=True, help='用例内容不能为空')

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'team': fields.String,
    'service': fields.String,
    'status': fields.String,
    'case_json': fields.Raw
}


@cases_blueprint.route('/index')
def index():
    return render_template('cases/index.html')


@cases_blueprint.route('/har/upload', methods=['POST'])
def har_upload():
    file = request.files['kartik-input-700']
    file_content = file.read().decode('utf-8')
    # file.save(root_dir + 'blog/tests/' + file.filename)
    test_case = MyHarParser(json.loads(file_content)).gen_testcase("JSON")
    return jsonify(test_case)


@cases_blueprint.route('/test', methods=['POST'])
def case_test():
    # runner = HttpRunner
    case_content = request.json['case']
    case_debug_file = f'{root_dir}blog/tests/debug/{int(time.time())}_debug.json'
    with open(case_debug_file, 'w') as f:
        json.dump(case_content, f)
    runner = HttpRunner(failfast=True, save_tests=False)
    summary = runner.run(case_debug_file)
    print(summary)
    return jsonify({"code": 200})


class ITestCase(Resource):

    @marshal_with(resource_fields)
    def get(self, case_id):
        test_cases = db.session.query(TestCases).filter(
            TestCases.id == case_id
        ).order_by(
            TestCases.id.asc()
        ).all()

        return test_cases[0].to_json()

    def delete(self, case_id):
        delete_case = db.session.query(TestCases).filter(
            TestCases.id == case_id
        ).update(
            {
                TestCases.status: 'deleted'
            }
        )
        db.session.commit()
        return jsonify({'code': 200})

    def put(self, case_id):
        args = parser.parse_args()
        update_case = db.session.query(TestCases).filter(
            TestCases.id == case_id
        ).update(
            {
                TestCases.name: args['name'],
                TestCases.team: args['team'],
                TestCases.service: args['service'],
                TestCases.case_json: args['case_json']
            }
        )
        db.session.commit()
        return jsonify({'code': 200})


class ITestCases(Resource):

    # @marshal_with(resource_fields)
    def get(self):
        # info = request.values
        # limit = info.get('limit', 10)  # 每页显示的条数
        # offset = info.get('offset', 0)  # 分片数，(页码-1)*limit，它表示一段数据的起点
        test_cases = db.session.query(TestCases).filter(
            TestCases.status.in_(['activated', 'draft'])
        ).order_by(
            TestCases.id.asc()
        ).all()

        cases_to_json = [case.to_json() for case in test_cases]
        # 格式化
        cases_marshal = marshal(cases_to_json, resource_fields)
        # all_case = jsonify({'total': len(data), 'rows': data[int(offset):(int(offset) + int(limit))]})
        return jsonify({'total': len(cases_marshal), 'rows': cases_marshal})

    def post(self):
        args = parser.parse_args()
        st = TestCases(
            name=args['name'],
            team=args['team'],
            service=args['service'],
            case_json=args['case_json']
        )
        st.trigger = {'type': 'interval', 'unit': 'minutes', 'size': '2'}
        st.status = 'activated'
        db.session.add(st)
        db.session.commit()
        return jsonify({'code': 200, 'msg': '用例添加成功'})


cases_api.add_resource(ITestCase, '/case/<int:case_id>')
cases_api.add_resource(ITestCases, '/cases')


@cases_blueprint.route('/example')
def example():
    data = {
        "returncode": 200,
        "returndata": {
            "datanodes": [{
                "code": "zb.A010101_sj.2019",
                "data": {
                    "data": 0,
                    "dotcount": 0,
                    "hasdata": False,
                    "strdata": ""
                },
                "wds": [{
                    "valuecode": "A010101",
                    "wdcode": "zb"
                }, {
                    "valuecode": "2019",
                    "wdcode": "sj"
                }]
            }, {
                "code": "zb.A010101_sj.2018",
                "data": {
                    "data": 333,
                    "dotcount": 0,
                    "hasdata": True,
                    "strdata": "333"
                },
                "wds": [{
                    "valuecode": "A010101",
                    "wdcode": "zb"
                }, {
                    "valuecode": "2018",
                    "wdcode": "sj"
                }]
            }]
        }
    }
    return jsonify(data)


# 引入定时任务管理
def _manage_test_case_file():
    test_cases = db.session.query(TestCases).filter(TestCases.status == 'activated').all()
    test_case_root_dir = root_dir + 'blog/tests/testcase/'
    shutil.rmtree(test_case_root_dir)
    os.mkdir(test_case_root_dir)
    for test_case in test_cases:
        test_case_file = test_case_root_dir + str(test_case.id) + '_case.json'
        with open(test_case_file, 'w') as f:
            json.dump(test_case.to_json()['case_json'], f)

    scheduler.remove_all_jobs()
    scheduler.add_job(_manage_test_case, 'interval', seconds=60)


def _manage_test_case():
    test_case_root_dir = root_dir + 'blog/tests/testcase/'
    runner = HttpRunner(failfast=True, save_tests=True)
    summary = runner.run(test_case_root_dir)
    # 用例集失败
    if summary['success'] is False:
        for detail in summary['details']:
            # 用例失败
            if detail['success'] is False:
                for record in detail['records']:
                    test_case_name = record['name']
                    test_case_status = record['status']
                    test_case_attachment = record['attachment']
                    test_case_meta_datas = record['meta_datas']
                    print('result' + str(test_case_name) + str(test_case_status) + str(test_case_attachment) + str(
                        test_case_meta_datas))
                    text = f'''
                    ## 用例状态

                    {test_case_status}

                    ## 用例详情

                    ```
                    {json.dumps(test_case_meta_datas, indent=2)}
                    ```
                    '''
                    send_to_dingding_marketdown(title=f'API{test_case_name}', text=text)


def send_to_dingding_marketdown(title, text):
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=bbcb656e68a3999a81e492c79eac4bd629dd90478640d34034788124ca7537dc'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title=title, text=text)


# 第一次启动刷新一遍用例
_manage_test_case_file()
scheduler_fude.add_job(_manage_test_case_file, 'interval', hours=1)
