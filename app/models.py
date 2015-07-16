from app import db
from hashlib import md5


class Alarms(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	time = db.Column(db.String(10), index=True, unique=True)
	days = db.Column(db.String(120))
	sounds = db.Column(db.String(140))

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)