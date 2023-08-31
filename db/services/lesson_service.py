from db.dao.LessonsDAO import LessonDAO

class LessonService:
    def __init__(self, dao: LessonDAO):
        self.dao = dao

    def create_all_lessons(self):
        self.dao.create_all()

    def get_all_lessons(self):
        return self.dao.get_all()
