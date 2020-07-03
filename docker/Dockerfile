FROM centos:7

# centos7 isu第三方源 https://ius.io/setup
RUN yum -y install \
    https://repo.ius.io/ius-release-el7.rpm \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum install -y python36 python36-libs python36-devel python36-pip \
    && yum install -y postgresql-devel gcc git make openssl openssl-devel

COPY ./requirements.txt /app/requirements/txt
RUN pip3 install -r /app/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ --trusted-host pypi.tuna.tsinghua.edu.cn

RUN rm -rf /var/cache/yum/x86_64/7/*

ADD . /app
USER root
WORKDIR /app
