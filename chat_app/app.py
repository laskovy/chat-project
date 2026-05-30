import flask

chat_applic = flask.Blueprint(
    import_name="chat_app",
    name="chat_app",
    template_folder="templates"
)