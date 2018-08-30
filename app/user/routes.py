from flask_via.routers.default import Pluggable
from app.user.views import *

#The class objects defined in views are mapped to app urls using Pluggable
routes = [
    Pluggable('/user/', ProfileView, 'profile'),
    Pluggable('/user/upload', UserUploadView, 'upload'),

    Pluggable('/authorize/<provider>', OauthAuthorize, 'oauth_authorize'),
    Pluggable('/callback/<provider>', OauthCallback, 'oauth_callback')

]