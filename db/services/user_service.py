from db.dao.UsersDAO import UserDAO

class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, message):
        self.dao.create(message)

    def update(self, message):
        self.dao.update(message)

    def delete(self, message):
        self.dao.delete(message)

    def get_one(self, message):
        return self.dao.get_one(message)
