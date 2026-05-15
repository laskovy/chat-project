from flask_login import LoginManager
from main_app.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(id: int):
    return User.query.get(id)
