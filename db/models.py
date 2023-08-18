
from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base, DeclarativeBase
from sqlalchemy import create_engine

Base: DeclarativeBase = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    phone_number = Column(String)

    
class Lessons_base(Base):
    __tablename__ = 'lessons_base'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(Date)
    total_price = Column(DECIMAL)
    user_id = Column(Integer, ForeignKey('user.id'))
    lesson_id = Column(Integer, ForeignKey('lesson.id'))
    user = relationship("User", foreign_keys=id)
    lesson = relationship("Lesson", foreign_keys=id)

class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    price = Column(DECIMAL)

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/postgres')

Base.metadata.create_all(engine)
