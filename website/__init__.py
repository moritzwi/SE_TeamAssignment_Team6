from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team6.sqlite3' 
    app.config['SECRET_KEY'] = "qwerasdf"
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app