from db.dao.DaysIntervalsDAO import DaysIntervalsDAO
from db.dao.LessonsDAO import LessonDAO
from db.dao.UsersDAO import UserDAO
from db.dao.Lessons_baseDAO import LessonsBaseDAO

from db.services.day_interval_service import DaysIntervalsService
from db.services.lesson_service import LessonService
from db.services.user_service import UserService
from db.services.lesson_base_service import LessonsBaseService
from db.schemas.days_intervals import DaysIntervalsSchema, IntervalsSchema, DaysSchema
from db.schemas.lessons_base import ScheduleSchema
from db.schemas.lessons import LessonSchema
from db.schemas.users import UserSchema

from db.setup_db import session

week_dao = DaysIntervalsDAO(session=session)
week_services = DaysIntervalsService(dao=week_dao)
week_schemas = DaysIntervalsSchema(many=True)
days_schemas = DaysSchema(many=True)
intervals_schemas = IntervalsSchema(many=True)

lesson_dao = LessonDAO(session=session)
lesson_services = LessonService(dao=lesson_dao)
lesson_schemas = LessonSchema(many=True)

user_dao = UserDAO(session=session)
user_services = UserService(dao=user_dao)
user_schemas = UserSchema(many=True)

lesson_base_dao = LessonsBaseDAO(session=session)
lesson_base_services = LessonsBaseService(dao=lesson_base_dao)
schedule_schemas = ScheduleSchema(many=True)
