from .db import *
from .loadenv import *
from .settings import *
from .urls import *
from .login_manager import *
from chat_app import *

project.register_blueprint(applic)
project.register_blueprint(chat_applic)