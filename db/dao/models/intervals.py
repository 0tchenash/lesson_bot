from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.dao.models import Base


class Intervals(Base):
    """Модель таблицы интервалов времени"""
    __tablename__ = "interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_time = Column(String)
    days = relationship("Days", secondary="day_interval")