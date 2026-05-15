import flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User, DATA_BASE


def render_reg():

    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        if password == confirm_password:
            user = User(
                email=email,
                password=generate_password_hash(password)
            )
            DATA_BASE.session.add(user)
            DATA_BASE.session.commit()
            return flask.redirect("/login")
    return flask.render_template("registration.html")

def render_login():
    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                

    return flask.render_template("login.html")