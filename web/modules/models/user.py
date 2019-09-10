from sqlalchemy import Column, Integer, String, Boolean
from modules.db import DeclarativeBase


class UserModel(DeclarativeBase):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email_address = Column(String, nullable=False)
