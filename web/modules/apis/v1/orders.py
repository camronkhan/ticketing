import json
from flask import jsonify, request
from flask_restplus import Resource, Namespace, fields
from modules.apis.util import model_result_set_to_json
from modules.services.order import OrderService


ns = Namespace('orders')

order_model = ns.model('Order', {
    'order_id': fields.Integer,
    'original_price': fields.Float,
    'final_price': fields.Float,
    'order_id': fields.Integer,
    'user_id': fields.Integer
})


@ns.route('/')
class Orders(Resource):
    
    @ns.marshal_list_with(order_model)
    def get(self):
        """Get all orders"""
        svc = OrderService()
        return svc.get_all()


@ns.route('/listings/<string:listing_id>')
class OrdersByListing(Resource):

    @ns.marshal_list_with(order_model)
    def get(self, listing_id):
        """Get all orders by listing"""
        svc = OrderService()
        return svc.get_all_by_listing_id(int(listing_id))


@ns.route('/<string:order_id>')
class Order(Resource):

    @ns.marshal_with(order_model)
    def get(self, order_id):
        """Get a single order"""
        svc = OrderService()
        return svc.get_one_by_order_id(int(order_id))
