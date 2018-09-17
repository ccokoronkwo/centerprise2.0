from . import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from .role import Role
from .user_image import UserImage
from .invoice import Invoice

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,  primary_key=True)
    date_created  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
    date_modified = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    
    #relationships:
    roles = db.relationship('Role', order_by=Role.id, secondary=roles_users, back_populates='user')
    user_image = db.relationship('UserImage', back_populates='user')
    invoices = db.relationship('Invoice', order_by=Invoice.id, back_populates='user')
    
    def __repr__(self):
        return '<User: {self.id}, {self.username}, {self.password}, {self.date_created}, {self.roles}, {self.invoices}>'.format(self=self)


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))