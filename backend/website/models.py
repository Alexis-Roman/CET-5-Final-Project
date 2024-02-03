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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150 ), unique=True)
    password = db.Column(db.String (150))
    username = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post')
    discussions = db.relationship('Discussions')
    images = db.relationship('IMG')

class Discussions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dTitle = db.Column(db.String(1000))
    dDescription = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class IMG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
