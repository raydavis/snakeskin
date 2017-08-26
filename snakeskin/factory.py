from flask import Flask

from snakeskin.configs import load_configs
from snakeskin.db import initialize_db
from snakeskin.routes import register_routes

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import find_modules, import_string

db = SQLAlchemy()


def create_app():
    """Initialize app with configs."""
    app = Flask(__name__.split('.')[0])

    load_configs(app)
    initialize_db(app)

    with app.app_context():
        register_routes(app)

    return app
