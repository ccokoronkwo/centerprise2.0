from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from wtforms.fields import PasswordField
from .models import *
from .models.user import User
from .models.user_image import UserImage
from .models.role import Role

from flask_security import current_user

# https://github.com/sasaporta/flask-security-admin-example/blob/master/main.py

# Customized User model for SQL-Admin
class UserAdmin(ModelView):
    #Prevent password from displaying on list of users
    column_exclude_list = ('password',)

    #Prevent standard password field from displaying whent craeating or editing a User
    form_excluded_columns = ('password',)

    # Prevent administration of Users unless the currently logged-in user has the "admin" role
    def is_accessible(self):
        return current_user.has_role('admin')

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = PasswordField('New Password')
        return form_class

    def on_model_change(self,form,model,is_created):
        #if password not blank
        if len(model.password2):
            model.password = utils.encrypt_password(model.password2)
            
class MyFileAdmin(FileAdmin):
    # Prevent administration of Roles unless the currently logged-in user has the "admin" role
    def is_accessible(self):
        return current_user.has_role('admin')

class _Admin(Admin, UserAdmin):
    def add_model_view(self, model):
        self.add_view(UserAdmin(model, db.session))

    def add_model_views(self, models):
        for model in models:
            self.add_model_view(model)

def create_security_admin(app, path):
    admin = _Admin(app, name='Centerprise 2.0', template_mode='bootstrap3')
    admin.add_model_views([User, Role, UserImage])
    admin.add_view(MyFileAdmin(path, '/static/', name='Static Files'))