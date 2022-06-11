from csv import unix_dialect
from email.policy import default
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    products = db.relationship('products', backref='user')
    
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')
    
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
            if self.is_following(user):
                self.followed.remove(user)

    def is_following(self, user):
            return self.followed.filter(
                followers.c.followed_id == user.id).count() > 0
            
    def followed_products(self):
            return products.query.join(
                followers, (followers.c.followed_id == products.user_id)).filter(
                    followers.c.follower_id == self.id)
<<<<<<< HEAD

=======
>>>>>>> main

    
class products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    picture = db.Column(db.String(200), nullable=False)
    keywords = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    sold = db.Column(db.String(80), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, price, picture, keywords, description, sold, user_id = user_id): 
        self.name = name
        self.price = price
        self.picture = picture
        self.keywords = keywords
        self.description = description
        self.sold = sold
        self.user_id = user_id
