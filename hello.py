# 使用render_template函数把JinJa2模板引擎集成到hello.py
# render-传递，template-模板
from flask import Flask, render_template, session, redirect, url_for, flash
# 将Flask-Bootstrap从flask.ext命名空间导入
from flask.ext.bootstrap import Bootstrap
# 导入和表单提交有关的类
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
# 将程序实例传入构造方法进行初始化
bootstrap = Bootstrap(app)
# 使用Flask-WTF设置一个密钥，避免跨站请求伪造攻击
app.config['SECRET_KEY'] = 'ThisIsAHardGuessString.&uY^%FG0-@Fv'

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

# 定义一个表单类，用于提交表单
class NameForm(Form):
    name = StringField('what is your name?', validators=[Required()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    # 用run方法启动Flask集成的Web服务器，并启用调试模式
    app.run(debug=True)
