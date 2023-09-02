from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.dao.models import Base

class DaysIntervals(Base):
    """Модель таблицы связи дней и интервалов времени"""
    __tablename__ = "day_interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('day.id'))
    interval_id = Column(Integer, ForeignKey('interval.id'))
    is_works = Column(Boolean, default=False)
    day = relationship("Days", foreign_keys=day_id)
    interval = relationship("Intervals", foreign_keys=interval_id)