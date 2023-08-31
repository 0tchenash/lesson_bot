from db.dao.models.users import User

class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, message, contact):
        user_name = message.from_user.username if message.from_user.username else None
        name = message.from_user.full_name if message.from_user.full_name else None
        user_id = message.from_user.id
        user = User(user_name=user_name, name=name, phone_number=str(contact), user_telegram_id=int(user_id))
        self.session.add(user)
        self.session.commit()
        self.session.close()

