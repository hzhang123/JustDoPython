# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  tools.py
@CreateTime     :  2020/7/3 12:02
------------------------------------
"""
import base64

import imgkit
import requests
from pandas import DataFrame


def dataframe_to_image(data: DataFrame):
    """
    返回html
    :param data:
    :return:
    """

    return imgkit.from_string(data.to_html(classes='pure-table pure-table-horizontal'),
                              False,
                              options={'encoding': 'utf8'},
                              css='table.css'
                              )


def upload_image(conf, image_str):
    """
    上传图片并返回url
    :param conf:
    :param image_str:
    :return:
    """
    image_base64 = str(base64.b64encode(image_str), encoding='UTF-8')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': conf.main.token,
    }
    r = requests.post(
        url=conf.main.url + conf.main.image_upload_path,
        json={'file': f'data:image/jpg;base64,{image_base64}'},
        headers=headers
    )
    return r.json()['url']
