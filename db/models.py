from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base, DeclarativeBase


Base: DeclarativeBase = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    phone_number = Column(String)


class Lessons_base(Base):
    __tablename__ = 'lessons_base'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String)
    total_price = Column(DECIMAL)
    user_id = Column(Integer, ForeignKey('user.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user = relationship("User", foreign_keys=user_id)
    lesson = relationship("Lesson", foreign_keys=lesson_id)


class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    price = Column(DECIMAL)


class Days(Base):
    __tablename__ = "day"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_date = Column(String)
    day_name = Column(String)
    is_works = Column(Boolean, default=False)


class Intervals(Base):
    __tablename__ = "interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_time = Column(String)
    is_works = Column(Boolean)


class DaysIntervals(Base):
    __tablename__ = "day_interval"

    id = Column(Integer, primary_key=True, autoincrement=True)
    day_id = Column(Integer, ForeignKey('day.id'))
    interval_id = Column(Integer, ForeignKey('interval.id'))
