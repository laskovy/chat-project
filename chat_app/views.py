import flask
from flask_login import current_user
from project.db import DATA_BASE
from chat_app.models import Group


def render_chat():
    my_group = Group.query.filter_by(creator_id=current_user.id).first()

    return flask.render_template("chat.html",my_group=my_group)


def create_chat():
    name = flask.request.form.get("chat_name")
    group = Group(name=name, creator_id=current_user.id)
    DATA_BASE.session.add(group)
    DATA_BASE.session.commit()

    return flask.redirect("/chat")
