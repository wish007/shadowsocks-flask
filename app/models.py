#-*- coding:utf-8 -*-

from app import db
from werkzeug.security import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    """每一个属性定义一个字段"""
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # @classmethod
    # def login_check(cls, user_name, user_password):
    #     user = cls.query.filter_by(username=user_name).first()
    #     if user is not None and user.verify_password(user_password):
    #         login_user()
    #     # user = cls.query.filter(db.or_(
    #     #     User.username == user_name, User.email == user_name)).first()
    #
    #     if not user:
    #         return None
    #     else:
    #         return user

    def __repr__(self):
        return '<User %r>' % (self.username)
