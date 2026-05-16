import flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from .models import User, DATA_BASE
from project.mail import send_email
from itsdangerous import URLSafeTimedSerializer

serializer = URLSafeTimedSerializer("my_secret_key")

def render_reg():

    if flask.request.method == "POST":
        email = flask.request.form.get("email")
        password = flask.request.form.get("password")
        confirm_password = flask.request.form.get("confirm_password")
        if password == confirm_password:
            verify_code = serializer.dumps(email)
            user = User(
                email=email,
                password=generate_password_hash(password),
                verify_code=verify_code
            )
            DATA_BASE.session.add(user)
            DATA_BASE.session.commit()
            verify_link =  f"http://127.0.0.1:5000/verify?code={verify_code}"
            send_email(user_email=email, verify_link=verify_link)
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

def verify_account():
    code = flask.request.args.get("code")
    try:
        email = serializer.loads(code, max_age=900)
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_active = True
            DATA_BASE.session.commit()
            return flask.redirect("/login")
        return "Користувача не знайдено"
    except:
        return "Невірний код"

          