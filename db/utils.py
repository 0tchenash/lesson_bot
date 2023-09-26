import datetime
from aiogram.dispatcher.filters.state import StatesGroup, State

def get_dates_of_current_month():
    today = datetime.date.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = today.replace(day=1, month=today.month % 12 + 1) - datetime.timedelta(days=1)

    dates = []
    current_date = first_day_of_month
    while current_date <= last_day_of_month:
        formatted_date = {current_date.strftime("%A"):f"{current_date:%Y-%m-%d}"}
        dates.append(formatted_date)
        current_date += datetime.timedelta(days=1)

    return dates

def generate_hour_intervals(start_hour, end_hour):
    hour_intervals = []
    for hour in range(start_hour, end_hour):
        interval = f"{hour}-{hour+1}"
        hour_intervals.append(interval)
    return hour_intervals

def serialize(data):
    dic_ = {'lesson_type': data.type,
            'lesson_day': data.day_name,
            'day_id': data.id,
            'lesson_time': data.lesson_time}
    return dic_

class LessonBaseState(StatesGroup):
    lesson_type = State()
    lesson_day = State()
    day_id = State()
    lesson_time = State()