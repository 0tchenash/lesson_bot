from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from db.setup_db import Base

class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    price = Column(DECIMAL)