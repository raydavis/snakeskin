from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import setup

# Initialize app with configs.
app = Flask(__name__.split('.')[0])
setup.load_configs(app)

# Database initialization depends on configs being in place.
db = SQLAlchemy(app)
db.init_app(app)

# Route registration depends on the database being in place (because of dependencies on models).
setup.register_routes(app)
