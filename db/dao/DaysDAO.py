from db.dao.models import Days, Intervals
from db.utils import generate_week, generate_hour_intervals

class WeekdayDAO:
    def __init__(self, session):
        self.session = session

    def create_all(self):
        data = generate_week()
        intervals = [Intervals(lesson_time=j) for j in generate_hour_intervals(8, 16)]
        for i in data:
            for n, d in i.items():
                day = Days(lesson_date=d, day_name=n)
                day.intervals.extend(intervals)
                self.session.add(day)
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Days).filter(Days.is_works==False).all()
        return data
