from flask_via.routers.default import Pluggable
from app.invoice.views import MainView

#The class objects defined in views are mapped to app urls using Pluggable
routes = [
    Pluggable('/invoice/', MainView, 'index')
]