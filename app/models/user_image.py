from . import db

class UserImage(db.Model):
	__tablename__ = 'user_image'
	id = db.Column(db.Integer, primary_key=True)
	user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
	image_filename = db.Column(db.String, default=None, nullable=True)
	image_url = db.Column(db.String, default=None, nullable=True)
	user = db.relationship('User', back_populates='user_image')
	def __repr__(self):
		return '<UserImage: {self.user_id}, {self.image_filename}, {self.image_url}>'.format(self=self)