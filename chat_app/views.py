import flask
from flask_login import current_user
from project.db import DATA_BASE
from chat_app.models import Group
from project.settings import *


def render_chat():
    my_group = Group.query.filter_by(creator_id=current_user.id).first()
    groups = Group.query.filter(Group.creator_id != current_user.id).all()
    return flask.render_template("chat.html",my_group=my_group, groups=groups)


def create_chat():
    name = flask.request.form.get("chat_name")
    group = Group(name=name, creator_id=current_user.id)
    DATA_BASE.session.add(group)
    DATA_BASE.session.commit()
    socketio.emit("new_chat",{"id": group.id, "name": group.name, "creator_id": group.creator_id})
    return flask.redirect("/chat")

def delete_chat():
    group = Group.query.filter_by(creator_id=current_user.id).first()
    if group:
        DATA_BASE.session.delete(group)
        DATA_BASE.session.commit()
        socketio.emit("chat_deleted", {"id": group.id})
    return flask.redirect("/chat")

