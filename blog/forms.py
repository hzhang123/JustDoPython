# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  hzhang
------------------------------------
@File           :  forms.py
@CreateTime     :  2020/3/20 18:12
------------------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from blog.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名已存在.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱已注册.')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    about_me = TextAreaField('关于我', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')


class SchedulerTaskForm(FlaskForm):
    name = StringField('任务名', validators=[DataRequired(message='请输入用户名')])
    team = StringField('开发组', validators=[DataRequired(message='请输入用户名')])
    service = StringField('所属服务', validators=[DataRequired(message='请输入用户名')])
    url = StringField('URL', validators=[DataRequired(message='请输入用户名')])
    method = StringField('请求方法', validators=[DataRequired(message='请输入用户名')])
    body = TextAreaField('body', validators=[DataRequired(message='请输入用户名')])
    assertion = StringField('断言方法', validators=[DataRequired(message='请输入用户名')])
    expected = TextAreaField('预期结果', validators=[DataRequired(message='请输入用户名')])
    submit = SubmitField('添加任务')


class TestCasesForm(FlaskForm):
    name = StringField('任务名', validators=[DataRequired(message='请输入用户名')])
    team = StringField('开发组', validators=[DataRequired(message='请输入用户名')])
    service = StringField('所属服务', validators=[DataRequired(message='请输入用户名')])
    case_json = TextAreaField('用例Json', validators=[DataRequired(message='请输入用户名')])
    submit = SubmitField('添加任务')
