from motivatix import db

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)

	def __repr__(self):
		return "<Person(name='%s')>" % (self.name)
