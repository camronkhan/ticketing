from flask import Blueprint
from flask_restplus import Api
from modules.apis.v1.listings import ns as listings_ns
from modules.apis.v1.sales import ns as sales_ns
from modules.apis.v1.orders import ns as orders_ns


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='Ticketing API', version='1.0')

api.add_namespace(listings_ns)
api.add_namespace(sales_ns)
api.add_namespace(orders_ns)