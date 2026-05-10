from project.db import*

class User(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    email = DATA_BASE.Column(DATA_BASE.String, unique=True, nullable=False)
    password = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    