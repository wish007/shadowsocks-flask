#-*- coding:utf-8 -*-

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    """每一个属性定义一个字段"""
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
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

    @classmethod
    def login_check(cls, user_name):
        user = cls.query.filter(db.or_(
            User.nickname == user_name, User.email == user_name)).first()

        if not user:
            return None
        else:
        	return user

    def __repr__(self):
        return '<User %r>' % (self.nickname)
