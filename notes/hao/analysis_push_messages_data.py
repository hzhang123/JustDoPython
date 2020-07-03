# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  analysis_qs.py
@CreateTime     :  2020/6/29 10:22
------------------------------------
"""
# 初始化配置文件
import os
import time
from datetime import timedelta, date

import pandas as pd
import psycopg2
import requests
from dingtalkchatbot.chatbot import DingtalkChatbot
from pyhocon import ConfigFactory

from notes.hao.tools import dataframe_to_image, upload_image

conf = ConfigFactory.parse_file(f'{os.path.abspath(os.path.dirname(__file__))}/../conf/push-monit.conf')
message_sent = 'gio_push_message_sent'
message_arrived = 'gio_push_message_arrived'
message_clicked = 'gio_push_message_clicked'
message_name = 'gio_push_message_name'
#
growing_conn = psycopg2.connect(
    host=conf.db_basic.host,
    port=conf.db_basic.port,
    database=conf.db_names.growing,
    user=conf.db_basic.user,
    password=conf.db_basic.password)

events_conn = psycopg2.connect(
    host=conf.db_basic.host,
    port=conf.db_basic.port,
    database=conf.db_names.events,
    user=conf.db_basic.user,
    password=conf.db_basic.password)

push_messages_data = pd.read_sql_query(
    f'''
    select
        t3.name as project_name,
        t1.ai as project_ai,
        t1.name as {message_name},
        t1.state,
        t4.name as segment_name,
        t4.user_num
    from
        push_messages t1
        join push_rules t2 on t1.id = t2.message_id
        join projects t3 on t1.ai = t3.keyid
        join user_segmentations t4 on split_part(t1.audience_id, ':', 2) :: int = t4.id
    where
        t2.start_at between TIMESTAMP 'today' - interval '1 days 8 hours' 
        and TIMESTAMP 'today' - interval '8 hours' 
        and t1.type = 'push'
    group by t3.name, t1.ai, t1.name, t1.state, t4.name, t4.user_num;
    ''',
    growing_conn
)

# 昨日存在推送的ais
ais = tuple(push_messages_data['project_ai'].drop_duplicates())

event_data = pd.read_sql_query(
    f'''
    select
        id as rule_id,
        project_id,
        key as event_key,
        ai as project_ai
    from
        custom_events
    where
        ai in {str(ais)}
        and key in ('{message_sent}', '{message_arrived}', '{message_clicked}')
        and status = 'activated';
    ''',
    events_conn
).sort_values(by='project_id')
growing_conn.close()
events_conn.close()

# 通过qs查询昨日推送数据
datas = pd.DataFrame(columns=['project_ai', message_name, message_sent, message_arrived, message_clicked])
for ai in ais:
    events = event_data[event_data['project_ai'] == ai]
    sent_rule_id = events[events['event_key'] == message_sent]['rule_id'].iloc[0]
    arrived_rule_id = events[events['event_key'] == message_arrived]['rule_id'].iloc[0]
    clicked_rule_id = events[events['event_key'] == message_clicked]['rule_id'].iloc[0]

    body = {
        "ai": ai,
        "exprs": f"c_{sent_rule_id}_distinct_;c_{arrived_rule_id}_distinct_;c_{clicked_rule_id}_distinct_",
        "beginTime": int(time.mktime((date.today() + timedelta(days=-1)).timetuple())) * 1000,
        "endTime": (int(time.mktime((date.today()).timetuple())) * 1000) - 1,
        "dimensions": "var_gio_push_message_name",
        "userScope": "uv",
        "interval": 86400000,
        "order": "col_0 desc",
        "limit": 20,
        "dimFilter": {
            "op": "and",
            "exprs": [{
                "op": "in",
                "key": "var_gio_push_message_name",
                "name": "触达推送名称",
                "values": list(push_messages_data[push_messages_data['project_ai'] == ai][message_name])
            }]
        },
        "exprWithFilters": [
            {"id": f"{sent_rule_id}", "exprType": "custom", "action": "distinct"},
            {"id": f"{arrived_rule_id}", "exprType": "custom", "action": "distinct"},
            {"id": f"{clicked_rule_id}", "exprType": "custom", "action": "distinct"}
        ]
    }

    r = requests.post(
        url=f'{conf.qs.host}{conf.qs.table_path}',
        json=body
    )
    if r.json()['status'] == 'success':
        data = r.json()['data']
        for row in data:
            datas = datas.append({
                'project_ai': ai,
                message_name: row[3],
                message_sent: row[0][0],
                message_arrived: row[1][0],
                message_clicked: row[2][0]
            }, ignore_index=True)

# 推送任务信息与送达数据merge
push_data = pd.merge(
    push_messages_data, datas, on=['project_ai', message_name]
).loc[:, ['project_name',
          message_name,
          'segment_name',
          'user_num',
          message_sent,
          message_arrived,
          message_clicked]]

# 比率计算
push_data['分群有效率'] = (
        push_data[message_sent].astype('float32') /
        push_data['user_num'].astype('float32')
)
push_data['送达率'] = (
        push_data[message_arrived].astype('float32') /
        push_data[message_sent].astype('float32')
)
push_data['点击率'] = (
        push_data[message_clicked].astype('float32') /
        push_data[message_arrived].astype('float32')
)

# 重命名列
push_data = push_data.rename(columns={
    "project_name": "项目名称",
    message_name: "推送任务",
    "segment_name": "分群名",
    "user_num": "分群人数",
    message_sent: "发送设备数",
    message_arrived: "送达设备数",
    message_clicked: "点击数"
})
# 排序
result = push_data.sort_values(by='送达率', ascending=False)
result['分群有效率'] = result['分群有效率'].apply(lambda x: format(x, '.2%'))
result['送达率'] = result['送达率'].apply(lambda x: format(x, '.2%'))
result['点击率'] = result['点击率'].apply(lambda x: format(x, '.2%'))

image = dataframe_to_image(result)
url = upload_image(conf, image)

xiaoding = DingtalkChatbot(webhook=conf.dingding.webhook, secret=conf.dingding.secret)
xiaoding.send_markdown(title='昨日推送\n',
                       text='#### 推送数据详情\n\n'
                            f'![报告]({url})\n',
                       is_at_all=False)
