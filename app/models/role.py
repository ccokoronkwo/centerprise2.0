from . import db

class Role(db.Model):
	__tablename__ = 'role'
	id = db.Column(db.Integer(), primary_key=True)
	user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))
	user = db.relationship('User', back_populates='roles')

	def __repr__(self):
		return '<Role: {self.id}, {self.name}, {self.description}>'.format(self=self)