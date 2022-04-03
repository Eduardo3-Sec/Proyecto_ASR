from datetime import datetime
from time import time
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    username = db.Column(db.String(20), primary_key=True)
    password = db.COlumn(db.String(20)) 