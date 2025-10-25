print('\n'*5)


            
print('\n'*5)

"""Сокращённый цикл for in"""
# Выражение for Элемент in Последовательность if Условие

# Решение задач по курсу
my_object = {
    'name': 'Igor',
    'surname': 'Oshust',
    'sex': 'Male',
    'id': '32',
}

my_object_upper = {k: v.upper() for k, v in my_object.items()}
my_object_long_length = {k: v for k, v in my_object.items() if len(v) > 3}


print(my_object_upper)
print(my_object_long_length)

# Создать словарь из списка с помощью генератора
my_scores = [10, 7, 14]
scores = {index: elem for index, elem in enumerate(my_scores)}
print(scores)  # {0: 10, 1: 7, 2: 14}

# for in для словаря
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {k: v * 10 for k, v in my_scores.items()}
print(scores)
print(my_scores)

# for in для множеств
my_set = {1, 10, 15}
new_set = {val * val for val in my_set}
print(new_set)


# Создание списка положительных чисел
lst = [abs(i) for i in range(-10, 11)]

# Тот же пример с добавлением условия
lst = [abs(i) for i in range(-10, 11) if abs(i) > 5]

"""Деление введённых чисел"""
# Улучшенная версия кода
while True:
    try:
        first_value = float(input('Enter first value: '))
        second_value = float(input('Enter second value: '))

        # Попытка деления
        result = first_value / second_value
        print(f'Result: {result}')

    except ValueError:
        print('Error: You must ener valid numbers!')
        continue  # проверяем итерацию
    except ZeroDivisionError:
        print('Error: Division by zero! Please enter a non-zero second value')
        continue

    # Если всё прошло успешно, спрашиваем о продолжении
    user_input = input('Try again? yes/no: ')
    if user_input.lower() == 'no':
        break
    elif user_input.lower() != 'yes':
        print('Please enter "yes" or "no".')

print('Bye!')


# Моё решение
user_input = ''

while user_input != 'no':
    first_value = float(input('Enter first value: '))
    second_value = float(input('Enter second value: '))

    try: 
        result = first_value / second_value
    except ZeroDivisionError as e:
        print('Eror: division by zero!')
        second_value = float(input('Enter second value: '))
    print(f'Result: {result}')

    user_input = input('Try again? yes/no: ')
    if user_input == 'yes':
        continue
else:
    print('bye')

# Решение учителя
while True:
    try:
        num_one = float(input('Please enter number one: '))
        num_two = float(input('Please enter number two: '))
    except ValueError as e:
        print(e)
        print('You must enter numbers!')
        continue # переходим на следующую итерацию (нижеизложенные строки кода не будут выполнены в рамках текущей итерации)

    print(num_one / num_two)

    answer = input('Do you want to continue? (yes/no): ')
    if answer == 'no':
        break


"""Угадай число"""
import random

random_num = random.randint(1, 5)

while True:
    num = int(input('Guess the number from 1 to 5: '))
    if num != random_num:
        print('Try again...')
        continue
    print('Congratulations!', random_num)
    break

# Посмотреть подклассы int
print(int.__subclasses__())

# Задача-1
my_object = {
    'name': 'Igor',
    'age': 28,
}
def dict_to_list(dictionary):
    seq = []
    for key, value in dictionary.items():
        if (type(value) == int):
            value *= 2
        seq.append((key, value))
    return seq
print(
    dict_to_list(my_object)
)

# Задача-2
seq = [1, 2, 3, True, 'string']
def filter_list(sequence, type_of_seq):
    new_list = []
    for i in sequence:
        # if isinstance(i, type_of_seq) -- спорный вариант (учитывает True)
        if (type(i) == type_of_seq):
            new_list.append(i)
    return new_list
print(
    filter_list(seq, bool),
    filter_list([3, 'dos', 123], int),
    sep='\n'
)

# Задача-2 (альтернативный вариант)
seq = [1, 2, 3, True, 'string']
def filter_list(sequence, type_of_sequence):
    return list(filter(lambda elem: type(elem) == type_of_sequence, sequence))
print(filter_list(seq, int))

# Задача-2 (решение учителя)
def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)
    return list(filter(check_element_type, list_to_filter))
print(filter_list([1, 10, 'abc', 5.5], int))


"""Циклы"""
# Циклы используются для перебора элементов последовательности
# Последовательности: dict, list, tuple, set, range, str
# Типы: for...in..., while

# Получение значения ключа при обходе словаря
my_dict = {'id': 324, 'title': 'test'}
for key in my_dict:
    print(type(key))
    print(key)
    print(my_dict[key])


# for in по словарю
my_object = {
    'x': 10,
    'y': True,
    'z': 'abc',
}
for key in my_object:
    print(key, my_object[key])

# Сохранение последнего значения перебора в глобальной области видимости
for el in [1, 'abc', True]:
    print(type(el))
    print(el)
print(el)  # True (сохраняет последний элемент), доступна в глобальной области видимости

# Получение значения ключа при обходе словаря
my_dict = {'id': 324, 'title': 'test'}
for key in my_dict:
    print(type(key))
    print(key)
    print(my_dict[key])


"""Тернарный оператор"""
# Вывод сведений в терминал исходя из содержимого кортежа
my_img = ('1920', '1080', True)
def show_result(tup: tuple):
    if len(my_img) == 2:
        return f'{my_img[0]}x{my_img[1]}'
    return 'Incorrect image formatting'
