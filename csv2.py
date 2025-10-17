import csv

def full_price(source, destination, index1, index2):
    """Вычисляет стоимость позиций и их общую сумму
    
    Args:
        source (str): Входной файл .csv с данными
        destination (str): Выходной файл .csv с результатами
        index1 (int): Индекс колонки (Количество)
        index2 (int): Индекс колонки (Цена)
        
    Returns:
        float: Общая сумма стоимости всех позиций.
        """
    
    with open(source, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
            
        total_sum = 0
        
        
        for i in range(len(data)):
            try:
                quantity = int(data[i][index1])
                # Количество товара из строки
                price = float(data[i][index2])
                # Цена единицы товара из строки
                total_cost = quantity * price
                # Количество на стоимость
                total_sum += total_cost
                # Прайс строки к итоговой сумме
                
                # Добавляем итоговую сумму в текущую строку
                data[i].append(total_cost)
                print(f"Строка {i}: {quantity} * {price} = {total_cost}")
            except (ValueError, IndexError):
                data[i].append('')
                # Если ошибка, оставить поле пустым
                
        		# Итоговая строка
        last_row = ["Общая стоимость заказа"] + [""] * (len(data[0]) - 2) + [str(total_sum)]
        data.append(last_row) #добавили
    
        # Запись результата в выходной файл
        with open(destination, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
    
    return total_sum

# Using
total = full_price('prices.csv', 'result.csv', 1, 2)
print(f"Общая стоимость заказа: {total}")