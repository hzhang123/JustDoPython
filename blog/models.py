from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from blog import db, login


# 使用flask-login要继承 UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_see = db.Column(db.DateTime, default=datetime.utcnow)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        # digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        # return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'
        return 'http://imgrt.pconline.com.cn/images/upload/upc/tx/pcdlc/1612/07/c358/spcgroup/center_121x75/31726523_1481121411919_120x75.jpg'


# 加载所有用户
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer)

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class SchedulerHttpTask(db.Model):
    __tablename__ = 'scheduler_task'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    team = db.Column(db.String(128))
    service = db.Column(db.String(128))
    url = db.Column(db.TEXT)
    method = db.Column(db.String(128))
    body = db.Column(db.TEXT)
    assertion = db.Column(db.TEXT)
    expected = db.Column(db.TEXT)
    status = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return fields


#
# class Host(db.Model):
#     __tablename__ = 'host'
#     id = db.Column()
#     hostname = db.Column()
#     ip4 = db.Column()
#     port = db.Column()
#     id_isa = db.Column()
#     id_isa_pub = db.Column()
#     statue = db.Column()
