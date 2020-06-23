# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  CreateSegmentsExportJob.py
@CreateTime     :  2020/4/20 15:14
------------------------------------
"""
import time

import pandas as pd

from segmentation_pb2 import *
from segmentation_pb2_grpc import *


def create_segment_export_job(host_ip, project_id, id):
    # 连接 rpc 服务器
    channel = grpc.insecure_channel(host_ip)
    # 调用 rpc 服务
    stub = SegServiceStub(channel)
    start_time = time.time()
    state = 'doing'
    i = 0
    while state == 'doing':
        response = stub.CreateSegmentExportJob(
            CreateSegmentExportJobRequest(id=id, project_id=project_id)
        )
        if i > 0:
            time.sleep(0.5)
        i += 1
        state = response.status
        print(response.status)
    print(response.status)
    print(time.time() - start_time, state)
    return time.time() - start_time, state


if __name__ == '__main__':
    df = pd.read_csv('user_segmentations.csv')
    usv_time = []
    uv_time = []
    for row in df.loc[0:1, ['id', 'name', 'type']].values:
        print(row[1], row[2], end=':')
        times, state = create_segment_export_job('*:111', 3, row[0])
        if row[2] == 'usv':
            usv_time.append(times)
        else:
            uv_time.append(times)
    create_segment_export_job('*:111', 3, 123)
    print(f'usv time:' + str(sum(usv_time) / len(usv_time)))
    print(f'uv time:' + str(sum(uv_time) / len(uv_time)))

    re = create_segment_export_job('10.0.0.156:19225', 3, 151284)
    print(re)
