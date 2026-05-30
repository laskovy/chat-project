from  main_app.views import render_reg, render_login
from project.settings import project
from main_app.views import *
from chat_app.views import render_chat



project.add_url_rule(rule = '/registration', view_func = render_reg, methods=["GET", "POST"])
project.add_url_rule(rule='/login', view_func=render_login, methods=["GET", "POST"])
project.add_url_rule(rule='/verify', view_func=verify_account)
project.add_url_rule(rule='/register_success', view_func=register_success)
project.add_url_rule(rule="/chat", view_func=render_chat)
