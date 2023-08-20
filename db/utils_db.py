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

print(result)