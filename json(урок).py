import json

data = {
	'name': 'Ивашка',
	'age': 30,
	'is_student': False,
	'skills': ['Python', 'SQL']
}

#convert py to json
json_string = json.dumps(data)
print(json_string)#utf не хватает

#запись
with open('output.json', 'w', newline="", encoding='utf-8') as file:
	json.dump(data, file)

#чтение
with open('output.json', 'r') as file:
	json.load(file)
print(data['skills'])

#json to py
json_string1 = '{"name": "Ивашка", "age": 30, "is_student": false, "skills": ["Python", "SQL"]}'
data2 = json.loads(json_string1)
print(data2)