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

# data = dg.data_gen() 

# drw.save_txt('data.txt', data)
# print(data)

# data = drw.read_txt('data.txt')
data = drw.read_csv('data.csv')
print(data)

drw.save_csv('data.csv', data)





