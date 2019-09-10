from modules.db import db_session
from modules.models.order import OrderModel


class OrderService():

    def get_all(self):
        res = db_session\
            .query(OrderModel)\
            .all()
        return res


    def get_all_by_listing_id(self, listing_id):
        res = db_session\
            .query(OrderModel)\
            .filter(OrderModel.listing_id == listing_id)\
            .all()
        return res


    def get_one_by_order_id(self, order_id):
        res = db_session\
            .query(OrderModel)\
            .filter(OrderModel.order_id == order_id)\
            .first()
        return res
