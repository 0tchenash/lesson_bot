from sqlalchemy.orm import DeclarativeBase, declarative_base

Base: DeclarativeBase = declarative_base()

from .days_intervals import DaysIntervals
from .days import Days
from .intervals import Intervals
from .lessons_base import Lessons_base
from .lessons import Lesson
from .users import User
