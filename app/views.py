# -*- coding:utf-8 -*-

import datetime
# 使用render_template函数把JinJa2模板引擎集成到hello.py
from flask import render_template, flash, redirect, session, url_for, request, g 
from flask.ext.login import login_user, logout_user, current_user, login_required 
from app.models import User, ROLE_USER, ROLE_ADMIN
from app import app, db, lm
# 导入和表单提交有关的类
# from flask.ext.wtf import Form
from app.forms import NameForm, LoginForm, SignUpForm


# 从数据库加载用户
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    # 验证用户是否被验证
    if current_user.is_authenticated():
        return redirect(url_for('index'))
    # 注册验证
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect(url_for('login'))

            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect(url_for("index", user_id=current_user.id))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect(url_for('login'))

    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    user = User()
    if form.validate_on_submit():
        user_name = request.form.get('user_name')
        user_email = request.form.get('user_email')

        register_check = User.query.filter(db.or_(
            User.nickname == user_name, User.email == user_email)).first()
        if register_check:
            flash("error: The user's name or email already exists!")
            return redirect(url_for('sign_up'))

        if len(user_name) and len(user_email):
            user.nickname = user_name
            user.email = user_email
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect(url_for('sign_up'))

            flash("Sign up successful!")
            return redirect(url_for('index'))

    return render_template("sign_up.html", form=form)
