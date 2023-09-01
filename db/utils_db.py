from datetime import datetime, timedelta
from .models import Days, Intervals
import calendar


def generate_week():
    # Начальная дата
    start_date = datetime.today()

    # Количество дней в массиве
    num_days = 7

    # Создание массива дней недели
    days_of_week = [start_date + timedelta(days=i) for i in range(1, num_days)]

    # Получение названий дней недели
    day_names = [calendar.day_name[day.weekday()] for day in days_of_week]

    # Создание словаря в формате {'DayName': 'YYYY-MM-DD'}
    day_dict = {day_name: day.strftime('%Y-%m-%d') for day, day_name in zip(days_of_week, day_names)}

    # Сортировка словаря по значениям (датам) в обратном порядке
    sorted_days = sorted(day_dict.items(), key=lambda x: x[1])

    # Преобразование в желаемый формат
    result = [{day_name: day_date} for day_name, day_date in sorted_days]

    return result

def generate_hour_intervals(start_hour, end_hour):
    hour_intervals = []
    for hour in range(start_hour, end_hour):
        interval = f"{hour}-{hour+1}"
        hour_intervals.append(interval)
    return hour_intervals

class WeekdayDAO:
    def __init__(self, session):
        self.session = session

    def create(self):
        data = generate_week()
        for i in data:
            for n, d in i.items():
                week = Days(lesson_date=d, day_name=n)
            self.session.add(week)
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Days).all()
        return data

class IntervalDAO:
    def __init__(self, session):
        self.session = session

    def create(self):
        data = generate_hour_intervals(8, 18)
        for i in data:
            interval = Intervals(lesson_time=str(i))
            self.session.add(interval)
        self.session.commit()
        self.session.close()

    def get_all(self):
        data = self.session.query(Intervals).all()
        return data
