from flask_via.routers.default import Pluggable
from app.invoices.views import *

#The class objects defined in views are mapped to app urls using Pluggable
routes = [
    Pluggable('/invoice/', MainView, 'index')
]