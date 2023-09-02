from db.dao.models import User

class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, message):
        """Регистрация пользователя"""
        user_name = message.from_user.username if message.from_user.username else None
        name = message.from_user.full_name if message.from_user.full_name else None
        user_id = message.from_user.id
        user = User(user_name=user_name, name=name, user_telegram_id=int(user_id))
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def update(self, message):
        """Изменение записи пользователя"""
        user = self.session.query(User).filter(User.user_telegram_id==message.from_user.id).first()
        user.phone_number = str(message.contact.phone_number)
        self.session.add(user)
        self.session.commit()
        self.session.close()

    def delete(self, message):
        """Удаление пользователя"""
        user = self.session.query(User).filter(User.user_telegram_id==message.from_user.id).first()
        self.session.delete(user)
        self.session.commit()
        self.session.close()

    def get_one(self, message):
        user = self.session.query(User).filter(User.user_telegram_id==message.from_user.id).first()
        return user
