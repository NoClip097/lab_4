import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    for i in items:  # Лезем в словари предметов последовательно
        if len(args) == 1:  # Для вывода значения по единственному ключу...
            yield i[args[0]] # ...просто отдаём значение
        else:  # Если ключей больше...
            d_out = {}  # ...будем отдавать словарь
            for j in args:  # Берём ключи последовательно
                if i[j] is not None:  # Предусмотреть возможное отсутствие пары!!!
                    d_out[j] = i[j]  # Добавляем в словарь соответствующую пару
            yield d_out  # Отдаём


# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randrange(begin, end+1, 1)