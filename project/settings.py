from flask import *
from main_app.app import applic
from flask_migrate import Migrate
from project.db import DATA_BASE
from .login_manager import login_manager
from flask_socketio import SocketIO


project = Flask(
    import_name="project"
)
project.secret_key = "secret_key"
login_manager.init_app(project)
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
project.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

DATA_BASE.init_app(project)

migrate = Migrate(project, DATA_BASE)
socketio = SocketIO(project)
