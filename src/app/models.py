from app import db 
from flask_login import UserMixin
from datetime import datetime, timezone
from sqlalchemy.sql import func
import uuid
from enum import Enum

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    password = db.Column(db.LargeBinary)
