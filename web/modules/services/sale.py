from modules.db import db_session
from modules.models.listing import ListingModel
from modules.models.order import OrderModel


class SaleService():

    def transact_sale(self, body):

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
