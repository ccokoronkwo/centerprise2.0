from flask_via.routers.default import Pluggable
from app.food.views import *

routes = [
    Pluggable('/food/', ProfileView, 'profile'),
    Pluggable('/food/upload', FoodUploadView, 'upload')
]