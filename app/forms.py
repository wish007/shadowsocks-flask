
from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms import StringField, SubmitField
from wtforms.validators import Required


# 定义一个表单类，用于提交表单
class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class LoginForm(Form):
    name = TextField('Name', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Remember_me', default=False)
