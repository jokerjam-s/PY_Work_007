# чтение данных из файла, в файл

from asyncio.windows_events import NULL
import os
import csv

# чтение из csv. если файл не существует - пустой словарь
# первая строка - заголовкиt
def read_csv(path: str, delim:str = ';') -> dict:
    if os.path.exists(path):
        return {}
    
    

# чтение из txt


# запись в csv


# запись в txt


