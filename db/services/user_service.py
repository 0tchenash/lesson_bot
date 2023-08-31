from db.dao.UsersDAO import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self):
        self.dao.create()
