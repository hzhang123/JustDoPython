# !/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

def job_0():
    print('test job')



    
def job_6():
    r = requests.get(
        url=f'http://messages-release.growingio.com/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications?url_scheme=growing.638b52710867187c&u=20E6240E-C859-40A6-8604-97A1503DEBC5&cs=20E6240E-C859-40A6-8604-97A1503DEBC5'
    )
    assert '弹窗20200303210125' in r.text
    

    
def job_7():
    r = requests.get(
        url=f'http://messages-release.growingio.com/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications?url_scheme=growing.638b52710867187c&u=20E6240E-C859-40A6-8604-97A1503DEBC5&cs=20E6240E-C859-40A6-8604-97A1503DEBC5'
    )
    assert '不存在的' in r.text
    

    
def job_8():
    r = requests.get(
        url=f'http://messages-release.growingio.com/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications?url_scheme=growing.638b52710867187c&u=20E6240E-C859-40A6-8604-97A1503DEBC5&cs=20E6240E-C859-40A6-8604-97A1503DEBC5'
    )
    assert '弹窗不存在' in r.text
    

    
def job_9():
    r = requests.get(
        url=f'http://messages-release.growingio.com/v3/0a1b4118dd954ec3bcc69da5138bdb96/notifications?url_scheme=growing.638b52710867187c&u=20E6240E-C859-40A6-8604-97A1503DEBC5&cs=20E6240E-C859-40A6-8604-97A1503DEBC5'
    )
    assert '弹窗20200303210125' in r.text
    
