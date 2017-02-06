# -*- coding:utf-8 -*-


from flask import Flask
# 将Flask-Bootstrap从flask.ext命名空间导入
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config')

from app import views
