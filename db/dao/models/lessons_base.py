from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from db.dao.models import Base


class Lessons_base(Base):
    """Модель таблицы базы с занятиями"""
    __tablename__ = 'lessons_base'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String)
    total_price = Column(DECIMAL)
    user_id = Column(Integer, ForeignKey('user.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user = relationship("User", foreign_keys=user_id)
    lesson = relationship("Lesson", foreign_keys=lesson_id)