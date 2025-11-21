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
os.chdir(dir_name)
print(f"Переходим в директорию: {os.getcwd()}")

#1файл
with open("file1.txt", 'w', encoding='utf-8') as file1:
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
    os.remove("file2.txt")
    print("Файл 'file2.txt' успешно уничтожен!")
except Exception as e:
    print(f"Ошибка: {e}")

#создаем поддиректорию
dir_name2 = "Поддиректория"
try:
    os.mkdir(dir_name2)
    print(f'Директория "{dir_name2}" создана успешно!')
except Exception as e:
    print(f"Ошибка: {e}")

#перемещение файла
try:
    os.rename("file1.txt", os.path.join(dir_name2, "file1.txt")
    print('Файл "file1.txt"успешно перемещен...')
except Exception as e:
    print(f"Ошибка: {e}")

#Возврат в родительскую директорию для возможности удаления
os.chdir("..")

#удаление директории вместе с содержимым
try:
    for item in os.listdir(dir_name):
        path = os.path.join(dir_name, item)

        #на предмет файлов
        if os.path.isfile(path):
            os.remove(path)
            print(f"Удален файл: {item}")

        # на предмет поддиректорий
        elif os.path.isdir(path):
            #сначала очистка
            for sub_item in os.listdir(path):
                sub_path=os.path.join(path, sub_item)
                if os.path.isfile(sub_path):
                    os.remove(sub_path)
            os.rmdir(path)
            print(f"Удалена поддиректория: {item}")
    os.rmdir(dir_name)
    print('Директория "Управление_файлами" успешно уничтожена!')
except Exception as e:
    print(f"Ошибочка вышла: {e}")

#проверка содержимого
print('\nОставшееся содержимое директории: ')
files = os.listdir()
for file in files:
    print(f"- {file}")