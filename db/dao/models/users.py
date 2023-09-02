from sqlalchemy import Column, Integer, String, Boolean
from db.dao.models import Base


class User(Base):
    """Модель таблицы пользователя"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    name = Column(String)
    phone_number = Column(String)
    user_telegram_id = Column(Integer)
    admin = Column(Boolean, default=False)
