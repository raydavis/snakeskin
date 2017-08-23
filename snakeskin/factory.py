import importlib.util
import os

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Initialize app with configs."""
    app = Flask(__name__.split('.')[0])
    load_configs(app)
    return app


def initialize_db(app):
    """Initialize database object."""
    db.init_app(app)
    return db


def load_configs(app):
    """
    On app creation, load and and override configs in the following order:
     - config/default.py
     - config/{SNAKESKIN_ENV}.py
     - config/{SNAKESKIN_ENV}-local.py (excluded from version control; sensitive values go here)
    """
    load_config(app, 'default')
    # SNAKESKIN_ENV defaults to 'development'.
    snakeskin_env = os.environ.get('SNAKESKIN_ENV', 'development')
    load_config(app, snakeskin_env)
    load_config(app, '{}-local'.format(snakeskin_env))


def load_config(app, config_name):
    """Load an individual configuration file if it exists."""
    config_path = 'config.{}'.format(config_name)
    if importlib.util.find_spec(config_path) is not None:
        app.config.from_object(config_path)


def register_routes(app):
    """Register app routes."""

    # Register API routes as blueprints.
    from snakeskin.api.tenant_controller import tenant
    from snakeskin.api.user_controller import user
    app.register_blueprint(tenant)
    app.register_blueprint(user)

    # Routes not matched by the API are handled by the front end.
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def front_end_route(**kwargs):
        return make_response(open('snakeskin/templates/index.html').read())
