from db.dao.models import Days, Intervals, DaysIntervals
from db.utils import generate_hour_intervals, get_dates_of_current_month

class DaysIntervalsDAO:
    def __init__(self, session):
        self.session = session

    def create_all(self):
        """Создание экземпляров класса интервал и день с последующим занесением в таблицы"""
        data = get_dates_of_current_month()
        interval = [Intervals(lesson_time=j) for j in generate_hour_intervals(8, 16)]
        self.session.add_all(interval)
        self.session.commit()
        for i in data:
            for n, d in i.items():
                day = Days(lesson_date=d, day_name=n)
                day.intervals.extend(interval)
                self.session.add(day)
        self.session.commit()
        self.session.close()

    def get_one_day(self, day_id):
        day = self.session.query(Days).filter(Days.id==int(day_id)).first()
        return day

    def get_similar_days(self, data):
        days = self.session.query(Days).filter(Days.day_name==data['lesson_day']).all()
        return days

    def get_one_interval(self, data):
        time = self.session.query(Intervals).filter(Intervals.lesson_time==data['lesson_time']).first()
        return time

    def get_all_days(self):
        """Получение записей из таблицы"""
        data = self.session.query(Days).filter(Days.is_works==False).filter(Days.day_name!="Sunday").all()
        return data

    def get_all_intervals(self, data):
        day = self.session.query(Days).filter(Days.day_name==data['lesson_day']).first()
        intervals = self.session.query(Intervals.lesson_time).join(DaysIntervals, Intervals.id == DaysIntervals.interval_id).join(Days, Days.id == DaysIntervals.day_id).filter(Days.id==day.id).filter(DaysIntervals.is_works==False).all()
        return intervals

    def take_time(self, data, day_id):
        """При выборе данного интервала пользователем происходит изменение параметра is_works,
            указанный промежуток перестает быть доступным"""
        day = self.get_one_day(day_id)
        time = self.get_one_interval(data)
        date = self.session.query(DaysIntervals).filter(DaysIntervals.day_id==day.id).filter(DaysIntervals.interval_id==time.id).first()
        date.is_works = True
        self.session.add(date)
        self.session.commit()
        self.session.close()


    def take_time_period(self, data):
        days = self.get_similar_days(data)
        for i in days:
            self.take_time(data, i.id)
