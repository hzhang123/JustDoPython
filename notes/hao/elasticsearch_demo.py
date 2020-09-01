# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  elasticsearch_demo.py
@CreateTime     :  2020/6/16 16:30
------------------------------------
"""
import re

from elasticsearch import Elasticsearch


def scrolling_es_result(body):
    names = []
    ip = ['host']
    es = Elasticsearch(hosts=ip, timeout=40)

    _scroll_id = None

    while True:
        if not _scroll_id:
            page = es.search(scroll='2m', size=7000, body=body)
        else:
            page = es.scroll(scroll_id=_scroll_id, scroll='2m')
        _scroll_id = page["_scroll_id"]
        scroll_size = len(page['hits']['hits'])
        if scroll_size < 1:
            break
        regex = r"name:(.*?),"
        print(scroll_size)
        for message in page['hits']['hits']:
            name = re.search(regex, message['_source']['message'])[1]
            if name not in names:
                names.append(name)

    print(names)


if __name__ == '__main__':
    body = {
        "query": {
            "bool": {
                "must": [{
                    "query_string": {
                        "query": '\"Find empty\"',
                        "analyze_wildcard": True,
                        "default_field": "*"
                    }
                }, {
                    "match_phrase": {
                        "service": {
                            "query": "marketing-automation"
                        }
                    }
                }, {
                    "range": {
                        "@timestamp": {
                            "gte": 1597939200000,
                            "lte": 1598494392501,
                            "format": "epoch_millis"
                        }
                    }
                }],
                "filter": [],
                "should": [],
                "must_not": []
            }
        },
        "sort": {
            "@timestamp": {
                "order": "asc"  # asc升序， desc降序
            }
        }
    }
    scrolling_es_result(body)
