import datetime
import calendar

# 1 ЧАСТЬ

# текущая дата и время
now = datetime.datetime.now()
print("Текущая дата и время: ", now)

# вывести день недели
ru_week = {
	'Monday': 'Понедельник',
	'Tuesday': 'Вторник',
	'Wednesday': 'Среда',
	'Thursday': 'Четверг',
	'Friday': 'Пятница',
	'Saturday': 'Суббота',
	'Sunday': 'Воскресенье'
} # переведем дни недели на рузге
eng_day = now.strftime("%A")
ru_day = ru_week.get(eng_day, eng_day) # 1 случай ищем в словаре, 2 случай вернуть англ, если не найдено
print("День недели: ", ru_day)

# вывести високосный ли год
try:
	is_leap = int(input("Введите год: "))
	if calendar.isleap(is_leap): # используем модуль calendar
		print(f"{is_leap} год високосный")
	else:
		print(f"{is_leap} год високосным не является...")
except ValueError:
	print(f"Введите год цифрами в формате ГГГГ")

# 2 ЧАСТЬ
# запрос ввода даты от пользователя(ГГГГММДД)
try:
	day = int(input("Введите день: "))
	month = int(input("Введите месяц: "))
	year = int(input("Введите год: "))
	print(f"Дата: {day:02d}.{month:02d}.{year}")

	# разница между текущей и введенной ранее датой (расчет и вывод ДДЧЧММ)
	request = datetime.datetime(year, month, day, 12, 0)
	difference = request - now

	# форматируем до минут
	d = difference.days
	h = difference.seconds // 3600#без остатка
	m = (difference.seconds % 3600) // 60

	print(f"Настоящее время: {now.strftime('%Y.%m.%d %H:%M')}")
	print(f"Запрашиваемая дата: {request.strftime('%Y.%m.%d %H:%M')}")

	#проверочка на актуальность запроса
	if difference.total_seconds() > 0:
		print(f"До запрашиваемой даты осталось: {d} дней {h} часов {m} минут")
	else:
		print(f"Запрашиваемая дата уже прошла...{abs(d)} дней {h} часов {m} минут назад")
except Exception as e:
	print(f"Ошибка: {e}")