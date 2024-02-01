from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import os


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category =  db.Column(db.Integer)
    title = db.Column(db.String(1000))
    description = db.Column(db.String(1000))
    instruction_title = db.Column(db.String(1000))
    instruction_description = db.Column(db.String(10000))
    reference = db.Column(db.String(1000))
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

class Discussions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dTitle = db.Column(db.String(1000))
    dDescription = db.Column(db.String(1000))
    dImage = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def save_image(self, image):
        if image:
            image_name = f"{self.id}_{image.filename}"
            image_path = os.path.join('backend/website/static/uploaded', image_name)  # Adjust the path as needed
            image.save(image_path)
            self.dImage = image_name
            return image_name
        return None
