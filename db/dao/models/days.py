from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.dao.models import Base

class Days(Base):
    """Модель таблицы дней"""
    __tablename__ = "day"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_date = Column(String)
    day_name = Column(String)
    is_works = Column(Boolean, default=False)
    intervals = relationship("Intervals", secondary="day_interval")
