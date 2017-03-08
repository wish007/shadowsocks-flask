# -*- coding:utf-8 -*-


from flask import Flask
# 将Flask-Bootstrap从flask.ext命名空间导入
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# 初始化flask应用
app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap(app)

# 初始化数据库
db = SQLAlchemy(app)

# 初始化flask-Login
lm = LoginManager()
lm.setup_app(app)

from app import views
