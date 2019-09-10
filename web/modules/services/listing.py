from modules.db import db_session
from modules.models.listing import ListingModel
from modules.models.order import OrderModel


class ListingService():

    def get_all(self, rank_best=False):
        q = db_session.query(ListingModel)
        if rank_best:
            q = self.rank_by_best(q)
        res = q.all()
        return res


    def get_all_by_event_id(self, event_id, rank_best=False):
        q = db_session\
            .query(ListingModel)\
            .filter(ListingModel.event_id == event_id)
        if rank_best:
            q = self.rank_by_best(q)
        res = q.all()
        return res


    def get_one_by_listing_id(self, listing_id):
        q = db_session\
            .query(ListingModel)\
            .filter(ListingModel.listing_id == listing_id)
        res = q.first()
        return res


    def rank_by_best(self, q):
        """This module determines 'best' to be defined as lowest price per ticket"""
        q = q.order_by(ListingModel.price.asc())
        return q


    def create_listing(self, body):
        new_listing = ListingModel(**body)
        db_session.add(new_listing)
        db_session.commit()


    def transact_sale(self, body):
        # Maybe there should be a transaction service?

        # Get POST request body
        listing_id = body['listing_id']
        requested_qty = body['requested_qty']
        buyer_user_id = body['user_id']

        # Get listing
        listing = db_session\
            .query(ListingModel)\
            .filter(ListingModel.listing_id == listing_id)\
            .first()

        # Validate listing currently has quantity to satisfy requested amount,
        # and if so, update the listing to reflect updated quantity
        remaining_qty = listing.current_qty - requested_qty
        if remaining_qty < 0:
            raise Exception('ERROR Not enough quantity to satisfy order!')
        listing.current_qty = remaining_qty
        
        # Create a new order
        new_order = OrderModel(
            order_id=None,
            order_qty=requested_qty,
            original_price=listing.price,
            final_price=listing.price,
            listing_id=listing.listing_id,
            user_id=buyer_user_id)
        db_session.add(new_order)

        # Commit transaction
        db_session.commit()
