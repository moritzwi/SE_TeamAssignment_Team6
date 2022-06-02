from email.policy import default
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    
    
class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_1 = db.Column(db.String(150), default='image.jpg')
    image_2 = db.Column(db.String(150), default='image.jpg')
    image_3 = db.Column(db.String(150), default='image.jpg')
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, price, keywords, description, image_1, image_2, image_3): 
        self.name = name
        self.price = price
        self.keywords = keywords
        self.description = description
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3