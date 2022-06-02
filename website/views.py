from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask_login import current_user, login_required
from . import db
from .models import Products


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user=current_user, products = Products.query.all()) 

@views.route('/shop')
def shop():
    return render_template("shop.html", user=current_user, products = Products.query.all())

### User Products ###

@views.route('/user-products')
def user_products():
    return render_template("user-products.html", user=current_user, products = Products.query.all())

@views.route('/add-product', methods = ['GET', 'POST']) 
def add_product():
    if request.method == 'POST':
        if not request.form.get('name') or not request.form.get('price') or not request.form.get('description'): 
            flash('Please enter all the fields', 'error')
        else:
            name = request.form.get('name')
            price = request.form.get('price'), 
            keywords = request.form.get('keywords'),
            description = request.form.get('description'),
            image_1 = request.files.get('image_1'),
            image_2 = request.files.get('image_2'),
            image_3 = request.files.get('image_3')
    
            product = Products(name=name, 
                            price=price, 
                            keywords=keywords, 
                            description=description, 
                            image_1=image_1, 
                            image_2=image_2, 
                            image_3=image_3)
            db.session.add(product) 
            db.session.commit()
                    
            flash('Product was successfully added') 
            return redirect(url_for('views.user_products'))
    return render_template('add-product.html', user=current_user)

@views.route('/edit-product')
def edit_product():
    return render_template("edit-product.html", user=current_user)

@views.route('/delete/<name>') 
def delete(name):
    product = Products.query.filter_by(name = name).first() 
    db.session.delete(product)
    db.session.commit()
    return	render_template('user-products.html', products = Products.query.all(), user=current_user)

