from flask import Flask
from flask_bootstrap import Bootstrap5


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap5(app)
    app.config["SECRET_KEY"] = "test"

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
