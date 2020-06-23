# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  cases.py
@CreateTime     :  2020/4/30 19:53
------------------------------------
"""
import datetime
import json
import os
import time
from enum import unique, Enum

from dingtalkchatbot.chatbot import DingtalkChatbot
from flask import Blueprint, render_template, jsonify, request
from flask_restful import Api, Resource, reqparse, fields, marshal, marshal_with
from httprunner.api import HttpRunner
from sqlalchemy import func

from blog import db, scheduler_fude
from blog.models import TestCases, TestCasesFailedHistory
from blog.my_har_parser import MyHarParser
from config import root_dir, cfg

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
                TestCases.status: CaseStatus.DELETED.value
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
                TestCases.case_json: args['case_json'],
                TestCases.status: CaseStatus.CREATED.value,
                TestCases.updated_at: datetime.datetime.now()
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
            TestCases.status.in_([CaseStatus.CREATED.value,
                                  CaseStatus.RUNNING.value,
                                  CaseStatus.SUSPENDED.value,
                                  CaseStatus.FAILED.value])
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
        st.status = CaseStatus.CREATED.value
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


@unique
class CaseStatus(Enum):
    """
    定时任务与用例状态
    """
    # 新创建状态
    CREATED = 'created'
    # 运行状态
    RUNNING = 'running'
    # 失败状态
    FAILED = 'failed'
    # 暂停状态
    SUSPENDED = 'suspended'
    # 删除状态
    DELETED = 'deleted'
    # 空值
    NULL = None


class CaseStatusManage:
    """
    管理测试用例状态
    """

    def to_running(self, case_id):
        self.update_status(case_id, CaseStatus.RUNNING.value)

    def to_failed(self, case_id):
        self.update_status(case_id, CaseStatus.FAILED.value)

    def to_suspended(self, case_id):
        self.update_status(case_id, CaseStatus.SUSPENDED.value)

    def to_deleted(self, case_id):
        self.update_status(case_id, CaseStatus.DELETED.value)

    def update_status(self, case_id, case_status):
        update_case = db.session.query(TestCases).filter(
            TestCases.id == case_id
        ).update(
            {
                TestCases.status: case_status
            }
        )
        db.session.commit()


class BackGroundJob(object):

    @classmethod
    def testcase_1m_job(cls):
        # 执行测试用例
        cls._manage_test_case()

    @classmethod
    def testcase_5m_job(cls):

        # 刷新用例文件
        cls._refresh_test_case_file()
        # 失败用例发送钉钉
        cls._send_report_to_dingding()

    @classmethod
    def testcase_10m_job(cls):
        # 刷新用例状态
        cls._refresh_test_case_status()

    @classmethod
    def _interval(cls, seconds):
        """
        指定间隔之前
        :param seconds:
        :return:
        """
        return datetime.datetime.now() - datetime.timedelta(seconds=seconds)

    @classmethod
    def _send_report_to_dingding(cls):
        """
        失败用例report发送钉钉
        :return:
        """
        xiaoding = DingtalkChatbot(cfg.dingding.report)
        failed_test_cases = db.session.query(
            TestCases.id, TestCases.name
        ).filter(
            TestCases.status == CaseStatus.FAILED.value
        ).all()
        if len(failed_test_cases) > 0:
            msg = 'MyAPI失败用例列表：'
            for test_case in failed_test_cases:
                msg += f'\t用例id: {test_case[0]}, 用例名称: {test_case[1]}\n'
            xiaoding.send_text(msg=msg)

    @classmethod
    def _refresh_test_case_status(cls):
        """
        失败率超过30%，标记为失败
        :return:
        """
        cnt = func.count(1).label('cnt')
        failed_test_case_list = db.session.query(
            TestCasesFailedHistory.test_case_id,
            cnt
        ).filter(
            TestCasesFailedHistory.created_at > cls._interval(600)
        ).group_by(
            TestCasesFailedHistory.test_case_id
        ).having(
            cnt > 3
        ).all()

        for failed_test_case in failed_test_case_list:
            CaseStatusManage().to_failed(failed_test_case[0])

    @classmethod
    def _refresh_test_case_file(cls):
        """
        新创建 与 正在运行的: 存在不动,
        新创建状态 -> 运行
        错误用例 -> 错误并停止
        :return:
        """
        test_case_root_dir = root_dir + '/blog/tests/testcase/'
        if not os.path.exists(test_case_root_dir):
            os.mkdir(test_case_root_dir)
        # 用例不是太多的情况下全部查出来
        # created running
        created_running_cases = db.session.query(TestCases).filter(
            TestCases.status.in_([CaseStatus.CREATED.value,
                                  CaseStatus.RUNNING.value])
        ).order_by(
            TestCases.id.asc()
        ).all()
        created_running_case_ids = [test_case.id for test_case in created_running_cases]

        # 所有已存在文件
        test_case_files = os.listdir(test_case_root_dir)
        test_case_files_map = {int(test_case_file.split('_')[0]): test_case_file for test_case_file in test_case_files}

        # 非上线用例删除
        for cur_case_id in test_case_files_map.keys():
            if cur_case_id not in created_running_case_ids:
                os.remove(test_case_root_dir + test_case_files_map[cur_case_id])
        # 不存在用例：创建
        # 近期更新：更新
        # 其它：不操作
        for test_case in created_running_cases:
            # 新上线用例创建
            if test_case.id not in test_case_files_map.keys():
                test_case_file = test_case_root_dir + str(test_case.id) + '_case.json'

                with open(test_case_file, 'w') as f:
                    # 标识一下用例与本条执行的关系
                    case_json = test_case.to_json()['case_json']
                    case_json['config']['name'] = str(test_case.to_json()['id']) + '_' + case_json['config']['name']
                    json.dump(case_json, f)

                CaseStatusManage().to_running(test_case.id)
            # 7min 内更新的重建
            elif test_case.id in test_case_files_map.keys() and test_case.updated_at > cls._interval(420):
                os.remove(test_case_root_dir + test_case_files_map[test_case.id])
                test_case_file = test_case_root_dir + str(test_case.id) + '_case.json'
                with open(test_case_file, 'w') as f:
                    # 标识一下用例与本条执行的关系
                    case_json = test_case.to_json()['case_json']
                    case_json['config']['name'] = str(test_case.to_json()['id']) + '_' + case_json['config']['name']
                    json.dump(case_json, f)
                CaseStatusManage().to_running(test_case.id)


    @classmethod
    def _manage_test_case(cls):
        """
        执行测试用例
        :return:
        """
        test_case_root_dir = root_dir + '/blog/tests/testcase/'
        if not os.listdir(test_case_root_dir):
            return
        runner = HttpRunner(failfast=True, save_tests=False)
        summary = runner.run(test_case_root_dir)
        # 用例集失败
        if summary['success'] is False:
            for detail in summary['details']:
                # 用例失败
                if detail['success'] is False:
                    cls._to_failed_recode(detail)
                    # for record in detail['records']:
                    #     test_case_name = record['name']
                    #     test_case_status = record['status']
                    #     test_case_attachment = record['attachment']
                    #     test_case_meta_datas = record['meta_datas']
                    #     text = f'''
                    #     ## 用例状态
                    #
                    #     {test_case_status}
                    #
                    #     ## 用例详情
                    #
                    #     ```
                    #     {json.dumps(test_case_meta_datas, indent=2)}
                    #     ```
                    #     '''

    @classmethod
    def _to_failed_recode(cls, detail):
        """
        记录失败的测试用例到数据库
        :param detail:
        :return:
        """
        failed_test_case_id = int(detail['name'].split('_')[0])

        test_cases_json = db.session.query(TestCases.case_json).filter(
            TestCases.id == failed_test_case_id
        ).first()
        test_case_fh = TestCasesFailedHistory(
            test_case_id=failed_test_case_id,
            test_case_json=test_cases_json
        )
        db.session.add(test_case_fh)
        db.session.commit()


scheduler_fude.add_job(BackGroundJob.testcase_1m_job, 'interval', minutes=1)
scheduler_fude.add_job(BackGroundJob.testcase_5m_job, 'interval', minutes=5)
scheduler_fude.add_job(BackGroundJob.testcase_10m_job, 'interval', minutes=10)
