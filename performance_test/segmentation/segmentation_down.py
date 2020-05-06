# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  segmentation_down.py
@CreateTime     :  2020/4/23 13:28
------------------------------------
"""
import os
import time

import grpc
import pandas as pd
from gevent._semaphore import Semaphore
from locust import events, Locust, TaskSet, task, between
from numpy import *

from segmentation.segmentation_pb2 import CreateSegmentExportJobRequest
from segmentation.segmentation_pb2_grpc import SegServiceStub

all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()


def on_hatch_complete(**kwargs):
    all_locusts_spawned.release()


events.hatch_complete += on_hatch_complete


class CreateSegmentExportJobGrpc(object):
    """
    编写grpc类用来替换self.client的http实例
    下面的两个钩子事件是为了收集统计信息，不然无法收到统计信息
        events.request_success.fire()
        events.request_failure.fire()
    """

    def __init__(self):
        self.name = 'RequestM'

    def post(self, host, port, data):
        # 开始时间
        start_time = int(time.time())
        try:

            # 创建链接
            channel = grpc.insecure_channel(host + ':' + port)
            stub = SegServiceStub(channel=channel)

            # 调用
            response = stub.CreateSegmentExportJob(
                CreateSegmentExportJobRequest(id=data['id'], project_id=data['project_id'])
            )
            while response.status == 'doing':
                response = stub.CreateSegmentExportJob(
                    CreateSegmentExportJobRequest(id=data['id'], project_id=data['project_id'])
                )
                time.sleep(0.5)
            # 结束时间
            total_time = int((time.time() - start_time) * 1000)
            if response.status != 'done':
                raise Exception
            events.request_success.fire(
                request_type='grpc',
                name=self.name,
                response_time=total_time,
                response_length=0
            )

        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(
                request_type='grpc',
                name=self.name,
                response_time=total_time,
                response_length=0,
                exception=e,
            )
        finally:
            return response


class GrpcLocust(Locust):
    """
    GrpcLocust从Locust继承； 这里主要是将self.client重新实例成
    """
    def __init__(self, *args, **kwargs):
        super(GrpcLocust, self).__init__(*args, **kwargs)
        self.client = CreateSegmentExportJobGrpc()


class SegmentsDown(TaskSet):

    @task(1)
    def segment_export_test(self):
        row = Segments.next()
        if row[0] == -1:
            exit()
        else:
            data = {
                'id': row[0],
                'project_id': 3
            }
            r = self.client.post(host='*', port='*', data=data)


class WebsiteUser(GrpcLocust):
    task_set = SegmentsDown
    wait_time = between(2, 5)


class Segments(object):
    start = end = 40
    df = pd.read_csv(os.path.abspath(os.path.dirname(__file__)) + '/user_segmentations.csv')

    @classmethod
    def next(cls):
        # cls.df.shape[0]
        if cls.end <= 1000:
            cls.start += 1
            cls.end += 1
            return cls.df.loc[cls.start:cls.end, ['id', 'name', 'type']].values[0]
        else:
            print('测试完成')
            return [-1]
