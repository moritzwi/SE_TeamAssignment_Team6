from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from . import db
from .models import products


views = Blueprint('views', __name__)

@views.route('/')

def home():
    return render_template("home.html", user=current_user)

@views.route('/shop')
def shop():
    return render_template("shop.html", user=current_user)

### User Products ###

@views.route('/user-products')
def user_products():
    return render_template("user-products.html", user=current_user, products = products.query.all())

@views.route('/add-product', methods = ['GET', 'POST']) 
def add_product():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['price'] or not request.form['description']: 
            flash('Please enter all the fields', 'error')
        else:
            product = products(request.form['name'], 
                               request.form['price'], 
                               request.form['keywords'],
                               request.form['description'],
                               request.form.get("image1", False),
                               request.form.get("image2", False),
                               request.form.get("image3", False))
            db.session.add(product) 
            db.session.commit()
            
            flash('Record was successfully added') 
            return redirect(url_for('views.user_products'))
    return render_template('add-product.html', user=current_user)

@views.route('/edit-product')
def edit_product():
    return render_template("edit-product.html", user=current_user)

@views.route('/delete/<name>') 
def delete(name):
    product = products.query.filter_by(name = name).first() 
    db.session.delete(product)
    db.session.commit()
    return	render_template('user-products.html', products = products.query.all(), user=current_user)

