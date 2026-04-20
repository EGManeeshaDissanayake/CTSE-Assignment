from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class Registration(Base):
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, index=True)
    event_id = Column(Integer, index=True)
    registered_at = Column(DateTime, default=datetime.utcnow)