from core.implemented import week_services

def get_data_week():
    return week_services.get_all_days()

def get_intervals(data):
    return week_services.get_all_intervals(data)
