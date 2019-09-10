from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from modules.db import DeclarativeBase
from modules.models.venue import VenueModel

class EventModel(DeclarativeBase):
    __tablename__ = 'events'
    event_id = Column(Integer, primary_key=True, autoincrement=True)
    event_name = Column(String, nullable=False)
    event_ts = Column(DateTime)
    venue_id = Column(Integer, ForeignKey(VenueModel.venue_id))
