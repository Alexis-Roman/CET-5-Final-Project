from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category =  db.Column(db.Integer)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    instruction_title = db.Column(db.String(1000))
    instruction_description = db.Column(db.String(10000))
    reference = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    image_id = db.Column(db.Integer, db.ForeignKey('img.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='posts', lazy=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150 ), unique=True)
    password = db.Column(db.String (150))
    username = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Discussions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dTitle = db.Column(db.String(1000))
    dDescription = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='discussions', lazy=True)
    image_id = db.Column(db.Integer, db.ForeignKey('img.id'))
    image = db.relationship('IMG', backref='discussion', lazy=True)

class IMG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_filename = db.Column(db.String(255), nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='images', lazy=True)
    posts = db.relationship('Post', lazy=True)
