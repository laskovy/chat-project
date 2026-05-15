from  main_app.views import render_reg, render_login
from project.settings import project



project.add_url_rule(rule = '/registration', view_func = render_reg, methods=["GET", "POST"])
project.add_url_rule(rule='/login', view_func=render_login, methods=["GET", "POST"])
