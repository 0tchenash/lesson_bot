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

DAY1 = KeyboardButton('day_1')
DAY2 = KeyboardButton('day_2')
DAY3 = KeyboardButton('day_3')
DAY4 = KeyboardButton('day_4')
DAY5 = KeyboardButton('day_5')

TIME_INTERVAL1 = KeyboardButton('time_interval1',
                                callback_data='time_interval_1')
TIME_INTERVAL2 = KeyboardButton('time_interval2',
                                callback_data='time_interval_2')
TIME_INTERVAL3 = KeyboardButton('time_interval3',
                                callback_data='time_interval_3')
TIME_INTERVAL4 = KeyboardButton('time_interval4',
                                callback_data='time_interval_4')
TIME_INTERVAL5 = KeyboardButton('time_interval5',
                                callback_data='time_interval_5')
TIME_INTERVAL6 = KeyboardButton('time_interval6',
                                callback_data='time_interval_6')


START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
FORMAT = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_SINGLE_LESSON)
GROUP = InlineKeyboardMarkup(row_width=1).add(
    BTN_SINGLE_LESSON, BTN_CHOOSED_GL)
SINGLE = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_CHOOSED_SL)


DAYS = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True).add(
    DAY1, DAY2, DAY3, DAY4, DAY5)
INTERVALS = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True).add(
    TIME_INTERVAL1, TIME_INTERVAL2, TIME_INTERVAL3, TIME_INTERVAL4,
    TIME_INTERVAL5, TIME_INTERVAL6)
