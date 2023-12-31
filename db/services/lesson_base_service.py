from db.dao.Lessons_baseDAO import LessonsBaseDAO

class LessonsBaseService:
    def __init__(self, dao: LessonsBaseDAO):
        self.dao = dao

    def create(self, data, day_id, message):
        self.dao.create(data, day_id, message)

    def get_all_lessons_for_one_user(self, user_id):
        return self.dao.get_all_lessons_for_one_user(user_id)

    def get_last_users_sign_up(self, user_id):
        return self.dao.get_last_users_sign_up(user_id)



    # def get_all_intervals(self):
    #     return self.dao.get_all()