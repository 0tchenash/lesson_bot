from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


BTN_ADD_USER_DATA = InlineKeyboardButton('Записаться!',
                                         callback_data='add_user_data')
BTN_CHOOSE_LESSON = InlineKeyboardButton('Дальше',
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
BTN_TAKE_TIME_PERIOD = InlineKeyboardButton('Take time period!',
                                         callback_data='take_time_period')


def get_kb_days(data):
    btn_lst = [InlineKeyboardButton(i['day_name'][0:3], callback_data=f"{i['day_name']} {i['id']} choosed_day_for_lesson") for i in data]
    kb = InlineKeyboardMarkup(row_width=5, resize_keyboard=True).add(*btn_lst)
    return kb

def get_kb_intervals(data):
    btn_lst = [InlineKeyboardButton(i['lesson_time'], callback_data=f"{i['lesson_time']} choosed_interval_for_lesson") for i in data]
    kb = InlineKeyboardMarkup(row_width=5, resize_keyboard=True).add(*btn_lst)
    return kb


START = InlineKeyboardMarkup().add(BTN_ADD_USER_DATA)
CHOOSE = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
FORMAT = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_SINGLE_LESSON)
GROUP = InlineKeyboardMarkup(row_width=1).add(
    BTN_SINGLE_LESSON, BTN_CHOOSED_GL)
SINGLE = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_CHOOSED_SL)
TAKE_TIME = InlineKeyboardMarkup(row_width=1).add(
    BTN_TAKE_TIME_PERIOD)

GET_PHONE = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Поделиться контактом', request_contact=True))
