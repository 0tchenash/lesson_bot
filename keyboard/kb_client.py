from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


BTN_CHOOSE_LESSON = InlineKeyboardButton('Записаться!',
                                         callback_data='choose_lesson')
BTN_GROUP_LESSON = InlineKeyboardButton('Групповое занятие',
                                         callback_data='group_lesson')
BTN_SINGLE_LESSON = InlineKeyboardButton('Индивидуальное занятие',
                                         callback_data='single_lesson')
BTN_BACK = InlineKeyboardButton('Назад',
                                         callback_data='choose_lesson')
BTN_CHOOSED_GL = InlineKeyboardButton('Подходит!',
                                         callback_data='choosed_group_lesson')
BTN_CHOOSED_SL = InlineKeyboardButton('Подходит!',
                                         callback_data='choosed_single_lesson')

DAY1 = KeyboardButton('day1', callback_data='day_1')
DAY2 = KeyboardButton('day2', callback_data='day_2')
DAY3 = KeyboardButton('day3', callback_data='day_3')
DAY4 = KeyboardButton('day4', callback_data='day_4')
DAY5 = KeyboardButton('day5', callback_data='day_5')



START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
FORMAT = InlineKeyboardMarkup(row_width=1).add(BTN_GROUP_LESSON, BTN_SINGLE_LESSON)
GROUP = InlineKeyboardMarkup(row_width=1).add(BTN_SINGLE_LESSON,BTN_CHOOSED_GL, BTN_BACK)
SINGLE = InlineKeyboardMarkup(row_width=1).add(BTN_GROUP_LESSON,BTN_CHOOSED_SL, BTN_BACK)


DAYS = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True).add(DAY1, DAY2, DAY3, DAY4, DAY5)
