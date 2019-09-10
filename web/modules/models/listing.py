from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from modules.db import DeclarativeBase
from modules.models.event import EventModel
from modules.models.user import UserModel

class ListingModel(DeclarativeBase):
    __tablename__ = 'listings'
    listing_id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float, nullable=False)
    original_qty = Column(Integer, nullable=False)
    current_qty = Column(Integer, nullable=False)
    section = Column(String, nullable=False)
    row = Column(String, nullable=False)
    event_id = Column(Integer, ForeignKey(EventModel.event_id), nullable=False)
    user_id = Column(Integer, ForeignKey(UserModel.user_id), nullable=False)
