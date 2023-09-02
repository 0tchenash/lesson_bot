import datetime

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

def make_client():
    client={}
    return client
