from db.dao.DaysDAO import WeekdayDAO

class DayService:
    def __init__(self, dao: WeekdayDAO):
        self.dao = dao

    def create_all_weekdays(self ):
        self.dao.create_all()

    def get_all_weekdays(self):
        return self.dao.get_all()
