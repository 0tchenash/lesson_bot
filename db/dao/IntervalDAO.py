from db.dao.models import Intervals
from db.utils import generate_hour_intervals

class IntervalDAO:
    def __init__(self, session):
        self.session = session

    def create_all(self):
        data = generate_hour_intervals(8, 1)
        for i in data:
            interval = Intervals(lesson_time=str(i))
            self.session.add(interval)
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Intervals).all()
        return data

    # def update(self, data):
    #     interval = self.session.query(Intervals).filter(Intervals.lesson_time==data.split()[0]).first()
    #     interval.is_works = True
    #     self.session.add(interval)
    #     self.session.commit()
    #     self.session.close()
