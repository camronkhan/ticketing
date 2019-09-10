from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from modules.db import DeclarativeBase
from modules.models.user import UserModel

class UserSessionModel(DeclarativeBase):
    __tablename__ = 'user_sessions'
    user_session_id = Column(Integer, primary_key=True, autoincrement=True)
    first_event_ts = Column(DateTime)
    last_event_ts = Column(DateTime)
    referral_code = Column(String)  # This can be further normalized
    user_id = Column(Integer, ForeignKey(UserModel.user_id), nullable=False)
