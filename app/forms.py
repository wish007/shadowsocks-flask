# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, Length


# 定义一个表单类，用于提交表单
class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class LoginForm(Form):
    user_name = StringField('user name',
                            validators=[Required(), Length(max=15)])
    user_password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')


class SignUpForm(Form):
    user_name = StringField('user name',
                            validators=[Required(), Length(max=15)])
    user_password = PasswordField('password', validators=[Required()])
    user_email = StringField('user email',
                             validators=[Email(), Required(), Length(max=128)])
    submit = SubmitField('提交')
