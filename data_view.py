# отображение данных на экран

# присоединим данные о ключах
from data_generate import keys_val as kv

def data_print(data: list):
    for row in data:
        line = f'{row[kv[0]]} {row[kv[1]]} - {row[kv[2]]}'
        print(line)
