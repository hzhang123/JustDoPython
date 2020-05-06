# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  class_test.py
@CreateTime     :  2020/4/27 13:18
------------------------------------
"""
import json
import os

from dingtalkchatbot.chatbot import DingtalkChatbot
from httprunner.api import HttpRunner


def send_to_dingding_marketdown(title, text):
    webhook = ''
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title=title, text=text)

def job_1():
    runner = HttpRunner(
        failfast=True,
        save_tests=True,
        log_level="INFO",
        log_file="test.log"
    )

    summary = runner.run(os.path.abspath(os.path.dirname(__file__)).split('JustDoPython')[0] + 'JustDoPython/blog/tests/testcase')
    # 用例集失败
    if summary['success'] is False:
        for detail in summary['details']:
            # 用例失败
            if detail['success'] is False:
                for record in detail['records']:
                    test_case_name = record['name']
                    test_case_status = record['status']
                    test_case_attachment = record['attachment']
                    test_case_meta_datas =  record['meta_datas']
                    print('result' + str(test_case_name) + str(test_case_status) + str(test_case_attachment) + str(test_case_meta_datas))
                    text = f'''
                    ## 用例状态
                    
                    {test_case_status}
                    
                    ## 用例详情
                    
                    ```
                    {json.dumps(test_case_meta_datas)}
                    ```
                    
                    '''
                    print(json.dumps(test_case_meta_datas, indent=2))
                    # send_to_dingding_marketdown(title=f'API{test_case_name}', text=text)

if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # scheduler.add_job(job_1, 'interval', seconds=5)
    # scheduler.start()
    job_1()
    # MyHarParser(
    #     "/Users/growingio/Downloads/example.har"
    # ).gen_testcase("JSON")
