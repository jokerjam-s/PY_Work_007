# чтение данных из файла, в файл

from operator import index
import os
import csv
import pandas as pd
import numpy as np

# чтение из csv. если файл не существует - пустой словарь
# первая строка - заголовкиt
def read_csv(path: str) -> list:
    if not os.path.exists(path):
        return {}


    df = pd.read_csv(path, delimiter=';',encoding='utf-8', index_col=None)
    data = df.to_dict()
    

    # data = []
    # cnt_rec = 1    
    # with open(path) as file:
    #     csv_reader = csv.reader(file, dialect='excel', delimiter=';')
    #     for r in csv_reader:
    #         data[cnt_rec] = r
    #         cnt_rec += 1

    return data

# чтение из txt
def read_txt(path: str) -> list:
    if not os.path.exists(path):
        return {}
    
    result = {}
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readline().replace('\n', '')
        result = []

        keys = line.split(' ')
        line = data.readline().replace('\n', '')
        while line != '':
            values = line.split(' ')
            tmp = {}
            for i in range(len(keys)):
                tmp[keys[i]] = values[i]
            
            result.append(tmp)
            line = data.readline().replace('\n', '')

    return result


# запись в csv
def save_csv(path: str, data: list)-> list:
    # r_keys = tuple(data[0].keys())

    df = pd.DataFrame.from_dict(data)
    df.to_csv(path, encoding='utf-8')

    # with open(path, 'w', encoding='utf-8') as file:
    #     s = csv.DictWriter(file, fieldnames=r_keys, delimiter=';')
    #     s.writeheader()
    #     for k in d_keys:
    #         s.writerow(data[k])
        
    # print(data)
    return data

# запись в txt
def save_txt(path: str, data: list) -> list:
    l_keys = list(data[0].keys())
    lines = ' '.join(l_keys) + '\n'
    for i in data:
        for k in l_keys:
            lines += i[k] + ' '
        lines = lines[0:-1] + '\n'
    lines = lines[0:-1]
    
    with open(path, 'w', encoding='UTF-8') as file:
        file.writelines(lines)
            
    return data



