from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
app = None


def create_app(config_name):
    global app
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    with app.app_context():
        db.init_app(app)

    from models import Person, Achievement
    from views import *
    return app
