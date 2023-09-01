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


def get_kb_days(data):
    btn_lst = [InlineKeyboardButton(i['lesson_date'], callback_data="choosed_day_for_group_lesson") for i in data]
    kb = InlineKeyboardMarkup(row_width=5, resize_keyboard=True).add(*btn_lst)
    return kb

def get_kb_intervals(data):
    btn_lst = [InlineKeyboardButton(i['lesson_time'], callback_data="choosed_interval_for_group_lesson") for i in data]
    kb = InlineKeyboardMarkup(row_width=5, resize_keyboard=True).add(*btn_lst)
    return kb


START = InlineKeyboardMarkup().add(BTN_CHOOSE_LESSON)
FORMAT = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_SINGLE_LESSON)
GROUP = InlineKeyboardMarkup(row_width=1).add(
    BTN_SINGLE_LESSON, BTN_CHOOSED_GL)
SINGLE = InlineKeyboardMarkup(row_width=1).add(
    BTN_GROUP_LESSON, BTN_CHOOSED_SL)
