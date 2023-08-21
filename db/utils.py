from core.implemented import week_services

def days_list(data):
    lst = [f'{d}-{n[:3]}' for d, n in data]
    return lst