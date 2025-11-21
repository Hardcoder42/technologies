import os

#1 ЧАСТЬ

#создаем
dir_name="Управление_файлами"
try:
    os.mkdir(dir_name)
    print("Директория "Управление_файлами" успешно создана!")
except Exception as e:
    print(f"Error: {e}")

#переходим
os.chdir("Управление_файлами")
print(f"Переходим в директорию: {os.getcwd()}")

#1файл
with open("text1.txt", 'w', encoding='utf-8') as file1:
    file1.write('Первый файл\n')
print('Файл "file1.txt" успешно создан!')

#2файл
with open('file2.txt', 'w', encoding='utf-8') as file2:
    file2.write('Второй файл\n')
print('Файл "file2.txt" успешно создан!')

print('\nСодержимое директории: ')
files = os.listdir()
for file in files:
    print(f"- {file}")

#2 ЧАСТЬ

#удаляем 1 из созданных файлов
try:
    os.remove(C:\Users\Ирина\Desktop\Python313\test_repository\Управление_файлами\file2.txt)
    print("Файл 'file2.txt' успешно уничтожен!")
except Error as e:
    print(f"Ошибка: {e}")

#создаем поддиректорию
dir_name2 = "Поддиректория"
try:
    os.mkdir(dir_name2)
    print("Директория "dir_name2" создана успешно!")
except Exception as e:
    print(f"Ошибка: {e}")

#перемещение файла
try:
    os.rename("Управление_файлами\text1.txt", "Поддиректория\text1.txt")
    print(Файл "file1.txt"успешно перемещен...)
except Exception as e:
    print(f"Ошибка: {e}")

#удаление директории вместе с содержимым
try:
    for item in os.listdir("Управление_файлами"):
        path = os.path.join("Управление_файлами", item)

        #на предмет файлов
        if os.path.isfile(path):
            os.remove(path)
            print(f"Удален файл: {item}")
        #на предмет поддиректорий
        elif os.path.isdir(path):
            os.rmdir(path)
            print(f"Удалена поддиректория: {item}")
    os.rmdir("Управление_файлами")
    print("Директория "Управление_файлами" успешно уничтожена!")
except Exception as e:
    print(f"Ошибочка вышла: {e}")

#проверка содержимого
print('\nОставшееся содержимое директории: ')
files = os.listdir()
for file in files:
    print(f"- {file}")