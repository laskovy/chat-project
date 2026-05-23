import flask

applic = flask.Blueprint(
    import_name="main_app",
    name="app1",
    template_folder="templates",
)