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
        lesson = Lessons_base(total_price=lesson.price, lesson_id=lesson.id, user_id=user.id, time=date.id)
        # lessons_base_schema = DaysIntervalsSchema()
        self.session.add(lesson)
        self.session.commit()
        self.session.close()
