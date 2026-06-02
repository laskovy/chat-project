from project.db import*
from flask_login import UserMixin



group_users = DATA_BASE.Table(
    "group_users",
    DATA_BASE.Column("user_id", DATA_BASE.Integer, DATA_BASE.ForeignKey("user.id"), primary_key=True),
    DATA_BASE.Column("group_id", DATA_BASE.Integer, DATA_BASE.ForeignKey("group.id"), primary_key=True)
)
class User(DATA_BASE.Model, UserMixin):
    id = DATA_BASE.Column(DATA_BASE.Integer, primary_key=True)
    email = DATA_BASE.Column(DATA_BASE.String, unique=True, nullable=False)
    password = DATA_BASE.Column(DATA_BASE.String, nullable=False)
    is_active = DATA_BASE.Column(DATA_BASE.Boolean, default=False)
    verify_code = DATA_BASE.Column(DATA_BASE.String, nullable=True)


    groups_created = DATA_BASE.relationship("Group", back_populates="creator")
    groups = DATA_BASE.relationship("Group", secondary=group_users, back_populates="members")
    messages = DATA_BASE.relationship("Message", back_populates="user")
    