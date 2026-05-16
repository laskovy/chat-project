from  main_app.views import render_reg, render_login
from project.settings import project
from main_app.views import *



project.add_url_rule(rule = '/registration', view_func = render_reg, methods=["GET", "POST"])
project.add_url_rule(rule='/login', view_func=render_login, methods=["GET", "POST"])
project.add_url_rule(rule='/verify', view_func=verify_account)
