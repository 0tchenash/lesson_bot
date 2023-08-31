from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


UPDATE_DATABASE = InlineKeyboardButton('Обновить',
                                         callback_data='update')
CHECK_TODAY_LESSON = InlineKeyboardButton('Расписание на сегодня',
                                         callback_data='check')
DELETE_LESSON = InlineKeyboardButton('Удалить',
                                         callback_data='delete')


ADMIN = InlineKeyboardMarkup(row_width=1).add(
    UPDATE_DATABASE, CHECK_TODAY_LESSON, DELETE_LESSON)