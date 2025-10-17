#Задание 0
"""
#вызов модуля
import csv

#данные
data = [
	['Имя', 'Возраст', 'Город'],
	['Анна', '25', 'Москва'],
	['Петр', '30', 'Санкт-Петербург'],
	['Мария', '28', 'Киев']
]

#открываем файл для записи
with open('new_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
	#корректный перенос строк, отображение кириллицы
	writer = csv.writer(csvfile)
	writer.writerows(data)#запись данных
	
with open('new_data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)
		#вывод каждой строки

with open('new_data.csv') as f:
		reader = csv.reader(f)
		print(list(reader))
		#список списков
"""
#Задание 0.1

#вызов модуля

import csv

#данные пишем уже не списком списков, а списком словарей
data = [
	{'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
	{'Имя': 'Петр', 'Возраст': '30','Город': 'Санкт-Петербург'},
	{'Имя': 'Мария','Возраст': '28','Город': 'Киев'}
]

#записываем данные в csv посредством словаря

with open('данные_с_заголовками.csv', 'w', newline='', encoding='utf-8') as csvfile:
		fieldnames = ['Имя', 'Возраст', 'Город']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		writer.writeheader()#запись заголовка
		writer.writerows(data)#данные

#чтение данных
with open('данные_с_заголовками.csv', 'r', encoding='utf-8') as csvfile:
	#'r' подразумевается по умолчанию, но я решил, что раз учимся, напишу по алгоритму, ошибкой это не является, encoding как перестраховка для кроссплатформенности, мало ли...
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['Имя'], row['Возраст'], row['Город'])