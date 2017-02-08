# -*- coding:utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email, Length


# 定义一个表单类，用于提交表单
class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')

# class LoginForm(Form):
#     name = TextField('Name', validators=[Required()])
#     password = PasswordField('password', validators=[Required()])
#     remember_me = BooleanField('Remember_me', default=False)

class LoginForm(Form):
    user_name = TextField('user name', validators=[Required(), Length(max=15)])
    # password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Log in')

class SignUpForm(Form):
    user_name = TextField('user name', validators=[Required(), Length(max=15)])
    # password = PasswordField('password', validators=[Required()])
    user_email = TextField('user email', validators=[Email(), Required(), Length(max=128)])
    submit = SubmitField('Sign up')
