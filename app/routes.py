from flask_via.routers.default import Blueprint

#All the blueprints for the resources used by application is registered here
routes = [
	Blueprint('invoices', 'app.invoices', template_folder="templates"),
    Blueprint('user', 'app.user', template_folder="templates"),
    Blueprint('restaurant', 'app.restaurant',  template_folder="templates"),
    Blueprint('food', 'app.food', template_folder="templates"),
]