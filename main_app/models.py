from project.db import*
from flask_login import UserMixin

class User(DATA_BASE.Model, UserMixin):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    email = DATA_BASE.Column(DATA_BASE.String, unique=True, nullable=False)
    password = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    