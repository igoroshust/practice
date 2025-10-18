print('\n'*5)


#  09:16:45
             

print('\n'*10)

"""Пример вызова функции по умолчанию"""

from datetime import date

def get_weekday():
    return date.today().strftime('%m.%d.%Y')

def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy

initial_post = {
    'id': 243,
    'author': 'Bogdan',
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)

# # Решение задачи-2
def update_car_info(**car):
    car['is_available'] = True
    return car

print(
    res := update_car_info(brand='Toyota', price=4_000_000)
)


# Решение задачи-1
def merge_lists(**kwargs):
    return dict(zip(kwargs['list_one'], kwargs['list_two']))

print(
    res_one := merge_lists(list_one=['a', 'b', 'c'], list_two=[1, 2, 3]),
    #  res_two := merge_lists(['a', 'b', 'c'], list_two=[1, 2, 3]),
)

"""Функции. Объединение аргументов в ключевыми словами в словарь. Работа с kwargs"""
def get_posts_info(**person):
    info = (
        f'{person['name']} wrote '
        f'{person['posts_qty']} posts'
    )
    return info

info = get_posts_info(name='Bogdan', posts_qty=25)
print(info)


"""Функции. Работа с args"""
def sum_nums(*args):
    return sum(args)

print(sum_nums(2, 3, 7))



"""Функции. Задача объединить списки и вернуть словарь"""
lst = [1, 2, 3]
lst1 = [4, 5, 6]

# Моё решение
def merge_lists_to_dict(first_list, second_list):
    first_list_copy = first_list.copy()
    second_list_copy = second_list.copy()

    result = dict(zip(first_list_copy, second_list_copy))
    return result

show = merge_lists_to_dict(lst, lst1)
print(show)


# Решение учителя
def merge_lists(list_one, list_two):
    return dict(zip(list_one, list_two))

res_one = merge_lists(['a', 'b', 'c'], [1, 2, 3])
print(res_one)

"""Функции. Создание копии объекта"""
person_one = {
    'name': 'Bob',
    'age': 21,
}

def increase_person_age_immutable(person):
    """Не меняет состояние исходного объекта"""
    person_copy = person.copy()  # Можно использовать deepcopy, если есть вложенные объекты
    person_copy['age'] += 1
    return person_copy

def increase_person_age_mutable(person):
    person['age'] += 1
    return person

result_immutable = increase_person_age_immutable(person_one)  # Поменяет возраст только в переменной
result_mutable = increase_person_age_mutable(person_one)  # Поменяет возраст объекта на 22

print(person_one)



"""Глубокая и неглубокая копии"""
import copy

info = {
    'name': 'Igor',
    'is_instructor': True,
    'reviews': []
}

other_info = info.copy()


other_info['reviews'].append('Great course!')

print(info, other_info)



"""Функция zip"""
#  zip - встроенная в Python функция, позволяющая объединять элемент из нескольких коллекций (список, кортеж, словарь, строка) в единый набор кортежей.
#  При этом каждый кортеж содержит элементы с одинаковыми индексами из переданных коллекций.
#  Формирование новых элементов на основании существующих последовательностей (объединение последовательностей)
#  zip(*terables)

#  zip передаётся на основании самого короткого списка (если значения не равны, то лишние не включаются)
#  Множества лучше не объединять в zip, поскольку последовательность не гарантируется.

fruits = ['apple', 'banana', 'orange']
quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)
#  <zip object at 0x7fbca80a74c0>

fruit_qtys_list = list(fruit_qtys_zip)

print(fruit_qtys_list)
#  [('apple', 100), ('banana', 70), ('lime', 50)]


#  Пример-1
names = ['Tom', 'Bob', 'Sam']
ages = [41, 46, 35]
for user in zip(names, ages):
    print(user)
#  ('Tom', 41) ...

#  Пример-2
for name, age in zip(names, ages):
    print(f'{name} => {age}')
    
#  Пример-3 (создание вложенных словарей)
"""Вложенные словари подходят, когда 
1) Нужен быстрый доступ к данным по уникальному ключу
2) Ключи имеют смысловую нагрузку и легко читаемы
3) Данные имеют иерархическую структуру

Список словажей лучше использовать, когда:
1) Важен порядок элементов
2) Не требуется быстрый доступ по ключу 
3) Данные однородны и не имеют уникальных идентификаторов 
4) Нужно перебирать элементы последовательно"""
users = {}
i = 0

for name, age in zip(names, ages):
    users.update({f'dict-{i}': {'name': name, 'age': age}})
    i += 1

print(users, sep='\n')


# Альтернативный способ записи
users1 = {}
for i, (name, age) in enumerate(zip(names, ages)):
    users1[f'user_{i}'] = {'name': name, 'age': age}

print(users1)




"""
Последовательности (6 типов)
list (+изменения, +порядок, +одинаковые элементы)
tuple (-изменения, +порядок, +одинаковые элементы)
set (+изменения, -порядок, -одинаковые элементы)
dict (+изменения, -порядок, -одинаковые элементы)
range (-изменения, +порядок, -одинаковые элементы)
str (-изменения, +порядок, +одинаковые элементы)
"""
