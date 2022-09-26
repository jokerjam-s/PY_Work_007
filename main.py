# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Как можно вводить данные?
# На семинаре: формат строки
# ДЗ: txt или csv
# Как их обрабатывать? Где хранить?
# На семинаре: список
# ДЗ: список словарей или другая структура
# Как запрашивать и получать данные?
# Какие функции можно для этого создать?
# Как вынести функции в модули?
#

import data_generate as dg
import data_read_write as drw
import in_out as ino
import os
import data_view as dv

# меню управления
def menu() -> int:
    os.system('cls')
    print('1 - сгенерировать набор')
    print('2 - прочитать набор из txt')
    print('3 - сохранить набор в txt')
    print('4 - экспорт в csv')
    print('5 - отобразить набор на экран')
    print('0 - выход')
    
    res = ino.input_int('> ')
    res = res if res in range(6) else 0

    return res



## MAIN ##

data = []
mn = 1
while mn > 0:
    mn = menu()

    match mn:
        case 1 :
            data = dg.data_gen()
            ino.show_msg('данные сгенерированы')
        case 2:
            data = drw.read_txt('data.txt')
            ino.show_msg('данные загружены')
        case 3:
            drw.save_txt('data.txt', data)
            ino.show_msg('данные сохранены')
        case 4:
            file_name = ino.input_str('файл для сохранения: ')
            drw.save_csv(file_name, data)
            ino.show_msg('данные экспортированы')
        case 5:
            dv.data_print(data)
            ino.show_msg('')
            




