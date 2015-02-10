from . import db

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	achievements = db.relationship('Achievement', backref='person', lazy='dynamic')

	def __repr__(self):
		return "<Person(name='%s')>" % (self.name)

class Achievement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.String, nullable=False)
	age = db.Column(db.Integer)
	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

	def __repr__(self):
		return "<Achievement(name='%s', age='%s')>" % (self.description, self.age)
