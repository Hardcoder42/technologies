
#EX 1(Counter)
from collections import Counter

#генерируем случайный список чисел
import random
r_numbers  = [random.randint(1,10)for _ in range(10)]
print(f"Числа: {r_numbers}")

#подсчет уникальных с помощью Counter
counter = Counter(r_numbers)
print(f"Уникальных чисел: {len(counter)}")

#3 наиболее частых, вывод их вхождений
for num, count in counter.most_common(3):
    print(f"Число {num}: {count} вхождений")

#EX 2(namedtuple)
from collections import namedtuple

#создаем именованный кортеж
Book = namedtuple('Book', ['title', 'author', 'genre'])

#создаем несколько экземпляров
book1 = Book('3 мушкетера', 'А. Дюма', 'Приключения')
book2 = Book('Отверженные','А. Дюма','Приключения')
book3 = Book('Человек, который смеётся','А. Дюма','Приключения')

#выводим инфу по атрибутам
print(book1.author)
print(book2.genre)
print(book3.title)

#EX 3(defaultdict)
from collections import defaultdict

#создаем defaultdict с типом данных list
dd = defaultdict(list)
print(f"Тип dd: {type(dd)}")
print(f"Значение dd: {dd}")

#добавляем несколько элементов, используя k and v
dd['fruits'].append('apple')
dd['fruits'].append('grape')
dd['vegetables'].append('potato')
dd['animals'].append('tiger')
dd['animals'].append('elephant')

#выводим содержимое, где значения-списки элементов с одинаковыми ключами
for key,value_list in dd.items():
    print(f"{key}: {value_list}")

#EX 4(deque)
from collections import deque

#создаем deque, добавляем в неё элементы
dq = deque([1,2,3,4,5])
print(f"Исходная очередь: {dq}")

#используем методы append, appendleft, pop, popleft для добавления и удаления элементов
#проверка как меняется deque после каждой манипуляции
dq.pop()
print(f"Pop: {dq}")
dq.popleft()
print(f"Popleft: {dq}")
dq.append(8)
print(f"Append: {dq}")
dq.appendleft(9)
print(f"Appendleft: {dq}")

# EX 5(deque простая очередь)
from collections import deque


# функция для добавления и извлечения элементов
def create_deque():
    """создает и возвращает пустую двустороннюю очередь"""
    return deque()


def add_element(dq, element, side='right'):
    """добавляет элемент слева и справа в очередь"""
    if side == 'right':
        dq.append(element)
    elif side == 'left':
        dq.appendleft(element)
    else:
        raise ValueError("side должен быть 'left' или 'right'")
    return dq


def del_element(dq, side='right'):
    """извлекает элемент слева и справа из очереди"""
    if not dq:
        return None, dq  # проверка на пустоты

    if side == 'right':
        element = dq.pop()  # сохраняем результат
    elif side == 'left':
        element = dq.popleft()  # сохраняем результат
    else:
        raise ValueError("side должен быть 'left' или 'right'")
    return element, dq  # возвращаем элемент и очередь


# создаем пустой deque
dq = create_deque()
print(f"Создана deque: {dq}")

# используем написанные функции
dq = add_element(dq, 2, 'right')
print(f"Добавлен элемент: {dq}")
dq = add_element(dq, 4, 'left')
print(f"Добавлен элемент: {dq}")
dq = add_element(dq, 6, 'right')
print(f"Добавлен элемент: {dq}")
dq = add_element(dq, 9, 'left')
print(f"Добавлен элемент: {dq}")
element, dq = del_element(dq, 'left')
print(f"Извлечен элемент: {element}, остаток: {dq}")
element, dq = del_element(dq, 'right')
print(f"Извлечен элемент: {element}, остаток: {dq}")
