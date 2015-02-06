from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config.from_object('config')

# DB connection
engine = create_engine(app.config['DATABASE_URL'])

# Session factory
DBSession = sessionmaker(bind=engine)

from motivatix.views import *
