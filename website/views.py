from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from .forms import Addproduct


views = Blueprint('views', __name__)

@views.route('/')

def home():
    return render_template("home.html", user=current_user)

@views.route('/shop')
def shop():
    return render_template("shop.html", user=current_user)

@views.route('/user-products')
def user_products():
    return render_template("user-products.html", user=current_user)

@views.route('/add-product', methods=['POST', 'GET'])
def add_product():
    form = Addproduct(request.form)
    return render_template("add-product.html", user=current_user, form=form)

@views.route('/edit-product')
def edit_product():
    return render_template("edit-product.html", user=current_user)

