from sqlalchemy import Column, Integer, String, DECIMAL
from db.dao.models import Base


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    price = Column(DECIMAL)