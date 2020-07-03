# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  analysis_messages.py
@CreateTime     :  2020/7/2 16:16
------------------------------------
"""
import os

import imgkit
import pandas as pd
import psycopg2
from IPython import display
from dingtalkchatbot.chatbot import DingtalkChatbot

from pyhocon import ConfigFactory

from notes.hao.tools import dataframe_to_image, upload_image

conf = ConfigFactory.parse_file(f'{os.path.abspath(os.path.dirname(__file__))}/../conf/push-monit.conf')

growing_conn = psycopg2.connect(
    host=conf.db_basic.host,
    port=conf.db_basic.port,
    database=conf.db_names.growing,
    user=conf.db_basic.user,
    password=conf.db_basic.password)

messages_sql = f'''
-- 因为状态变化不唯一所以无法确定下线被修改为草稿状态的，以及其他情况可能漏掉
WITH messages_data AS (
/*
弹窗与banner
 1. 一直在线
 2. 上线到昨日下线（删除的无法统计, 不知道删除前的状态）
*/
SELECT
	"id" as message_id, project_id, "name" as message_name, "type" as message_type, platform
FROM push_messages t1
WHERE
	(("id" in (
				SELECT DISTINCT message_id 
				FROM push_rules 
				WHERE 
					end_at > TIMESTAMP 'today' - interval '1 days 8 hours' 
					AND activate_at < TIMESTAMP 'today' - INTERVAL '8 hours' )
		  AND t1."state" = 'activated')
		OR (t1."state" = 'stop' AND updated_at > TIMESTAMP 'today' - interval '1 days 8 hours'))
	AND "type" IN ('popupWindow')
UNION
/*
*/
SELECT
	"id" as message_id, project_id, "name" as message_name, "type" as message_type, platform
FROM push_messages
WHERE
	"id" in (
		SELECT 
			DISTINCT message_id 
		FROM push_rules 
		WHERE
			start_at between TIMESTAMP 'today' - interval '1 days 8 hours' 
        AND TIMESTAMP 'today' - interval '8 hours' 
	)
	AND "type" IN ('push')
UNION
/*
实验弹窗
1. 判断弹窗子信息可能在线的
2. 取父信息中包含可能在线的子信息，且父信息不是草稿状态
*/
SELECT
	"id" as message_id, project_id, "name" as message_name, 'abTest' as message_type, platform
FROM ab_test 
WHERE 
	latest_messages && ARRAY(
		SELECT "id" as ab_test_message_id
		FROM ab_test_messages t1
		WHERE
				(("id" in (
						SELECT DISTINCT message_id 
						FROM ab_test_rules 
						WHERE 
							end_at > TIMESTAMP 'today' - interval '1 days 8 hours' 
							AND activate_at < TIMESTAMP 'today' - INTERVAL '8 hours' )
					AND t1."state" = 'activated')
				OR (t1."state" = 'stop' AND updated_at > TIMESTAMP 'today' - interval '1 days 8 hours'))
			AND "state" IN ('activated'))
	AND state != 'draft'
UNION
/*
资源位与弹窗规则（除类型、online_messages）其余相同
*/
SELECT
	"id" as message_id, project_id, "name" as message_name, "type" as message_type, platform
FROM online_messages t1
WHERE
	(("id" in (
				SELECT DISTINCT message_id 
				FROM push_rules 
				WHERE 
					end_at > TIMESTAMP 'today' - interval '1 days 8 hours' 
					AND activate_at < TIMESTAMP 'today' - INTERVAL '8 hours' )
		  AND t1."state" = 'activated')
		OR (t1."state" = 'stop' AND updated_at > TIMESTAMP 'today' - interval '1 days 8 hours'))
	AND "type" IN ('banner')
UNION
/*
webhook
*/
SELECT
	"id" as message_id, project_id, "name" as message_name, 'webhook' as message_type, '' as platform
FROM webhook
WHERE
	start_at BETWEEN TIMESTAMP 'today' - interval '1 days 8 hours' 
		AND TIMESTAMP 'today' - interval '8 hours')
SELECT 
	t2."name" AS project_name, 
	CASE t1.message_type 
		WHEN 'popupWindow' THEN '普通弹窗'
	    WHEN 'push' THEN '推送'
	    WHEN 'banner' THEN '资源位'
	    WHEN 'abTest' THEN '测试弹窗'
	    WHEN 'webhook' THEN 'WebHook'
	END message_type,
	count(1) as cnt 
FROM 
	messages_data t1 JOIN projects t2 ON t1.project_id = t2."id"
WHERE t1.project_id NOT IN {str(tuple(conf.project.exclude)).replace(',)', ')')}
GROUP BY 
	t1.project_id, t2."name", t1.message_type 
ORDER BY t1.project_id;
'''

messages_data = pd.read_sql_query(messages_sql, growing_conn)
growing_conn.close()

# 数据透视
messages_data = messages_data.rename(columns={"project_name": "项目名称", "message_type": "任务类型"})
result = messages_data.pivot_table('cnt', index='项目名称', columns='任务类型').fillna(0)
# 追加总计
result = result.reset_index().append(result.sum(axis=0).to_dict(), ignore_index=True).fillna('总计').set_index('项目名称')

image = dataframe_to_image(result)
url = upload_image(conf, image)

xiaoding = DingtalkChatbot(webhook=conf.dingding.webhook, secret=conf.dingding.secret)
xiaoding.send_markdown(title='昨日用户运营使用情况\n', text='#### 数据详情\n\n'
                                                  f'![报告]({url})\n',
                       is_at_all=False)
