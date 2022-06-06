from email.policy import default
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    products = db.relationship('products', backref='user')

    
class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sold = db.Column(db.String(80), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, price, keywords, description, sold, user_id = user_id): 
        self.name = name
        self.price = price
        self.keywords = keywords
        self.description = description
        self.sold = sold
        self.user_id = user_id