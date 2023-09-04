from db.dao.models import Days, Intervals, DaysIntervals
from db.utils import generate_hour_intervals, get_dates_of_current_month

class Days_intervalsDAO:
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


    def get_all(self):
        """Получение записей из таблицы день"""
        data = self.session.query(Days).filter(Days.is_works==False).filter(Days.day_name!="Sunday").all()
        return data

    def get_all_intervals(self, data):
        day = self.session.query(Days).filter(Days.day_name==data['lesson_day']).first()
        intervals = self.session.query(Intervals.lesson_time).join(DaysIntervals, Intervals.id == DaysIntervals.interval_id).join(Days, Days.id == DaysIntervals.day_id).filter(Days.id==day.id).filter(DaysIntervals.is_works==False).all()
        return intervals

    def take_time(self, data):
        """При выборе данного интервала пользователем происходит изменение параметра is_works,
            указанный промежуток перестает быть доступным"""
        day = self.session.query(Days).filter(Days.day_name==data['lesson_day']).first()
        time = self.session.query(Intervals).filter(Intervals.lesson_time==data['lesson_time']).first()
        date = self.session.query(DaysIntervals).filter(DaysIntervals.day_id==day.id).filter(DaysIntervals.interval_id==time.id).first()
        date.is_works = True
        self.session.add(date)
        self.session.commit()
        self.session.close()
