from sqlalchemy import Column, Integer, ForeignKey
from db.dao.models import Base

class DaysIntervals(Base):
    __tablename__ = "day_interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('day.id'))
    interval_id = Column(Integer, ForeignKey('interval.id'))