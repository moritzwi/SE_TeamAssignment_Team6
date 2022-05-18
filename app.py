from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team6.sqlite3' 
app.config['SECRET_KEY'] = "qwerasdf"

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.debug = True
    db.create_all() 
    app.run()