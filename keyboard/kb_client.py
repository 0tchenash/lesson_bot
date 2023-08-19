from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


BTN_CHOOSE_LESSON = InlineKeyboardButton('Записаться!',
                                         callback_data='choose_lesson')
BTN_GROUP_LESSON = InlineKeyboardButton('Записаться!',
                                         callback_data='group_lesson')
BTN_SINGLE_LESSON = InlineKeyboardButton('Записаться!',
                                         callback_data='single_lesson')
BTN_BACK = InlineKeyboardButton('Записаться!',
                                         callback_data='back')


START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
FORMAT = InlineKeyboardMarkup().add(BTN_GROUP_LESSON, BTN_SINGLE_LESSON)
START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
