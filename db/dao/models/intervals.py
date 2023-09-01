from sqlalchemy import Column, Integer, String, Boolean
from db.dao.models import Base


class Intervals(Base):
    __tablename__ = "interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_time = Column(String)
    is_works = Column(Boolean, default=False)