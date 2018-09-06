from flask import request, url_for, redirect, render_template, flash, current_app
from flask.views import MethodView
from flask_security.utils import login_user
from flask_security import current_user
from flask_security.datastore import SQLAlchemyUserDatastore

from app.user.forms import UserImageForm
from app.user.oauth import OAuthSignIn

from ..models import FinalUser, FinalUserImage, Role, db
# from . import user_photo
# from .. import app

user_datastore = SQLAlchemyUserDatastore(db, FinalUser, Role)

class MainView(MethodView):
    def get(self):
        return render_template('invoices/index.html')
