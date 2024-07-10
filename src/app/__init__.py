# code taken from homework 2 - user authentication
from flask import Flask
import bcrypt
import os

app = Flask("Authentication Web App")
app.secret_key = os.environ['SECRET_KEY']

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app1.db'
db.init_app(app)

from sqlalchemy import inspect

from app.models import User

# create tables
with app.app_context():
    try:
        db.create_all()
    except:
        pass

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes