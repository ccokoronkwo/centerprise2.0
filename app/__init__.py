import sqlite3
import os.path
import sys
sys.path.append('..')
sys.path.append('.')
from flask import Flask, render_template, current_app
from flask_assets import Environment
from flask_wtf import CSRFProtect
from flask_security import Security, SQLAlchemyUserDatastore, utils
from flask_via import Via
from flask_uploads import configure_uploads

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

from .assets import create_assets
from .models import *
from .models.user import User
from .models.role import Role

from .user.forms import SecurityRegisterForm

from config import app_config

from .admin import create_security_admin

from flask_migrate import Migrate


def create_app(config_name):
    global user_datastore
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    csrf = CSRFProtect()
    csrf.init_app(app)

    assets = Environment(app)
    create_assets(assets)

    via = Via()
    via.init_app(app)

    # Ipload in several models - - - -

    from .user import user_photo
    #from .restaurant import restaurant_photo
    #from .food import food_photo

    
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    #configure_uploads(app, (restaurant_photo, food_photo, user_photo))
    configure_uploads(app, (user_photo))

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)

    security = Security(app, user_datastore, register_form=SecurityRegisterForm)

    create_security_admin(app=app, path=os.path.join(os.path.dirname(__file__)))
    
    with app.app_context():
        db.init_app(app)
        #Conditionally create admin/end_user
        db.create_all()
        user_datastore.find_or_create_role(name='admin', description='Administrator')
        user_datastore.find_or_create_role(name='end-user', description='End user')
        db.session.commit()

        # Create two Users for testing purposes -- unless they already exists.
        # In each case, use Flask-Security utility function to encrypt the password.
        encrypted_password = utils.encrypt_password('password')
        if not user_datastore.get_user('admin@centershealthcare.org'):
            user_datastore.create_user(email='admin@centershealthcare.org', password=encrypted_password)
        if not user_datastore.get_user('enduser@centershealthcare.com'):
            user_datastore.create_user(email='enduser@centershealthcare.org', password=encrypted_password)

        # Commit any database changes; the User and Roles must exist before we can add a Role to the User
        db.session.commit()

        # Give one User has the "end-user" role, while the other has the "admin" role. (This will have no effect if the
        # Users already have these Roles.) Again, commit any database changes.
        user_datastore.add_role_to_user('enduser@centershealthcare.org', 'end-user')
        user_datastore.add_role_to_user('admin@centershealthcare.org', 'admin')
        db.session.commit()

        migrate = Migrate(app,db)


    @app.route('/', methods=['GET'])
    @app.route('/home', methods=['GET'])    
    def index():
        return render_template('index.html')

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('error/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('error/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        db.session.rollback()
        return render_template('error/500.html', title='Server Error'), 500

    return app