from db.dao.models import Lessons_base, User, DaysIntervals, Days, Intervals, Lesson
from db.schemas.days_intervals import DaysIntervalsSchema

class LessonsBaseDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, time_id):
        sign_up = self.session.query(Lessons_base).filter(Lessons_base.time==time_id)
        return sign_up

    def create(self, data, day_id, message):
        lesson = self.session.query(Lesson).filter(Lesson.type==data['lesson_type']).first()
        user = self.session.query(User).filter(User.user_telegram_id==message.from_user.id).first()
        time = self.session.query(Intervals).filter(Intervals.lesson_time==data['lesson_time']).first()
        date = self.session.query(DaysIntervals).filter(DaysIntervals.day_id==day_id).filter(DaysIntervals.interval_id==time.id).first()
        lesson = Lessons_base(lesson_id=lesson.id, user_id=user.id, time_id=date.id)
        # lessons_base_schema = DaysIntervalsSchema()
        self.session.add(lesson)
        self.session.commit()
        self.session.close()

    def get_all_lessons_for_one_user(self, user_id):
        user = self.session.query(User).filter(User.user_telegram_id==user_id).first()
        lessons = self.session.query(Lessons_base, DaysIntervals, Days.day_name, Intervals.lesson_time, Lesson.type, Lesson.price)\
            .join(DaysIntervals, Lessons_base.time_id == DaysIntervals.id)\
            .join(Days, DaysIntervals.day_id == Days.id)\
            .join(Intervals, DaysIntervals.interval_id == Intervals.id)\
            .join(Lesson, Lessons_base.lesson_id == Lesson.id)\
            .filter(Lessons_base.user_id == user.id).all()
        return lessons

    def get_last_users_sign_up(self, user_id):
        user = self.session.query(User).filter(User.user_telegram_id==user_id).first()
        data = self.session.query(Lessons_base, DaysIntervals, Days.day_name, Days.id, Intervals.lesson_time, Lesson.type, Lesson.price)\
            .join(DaysIntervals, Lessons_base.time_id == DaysIntervals.id)\
            .join(Days, DaysIntervals.day_id == Days.id)\
            .join(Intervals, DaysIntervals.interval_id == Intervals.id)\
            .join(Lesson, Lessons_base.lesson_id == Lesson.id)\
            .order_by(Lessons_base.id.desc()).filter(Lessons_base.user_id==user.id).first()
        return data