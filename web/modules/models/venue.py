from sqlalchemy import Column, Integer, String
from modules.db import DeclarativeBase


class VenueModel(DeclarativeBase):
    __tablename__ = 'venues'
    venue_id = Column(Integer, primary_key=True, autoincrement=True)
    venue_name = Column(String, nullable=False)
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    address_line_3 = Column(String)
    city = Column(String, nullable=False)
    county_region = Column(String)
    state_province = Column(String, nullable=False)
    zip_post_code = Column(String)
    country = Column(String, nullable=False)
