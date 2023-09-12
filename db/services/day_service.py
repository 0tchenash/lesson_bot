from db.dao.DaysIntervalsDAO import DaysIntervalsDAO

class DayService:
    def __init__(self, dao: DaysIntervalsDAO):
        self.dao = dao

    def create_all(self ):
        self.dao.create_all()

    def get_all_days(self):
        return self.dao.get_all_days()

    def take_time(self, data, day_id):
        self.dao.take_time(data, day_id)

    def get_all_intervals(self, data):
        return self.dao.get_all_intervals(data)

    def take_time_period(self, data):
        self.dao.take_time_period(data)

    def get_similar_days(self, data):
        return self.dao.get_similar_days(data)
