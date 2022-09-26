import random as rnd

MEN_NAMES_CNT = 13
MEN_LASTN_CNT = 13
WOMEN_NAMES_CNT = 11
WOMEN_LASTN_CNT = 12

# генерация даных
names_set = (   'Андрей', 'Сергей', 'Дмитрий', 'Олег', 'Семен', 'Иван',
                'Николай', 'Михаил', 'Петр', 'Федор', 'Павел', 'Владимир', 'Владислав',
                'Мария', 'Анна', 'Елена', 'Светлана', 'Ольга', 'Тамара',
                'Татьяна', 'Евгения', 'Оксана', 'Яна', 'Жанна')

lastn_set = (   'Иванов', 'Петров', 'Сидоров', 'Николаенко', 'Галушкин', 'Баширов',
                'Семенов', 'Крупеня', 'Лобов', 'Павлов', 'Тимирязев', 'Тополев', 'Тимошенко',
                'Еремина', 'Иванова', 'Галушкина', 'Курочкина', 'Татьмина', 'Соколова',
                'Решкина', 'Павлова', 'Сидорцова', 'Каманова', 'Толочко', 'Кашина')


def data_gen(cnt_record: int = 20) -> dict:
    result = []
    print(cnt_record)
    for i in range(cnt_record):
        mw = rnd.randint(0, 1)   # м / ж
        
        k = rnd.randint(0, MEN_NAMES_CNT) if mw == 1 else rnd.randint(
            MEN_NAMES_CNT, MEN_NAMES_CNT+WOMEN_NAMES_CNT-1)
        name_pers = names_set[k]
        
        k=rnd.randint(0, MEN_LASTN_CNT) if mw == 1 else rnd.randint(
            MEN_LASTN_CNT, MEN_LASTN_CNT+WOMEN_LASTN_CNT-1)
        lname_pers = lastn_set[k]
        
        phone_pers = f'+{rnd.randint(11111, 99999)}'

        result.append({ 'name': name_pers,
                        'name_last': lname_pers, 'phone': phone_pers})
        
    return result
