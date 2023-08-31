from core.implemented import week_services, interval_services

def get_data_week():
    return week_services.get_all_weekdays()

def get_intervals():
    return interval_services.get_all_intervals()