print(show_result(my_img))

# Тернарный оператор для подсчёта длины строки
string = 'jdasjp ijdAPISDJ Paidj pasdjoasjd oiajsdoi ajsodiasjdias oadisjoaisdjaisdjai jaidjapidj'
print('String is long') if len(string) >= 79 else print('String is short')


# Вывод сведений в терминал исходя из содержимого кортежа
my_img = ('1920', '1080',)
info = f'{my_img[0]}x{my_img[1]}' if len(my_img) == 2 else 'Incorrect image formatting'
print(info)

# Тернарный оператор
my_number = 21.5
print('is int') if type(my_number) is int else print('is not int')

# Второй пример (Вызов разных функций в зависимости от того или иного условия)
send_img(img) if img.get['is_processed'] else process_and_send_img(img)

# Третий пример
product_qty = 10
print('in stock' if product_qty > 0 else 'out of stock')

# Присвоение тернарного оператора переменной
temp = +24
weather = 'hot' if temp > 18 else "cold"
print(weather)


# Решение задачи на дистанцию
my_dict = {
    'distance': 3000,
    'speed': 200,
    'time': 10,
}


def route_info(dictionary: dict):
    """Моё решение"""
    if dictionary.get('distance') and (type(dictionary['distance']) is int):
        return f"Distance to your destination is {dictionary['distance']}"

    elif not dictionary.get('distance') and (dictionary.get('speed') and dictionary.get('speed')):
        return f"___Distance to your destination is {dictionary['speed'] * dictionary['time']}"

    else:
        return "No distance info is available"


def route_info_1(route):
    """Решение учителя"""
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"

    # Если первое условие ложно, переходим ко второму условию!
    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return "No distance info is available"


def route_info_2(route):
    """Решение учителя с if-else"""
    if ('distance' in route) and (type(route['distance']) == int):
        route_info = f"Distance to your destination is {dictionary['distance']}"
    elif ('speed' in route) and ('time' in route):
        route_info = f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        route_info = "No distance info is available"
    return route_info


print(
    route_info_1(my_dict),
    sep='\n'
)

# Проверяем тип параметра функции
# !!! Внутри функции лучше использовать return, а не блоки if elif else
def nums_info(a, b):
    """Проверяем тип параметров"""
    if (type(a) is not int) or (type(b) is not int):
        return 'Один из аргументов не целое число'

    if a >= b:
        return f'{a} больше или равно {b}'

    return f'{a} меньше {b}'

print(nums_info(True, 10))

# Альтернативная запись
def nums_info(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = 'Один из аргументов не целое число'
    elif a >= b:
        info = f'{a} больше или равно {b}'
    else:
        info = f'{a} меньше {b}'
    return info


# Проверка позитивного числа
num_one = 10
num_two = 5.3

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
    isinstance(num_two, int)):
    print('Both number are ints and positive')

# Проверка наличия ключа в словаре
my_phone = {
    'price': 200,
    'brand': 'Siemens',
}

if my_phone.get('brand'):
    print('Phone\'s brand is', my_phone['brand'])
else:
    print('There is no phone brand')

# Распаковка списка в позиционные аргументы

"""Создайте список словарей,
в котором 3 словаря,
с помощью оператора распаковки списков
создать 3 переменные каждая из которых будет содержать один из словарей,
создать функцию, принимающую 2 аргумента
в вызове функции должны распаковывать словарь
функцию нужно вызвать трижды (в оригинальном списке должно быть 3 словаря)
у каждого словаря должно быть по два ключа"""

dictionary_list = [
    {'name': 'Igor', 'surname': 'Oshust'},
    {'name': 'Egor', 'surname': 'Malkin'},
    {'name': 'Gregor', 'surname': 'Palkin'},
]

first, second, third = dictionary_list

def get_info(name, surname):
    return f"one - {name}, two - {surname}"

print(
    get_info(**first),
    get_info(**second),
    get_info(**third),
    sep='\n'
)

user_data = ['Bogdan', 23] 

def user_info(name, comments_qty):  # В таком случае в списке должно быть точно два аргумента
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(user_info(*user_data))

"""Распаковка словаря в аргументы с ключевыми словами"""
user_profile = {
    'name': 'Bogdan',
    'comments_qty': 23,
}

def user_info(name, comments_qty=0):  # В таком случае в словаре не может быть более 2 ключей!
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(
    # С помощью распаковки передаём ключи словаря в качестве аргументов функции user_info
    user_info(**user_profile),

    # Альтернативная запись
    user_info(user_profile['name'], user_profile['comments_qty']),

    # С явным указанием аргументов с ключевыми словами
    user_info(name=user_profile['name'], comments_qty=user_profile['comments_qty']),
    
    sep='\n'
)

# + Можно распаковать словарь следующим образом (но не рекомендуется, ибо мы фактически распаковываем названия ключей и не получаем значения этих ключей)
name, comments_qty = user_profile
print(name)
print(comments_qty)

"""Использование * при распаковке"""
my_fruits = ['apple', 'banana', 'lime']
my_apple, *remaining_fruits = my_fruits
print(my_apple)  # apple
print(remaining_fruits)  # ['banana', 'lime']

"""Распаковка списков (LIST)"""
my_fruits = ['apple', 'banana', 'lime']
my_apple, my_banana, my_lime = my_fruits

print(
    my_apple,
    my_banana,
    my_lime
)


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
