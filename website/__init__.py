from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_url_path='/website/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team6.sqlite3' 
    app.config['SECRET_KEY'] = "qwerasdf"
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, products
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        try:
            return User.query.get(int(id))
        except:
            return None
    
    return app

def create_database(app):
    db.create_all(app=app)
    print('Created Database!')