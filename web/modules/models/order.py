from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from modules.db import DeclarativeBase
from modules.models.listing import ListingModel
from modules.models.user import UserModel


class OrderModel(DeclarativeBase):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_qty = Column(Integer, nullable=False)
    original_price = Column(Float, nullable=False)
    final_price = Column(Float, nullable=False)
    listing_id = Column(Integer, ForeignKey(ListingModel.listing_id), nullable=False)
    user_id = Column(Integer, ForeignKey(UserModel.user_id), nullable=False) # buyer
