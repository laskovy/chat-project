import flask
from flask_login import current_user
from project.db import DATA_BASE
from chat_app.models import Group, Message
from project.settings import socketio
from flask_socketio import join_room, emit


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

@socketio.on("connect_chat")
def handle_connect_chat(data):
    group_id = data.get("group_id")
    group = Group.query.get(group_id)
    if group:
        join_room(f"chat_{group_id}")
        socketio.emit("chat_connected", {"group_id": group_id})


@socketio.on("send_message")
def handle_send_message(data):
    text = data.get("text")
    group_id = data.get("group_id")
    if not text or not group_id:
        return
    msg = Message(text=text, user_id=current_user.id, group_id=group_id)
    DATA_BASE.session.add(msg)
    DATA_BASE.session.commit()
    socketio.emit("new_message", {"id": msg.id, "text": msg.text, "user_id": msg.user_id, "group_id": msg.group_id}, room=f"chat_{group_id}")