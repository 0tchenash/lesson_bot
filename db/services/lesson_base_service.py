from db.dao.Lessons_baseDAO import LessonsBaseDAO

class LessonsBaseService:
    def __init__(self, dao: LessonsBaseDAO):
        self.dao = dao

    def create(self, data, day_id, message):
        self.dao.create(data, day_id, message)



    # def get_all_intervals(self):
    #     return self.dao.get_all()