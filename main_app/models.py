from project.db import*
from flask_login import UserMixin

class User(DATA_BASE.Model, UserMixin):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    email = DATA_BASE.Column(DATA_BASE.String, unique=True, nullable=False)
    password = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    is_active = DATA_BASE.Column(DATA_BASE.Boolean, default=False)
    verify_code = DATA_BASE.Column(DATA_BASE.String, nullable=True)

    groups = DATA_BASE.relationship("Group", back_populates="creator")
    messages = DATA_BASE.relationship("Message", back_populates="user")