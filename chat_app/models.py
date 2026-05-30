from project.db import *
from main_app.models import User

class Group(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    name = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    creator_id = DATA_BASE.Column(DATA_BASE.Integer, DATA_BASE.ForeignKey("user.id"))

    creator = DATA_BASE.relationship("User", back_populates="groups")
    messages = DATA_BASE.relationship("Message", back_populates="group")


class Message(DATA_BASE.Model):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    text = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    user_id = DATA_BASE.Column(DATA_BASE.Integer, DATA_BASE.ForeignKey("user.id"))
    group_id = DATA_BASE.Column(DATA_BASE.Integer, DATA_BASE.ForeignKey("group.id"))

    user = DATA_BASE.relationship("User", back_populates="messages")
    group = DATA_BASE.relationship("Group", back_populates="messages")