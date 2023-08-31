from db.dao.models.days import Days
from db.utils import generate_week

class WeekdayDAO:
    def __init__(self, session):
        self.session = session

    def create_all(self):
        data = generate_week()
        for i in data:
            for n, d in i.items():
                week = Days(lesson_date=d, day_name=n)
            self.session.add(week)
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Days).all()
        return data
