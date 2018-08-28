from flask_via.routers.default import Pluggable
from app.restaurant.views import *

routes = [
    Pluggable('/restaurant/', ProfileView, 'profile'),
    Pluggable('/restaurant/upload', RestaurantUploadView, 'upload')
]