from db.utils_db import IntervalDAO
class IntervalService:
    def __init__(self, dao: IntervalDAO):
        self.dao = dao

    def create_intervals(self):
        self.dao.create()

    def get_all_intervals(self):
        return self.dao.get_all()
