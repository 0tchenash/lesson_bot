from sqlalchemy import Column, Integer, String, Boolean
from db.setup_db import Base

class Days(Base):
    __tablename__ = "day"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_date = Column(String)
    day_name = Column(String)
    is_works = Column(Boolean, default=False)
