import hashlib
from datetime import datetime

from flask_login import UserMixin

from vulnbid import db


class User(UserMixin, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True)
    realname = db.Column(db.String(256))
    join_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    last_seen = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __repr__(self):
        _repr = '<models.User instance; ID: {}; username: {}>'
        return _repr.format(self.id, self.username)

    @staticmethod
    def generate_gravatar_url(username, size):
        GRAVATAR = 'http://www.gravatar.com/avatar/{}?d=identicon&s={}&r=pg'

        if not isinstance(size, int):
            raise Exception('Provided size must be of type int and a power of 2.')

        return GRAVATAR.format(
            str(hashlib.md5(username.encode('utf-8'))),
            str(size)
        )
