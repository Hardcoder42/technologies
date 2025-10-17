import csv #вызов модуля

def txt_to_csv(txtfile_path, csvfile_path, delimiter=None):
    """Конвертер текстового файла в .csv с автоматическим определением разделителя
	
	args:
		txtfile_path - путь к исходному тексту
		csvfile_path - путь для сохранения .csv
		delimeter (str, optional) - разделитель(None - определяется автоматически)
		
	returns:
		.csv файл
	
	"""
	#открываем файл
    with open(txtfile_path, 'r', encoding='utf-8') as txtfile:
        #записываем файл
        with open(csvfile_path, 'w', newline='', encoding='utf-8') as csvfile:
            lines = txtfile.readlines()
            writer = csv.writer(csvfile)
            
            for line in lines:
                if delimiter:
                    row = line.strip().split(delimiter)
                else:
                    # Автоопределение разделителя
                    if '\t' in line:
                        row = line.strip().split('\t')
                    elif ';' in line:
                        row = line.strip().split(';')
                    else:
                        row = line.strip().split()
                writer.writerow(row)

# Использование
txt_to_csv('prices.txt', 'prices.csv')