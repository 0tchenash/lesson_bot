from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.setup_db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    name = Column(String)
    phone_number = Column(String)
    user_telegram_id = Column(Integer)
    admin = Column(Boolean, default=False)