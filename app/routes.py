from flask_via.routers.default import Blueprint

#All the blueprints for the resources used by application is registered here
routes = [
	Blueprint('invoice', 'app.invoice', template_folder="templates"),
    Blueprint('cpuser', 'app.user', template_folder="templates"),
    Blueprint('restaurant', 'app.restaurant',  template_folder="templates"),
    Blueprint('food', 'app.food', template_folder="templates"),
]