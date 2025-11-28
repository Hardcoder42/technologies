import itertools

# Задача 1: Комбинации чисел из списка
# Дан список чисел [1, 2, 3, 4]. Cоздайте все возможные комбинации чисел длиной 2 и выведите их.
'''
itertools.combinations(iterable, r) #r=длина комбинации
Генерирует все возможные комбинации элементов из итерируемого объекта длины r.
'''
items = [1, 2, 3, 4]
for c in itertools.combinations(items, 2):
    print(c)

# Задача 2: Перебор перестановок букв в слове
# Для слова 'Python' найдите все возможные перестановки букв. Выведите каждую перестановку на отдельной строке.
'''
itertools.permutations(iterable, r=None) #r=перестановки определенной длины
Генерирует все возможные перестановки элементов из итерируемого объекта.
'''
word = ['p', 'y', 't', 'h', 'o', 'n']
for p in itertools.permutations(word):
    print(p)

# стало интересно, сколько перестановок на 6 символов
all_permutations = list(itertools.permutations(word))  # оформляем списком результат
count = len(all_permutations)  # подсчитываем результаты списка
print(f"Количество перестановок: {count}")

# Задача 3: Объединение списков в цикле
# Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. Объедините их в один список в цикле, повторяя этот цикл 5 раз.
'''
itertools.cycle(iterable)
Бесконечно повторяет элементы из итерируемого объекта.
'''
list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']
combined = list1 + list2 + list3  # всего 7 символов
result = list(itertools.islice(itertools.cycle(combined), 5 * len(combined)))
# cycle-бесконечный список, islice-ограничение количества элементов, таким образом мы присовокупляем
# islice к cycle и через запятую указываем нужное количество элементов(циклов)
print(result)

# Сделаем то же через itertools.chain
'''
itertools.chain(*iterables)
Объединяет несколько итерируемых объектов в один последовательный итератор.
'''
list1 = ['a', 'b']
list2 = [1, 2, 3]
list3 = ['x', 'y']
combined_tuple = tuple(itertools.chain(list1, list2, list3))  # устойчивый кортеж
result = list(itertools.chain(*itertools.repeat(combined_tuple, 5)))  # представляем списком и повторяем 5 раз
print(result)

# Задача 4: Генерация бесконечной последовательности чисел
# Создайте бесконечный генератор, который будет возвращать последовательность чисел Фибоначчи.
# Выведите первые 10 чисел Фибоначчи.
'''
itertools.count(start=0, step=1)
Генерирует бесконечную арифметическую прогрессию
'''


def fibonacci_count(n):
    def fib_gen():  # создаем генератор
        a, b = 0, 1
        for _ in itertools.count():  # бесконечный генератор
            yield a  # создает генератор выдающий значения по одному
            a, b = b, a + b  # готовит следующее значение

    return list(itertools.islice(fib_gen(), n))  # но мы берем только первые n чисел из бесконечности (islice)


# первые 10 чисел
result = fibonacci_count(10)
print(result)

# Задача 5: Составление всех возможных комбинаций слов
# С itertools.product, создайте все возможные комбинации слов из двух списков: ['red', 'blue'] и ['shirt', 'shoes'].
# Выведите каждую комбинацию на отдельной строке.
l1 = itertools.product(['red', 'blue'], ['shirt', 'shoes'])
for color, item in l1:  # распаковка кортежа для вывода на каждой отдельной строке и доступа к отдельным элементам
    print(f"{color} {item}")
