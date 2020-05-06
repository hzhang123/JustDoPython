# !/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from blog import app, db
from blog.cases import cases_blueprint
from blog.forms import LoginForm, RegistrationForm, EditProfileForm
from blog.models import User

# app.register_blueprint(locust_hive, url_prefix='/locusts')
# app.register_blueprint(scheduler_task, url_prefix='/scheduler')
app.register_blueprint(cases_blueprint, url_prefix='/case')


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'zhanghao'}
    posts = [
        {
            'author': {'username': '张三'},
            'body': '这是模板循环例子～1'
        },
        {
            'author': {'username': '李四'},
            'body': '这是模板循环例子～2'
        }
    ]
    return render_template('index.html', title='我的', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 判断用户是否验证，如果验证返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # 对表格数据进行验证
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # 如果用户不存在或者密码不正确就会闪现这条信息
            flash(f'无效的用户名或密码')
            return redirect(url_for('login'))
        # 这是一个非常方便的方法，当用户名和密码都正确时来解决记住用户是否记住登录状态的问题
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            # flash(f'用户的登录名是{form.username.data}，是否记住我{form.remember_me.data}')
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='登录', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    # 判断当前用户是否验证，如果通过的话返回首页
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你注册成功')
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': '测试Post #1号'},
        {'author': user, 'body': '测试Post #2号'}
    ]
    return render_template('user.html', user=user, posts=posts)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('你的提交已变更')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='个人资料编辑', form=form)
