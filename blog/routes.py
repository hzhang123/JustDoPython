from flask import render_template, flash, redirect, url_for

from blog import app
from blog.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'用户的登录名是{form.username.data}，是否记住我{form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='登录', form=form)
