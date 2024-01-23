from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category =  db.Column(db.Integer)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    materials = db.Column(db.String(1000))
    instruction_title = db.Column(db.String(1000))
    instruction_description = db.Column(db.String(10000))
    # instruction_image = db.Column(db.Image)
    reference = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150 ), unique=True)
    password = db.Column(db.String (150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    posts = db.relationship('Post')

