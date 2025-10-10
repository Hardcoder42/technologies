import re
from collections import Counter

text = """Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.
"""

with open("mail.txt", "w", encoding = "utf-8") as f:
	f.write(text)

with open("mail.txt", "r", encoding = "utf-8") as f:
	mail_content = f.read()

def get_words(mail, filename="mail.txt"):
	"""
	Извлекает слова из текстового файла, выводит счетчик слов
	
	Args:
		mail: входной текст
	
	Returns: обьект со статистикой слов
	"""
	if not mail or not isinstance(mail, str):
		return Counter()
	
	#очистка и нормализация текста
	clean = re.sub(r'[^\w\s]', "", mail)#символы
	lower = clean.lower()#нижний регистр
	words = lower.split()#разделитель пробел
	
	#выводы
	print(f"Название файла: {filename}")
	print(f"Общее количество слов:  {len(words)}") #общее количество
	print(f"Уникальных вхождений:  {len(set(words))}")#уникальные слова
	
	return Counter(words)#возвращаем результат
	

result = get_words(mail_content)#список слов
#print(result)#по заданию не нужен
print("\nСтатистика: ")
for word, count in result.items():
	print(f"{word}: {count}")
