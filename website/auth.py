import email
import imp
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect password.', category='error')
        else:
            flash('Username does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        email = request.form.get('email')
        
        user = User.query.filter_by(username=username).first()
        email = User.query.filter_by(email=email).first()
        
        if user:
            flash('Username already exist.', category='error')
        if email:
            flash('Email already exist.', category='error')
        elif len(email) < 4:
            flash("Email must be greater then 4 characters", category="error")
        elif len(username) < 5:
            flash("Username must be greater then 5 characters", category="error")
        elif len(name) < 2:
            flash("Name must be greater then 2 characters", category="error")
        elif len(password) < 8:
            flash("Password must be greater then 8 characters", category="error")
        else:
            new_user = User(email=email, username=username, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('User created!')
            return redirect(url_for('views.home'))
            
    return render_template("sign-up.html", user=current_user)


