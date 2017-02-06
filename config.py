import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'ThisIsAHardGuessString.&uY^%FG0-@Fv'

# 数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLAlchemy-migrate 数据文件存储的路径
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
