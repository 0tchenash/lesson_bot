from db.dao.Lessons_baseDAO import LessonsBaseDAO

class LessonsBaseService:
    def __init__(self, dao: LessonsBaseDAO):
        self.dao = dao

    def create(self, data, message):
        self.dao.create(data, message)



    # def get_all_intervals(self):
    #     return self.dao.get_all()