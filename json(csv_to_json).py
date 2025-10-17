import csv
import json

def csv_to_json(csvfile, jsonfile, delimiter=',', indent=4):
	"""Конвертер файлов CSV в формат JSON
	
	args:
		csvfile - название CSV файла
		jsonfile - имя JSON файла
		delimiter - разделитель значений
		indent - отступ
		
	returns:
		Преобразованный файл формата JSON без потерь данных исходного файла
	
	"""
	data = []
	
	with open(csvfile, 'r', encoding='utf-8') as infile:
		reader = csv.DictReader(infile, delimiter=delimiter)
		for row in reader:
			#выводим данные для проверки
			print(row['Имя'], row['Возраст'], row['Город'])
			#добавляем строку в список данных
			data.append(row)
	
	with open(jsonfile, 'w', encoding='utf-8') as outfile:
		json.dump(data, outfile, ensure_ascii=False, indent=indent)
	
	print(f"Файл успешно преобразован в {jsonfile}")

#using
csv_to_json('данные_с_заголовками.csv', 'new_data.json')
#согласно задания параметры разделителя значений и отступ выставлен, что касается разделителя строк, он по умолчанию при чтении отображается с новой строки, при записи можно использовать newline=''. 