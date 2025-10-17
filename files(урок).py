"""
f = open("test.txt", "w")#название и запись
f.write("This is test stringi")#запись в файл
f.close#закрыть, иначе не сохр


f = open("test.txt", "r")#название и чтение
data = f.read()
print(data)
f.close#закрыть обязательно

f = open("test.txt", "w")#перезапись
f.write("This is another stringi")
f.close

f = open("test.txt", "r")#чтение
data = f.read()
print(data)
f.close

f = open("test.txt", "a")#дозапись
f.write("This is dich")
f.close

f = open("test.txt", "r")#чтение
data = f.read()
print(data)
f.close

f = open("test.txt", "w", encoding = "utf-8")#для корректного отображения русского текста
f.write("Hello, русский текст\n")
f.close()

f = open("test.txt")
print(f.read())
___
f = open("test.txt", "w", encoding = "utf-8")
sequence = ["Первая строка\n", "Вторая строка\n", "Третья строка\n"]
f.writelines(sequence)#записывает строки в файл
f.close()

f = open("test.txt", "r", encoding = "utf-8")
data = f.readlines()#считывание обратно в список
print(data)
f.close
___
f = open("numbers.txt", "w")
sequence = ["1\n","2\n","3\n","4\n","5\n","6\n","7\n","8\n","9\n"]
f.writelines(sequence)
f.close()

f = open("numbers.txt", "r")
data = f.readlines()#как улучшить?
print(data)
f.close()

#варианты преобразования в числа
#1
data = [int(i) for i in data]#вставляем после определения data
#2
data = list(map(int, f.readlines()))#замена той data
__
f = open("numbers.txt")#считывание по значению за раз
for line in f:
	print(line.strip())
	
f.close()
"""
with open("numbers.txt") as f:#with автоматически применяет f.close()
	for line in f:
		print(line.strip())