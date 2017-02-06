# -*- coding:utf-8 -*-

# 使用render_template函数把JinJa2模板引擎集成到hello.py
from flask import render_template, session, redirect, url_for, flash
from app import app
# 导入和表单提交有关的类
from flask.ext.wtf import Form
from app.forms import NameForm, LoginForm


# 在视图函数中添加路由方法，使之能够渲染表单
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)
