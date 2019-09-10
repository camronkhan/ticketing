import json
from flask import jsonify, request
from flask_restplus import Resource, Namespace, fields
from modules.services.listing import ListingService
from modules.services.sale import SaleService


ns = Namespace('sales')

sale_model = ns.model('Sale', {
    'listing_id': fields.Integer,
    'requested_qty': fields.Integer,
    'user_id': fields.Integer
})


@ns.route('/')
class Sales(Resource):

    @ns.expect(sale_model)
    @ns.response(400, 'Validation error')
    def post(self):
        """Transact a sale"""
        body = request.json
        svc = ListingService()
        return svc.transact_sale(body)
