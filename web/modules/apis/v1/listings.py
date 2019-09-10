import json
from flask import jsonify, request
from flask_restplus import Resource, Namespace, fields
from modules.apis.util import model_result_set_to_json
from modules.services.listing import ListingService
from modules.services.sale import SaleService


ns = Namespace('listings')

listing_model = ns.model('Listing', {
    'listing_id': fields.Integer,
    'price': fields.Float,
    'original_qty': fields.Integer,
    'current_qty': fields.Integer,
    'section': fields.String,
    'row': fields.String,
    'event_id': fields.Integer,
    'user_id': fields.Integer
})

sale_model = ns.model('Sale', {
    'listing_id': fields.Integer,
    'requested_qty': fields.Integer,
    'user_id': fields.Integer
})


@ns.route('/')
class Listings(Resource):
    
    @ns.marshal_list_with(listing_model)
    def get(self):
        """Get all listings"""
        svc = ListingService()
        return svc.get_all()

    
    @ns.expect(listing_model)
    @ns.marshal_with(listing_model, code=201, description='Listing created')
    @ns.response(400, 'Validation error')
    def post(self):
        """Create a new listing"""
        body = request.json
        svc = ListingService()
        return svc.create_listing(body)


@ns.route('/events/<string:event_id>')
class ListingsByEvent(Resource):

    @ns.marshal_list_with(listing_model)
    def get(self, event_id):
        """Get all listings by event"""
        svc = ListingService()
        return svc.get_all_by_event_id(int(event_id))


@ns.route('/<string:listing_id>')
class Listing(Resource):

    @ns.marshal_with(listing_model)
    def get(self, listing_id):
        """Get a single listing"""
        svc = ListingService()
        return svc.get_one_by_listing_id(int(listing_id))


#
# Using query parameters would be a better choice here, but I don't want to
# flask-restplus's built-in reqparser as it's deprecated, and I don't want to
# put in the effort to integrating marshmallow at this time.
#

@ns.route('/best')
class BestListings(Resource):
    
    @ns.marshal_list_with(listing_model)
    def get(self):
        """Get all listings ranked by 'best' (in this case, lowest price)"""
        svc = ListingService()
        return svc.get_all(rank_best=True)


@ns.route('/best/events/<string:event_id>')
class BestListingsByEvent(Resource):

    @ns.marshal_list_with(listing_model)
    def get(self, event_id):
        """Get all listings by event ranked by 'best' (in this case, lowest price)"""
        svc = ListingService()
        return svc.get_all_by_event_id(int(event_id), rank_best=True)
