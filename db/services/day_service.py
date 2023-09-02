from db.dao.DaysIntervalsDAO import Days_intervalsDAO

class DayService:
    def __init__(self, dao: Days_intervalsDAO):
        self.dao = dao

    def create_all_weekdays(self ):
        self.dao.create_all()

    def get_all_weekdays(self):
        return self.dao.get_all()

    def take_time(self, data):
        self.dao.take_time(data)

    def get_all_intervals(self, data):
        return self.dao.get_all_intervals(data)
