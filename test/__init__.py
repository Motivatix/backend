from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.testing import TestCase

from ..motivatix import create_app, db
from ..motivatix.models import Person, Achievement

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
		larry_page = Person(name='Larry Page')
		self.db.session.add(larry_page)
		lp1 = Achievement(description='Started thinking about starting company', age=12)
		lp2 = Achievement(description='Founded Google', age=25)
		lp3 = Achievement(description='Announced Google Glass project', age=39)
		self.db.session.add(lp1)
		self.db.session.add(lp2)
		self.db.session.add(lp3)
		larry_page.achievements.append(lp1)
		larry_page.achievements.append(lp2)
		larry_page.achievements.append(lp3)

		steve_jobs = Person(name='Steve Jobs')
		self.db.session.add(steve_jobs)
		sj1 = Achievement(description='Founded Apple Computer Company with Wozniak', age=21)
		sj2 = Achievement(description='Stanford speech', age=50)
		self.db.session.add(sj1)
		self.db.session.add(sj2)
		steve_jobs.achievements.append(sj1)
		steve_jobs.achievements.append(sj2)

		self.db.session.commit()
