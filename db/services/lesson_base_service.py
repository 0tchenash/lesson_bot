from db.dao.Lessons_baseDAO import Lessons_baseDAO

class Lessons_baseService:
    def __init__(self, dao: Lessons_baseDAO):
        self.dao = dao

    def create(self, data, message):
        self.dao.create(data, message)



    # def get_all_intervals(self):
    #     return self.dao.get_all()