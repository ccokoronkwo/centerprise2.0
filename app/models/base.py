from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_security import UserMixin, RoleMixin
import datetime


#   https://pythonhosted.org/Flask-Security/quickstart.html
#   python manage.py db upgrade && python manage.py db revision --autogenerate


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__  = True
    id            = db.Column(db.Integer,  primary_key=True)
    date_created  = db.Column(db.TIMESTAMP, default=func.current_timestamp())
    date_modified = db.Column(db.TIMESTAMP, default=func.current_timestamp(), onupdate=func.current_timestamp())


roles_users = db.Table('roles_users',
        db.Column('final_user_id', db.Integer(), db.ForeignKey('final_user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

