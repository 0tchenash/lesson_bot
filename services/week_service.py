from db.utils_db import WeekdayDAO
class WeekService:
    def __init__(self, dao: WeekdayDAO):
        self.dao = dao

    def sorted_data_week(self, ):
        self.dao.create()

    def get_all_weekday(self):
        return self.dao.get_all()
