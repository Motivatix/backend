from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

app = None
db = None


def create_app(config_name):
    global app, db
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db = SQLAlchemy(app)

    from models import Person, Achievement
    from views import *
    return app
