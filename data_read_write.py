# чтение данных из файла, в файл

import os
import pandas as pd

# чтение из txt
def read_txt(path: str = 'data.txt') -> list:
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
def save_csv(data: list, path: str = 'data.csv')-> list:

    df = pd.DataFrame.from_dict(data)
    df.to_csv(path, encoding='utf-8', index=False)

    return data

# запись в txt
def save_txt(data: list, path: str = 'data.txt') -> list:
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



