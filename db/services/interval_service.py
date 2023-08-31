from db.dao.IntervalDAO import IntervalDAO

class IntervalService:
    def __init__(self, dao: IntervalDAO):
        self.dao = dao

    def create_all_intervals(self):
        self.dao.create_all()

    def get_all_intervals(self):
        return self.dao.get_all()
