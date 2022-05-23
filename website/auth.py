from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        email = request.form.get('email')
        
        if len(email) < 4:
            flash("Email must be greater then 4 characters", category="error")
        if len(username) < 5:
            flash("Username must be greater then 5 characters", category="error")
        elif len(name) < 2:
            flash("Name must be greater then 2 characters", category="error")
        elif len(password) < 8:
            flash("Password must be greater then 8 characters", category="error")
        else:
            #add user to db
            pass
            
    return render_template("sign-up.html")


