from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.testing import TestCase

from motivatix import create_app, db
from motivatix.models import Person, Achievement


class BaseTestCase(TestCase):
    def create_app(self):
        self.app = create_app('testing')
        self.db = db

        return self.app

    def setUp(self):
        self.db.create_all()
        self.populate_database()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def populate_database(self):
        larry = Person(name='Larry Page')
        self.db.session.add(larry)
        achievementsLarry = [('Started thinking about starting company', 12),
                             ('Founded Google', 25),
                             ('Announced Google Glass project', 39)]
        for description, age in achievementsLarry:
            a = Achievement(description=description, age=age)
            self.db.session.add(a)
            larry.achievements.append(a)

        steve = Person(name='Steve Jobs')
        self.db.session.add(steve)
        achievementsSteve = [('Founded Apple Computer Company with Wozniak', 21),
                             ('Stanford speech', 50)]
        for description, age in achievementsSteve:
            a = Achievement(description=description, age=age)
            self.db.session.add(a)
            steve.achievements.append(a)

        self.db.session.commit()
