from db.dao.models import Lesson

class LessonDAO:
    def __init__(self, session):
        self.session = session

    def create_all(self):
        lesson_1 = Lesson(type="Групповое", price=800.0)
        lesson_2 = Lesson(type="Индивидуальное", price=1600.0)
        self.session.add_all([lesson_1, lesson_2])
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Lesson).all()
        return data