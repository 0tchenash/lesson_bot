from db.dao.models import Lessons_base, User, DaysIntervals, Days, Intervals, Lesson

class Lessons_baseDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data, message):
        lesson = self.session.query(Lesson).filter(Lesson.type==data['lesson_type']).first()
        user = self.session.query(User).filter(User.user_telegram_id==message.from_user.id).first()
        day = self.session.query(Days).filter(Days.day_name==data['lesson_day']).first()
        time = self.session.query(Intervals).filter(Intervals.lesson_time==data['lesson_time']).first()
        date = self.session.query(DaysIntervals).filter(DaysIntervals.day_id==day.id).filter(DaysIntervals.interval_id==time.id).first()
        lesson = Lessons_base(total_price=lesson.price, lesson_id=lesson.id, user_id=user.id, time=date.id)
        self.session.add(lesson)
        self.session.commit()
        self.session.close()

