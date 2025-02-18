"""Получить информацию об операционной системе"""
# import platform
#
# # Получаем информацию о системе
# os_info = platform.system()
# os_version = platform.version()
#
# print('ОС: ', os_info)
# print('Версия: ', os_version)

"""Сортировка вставками"""
# # Сортировка вставками - алгоритм сортировки, который работает также, как вы сортируете карты в руке.
# # Значение справа сравнивается со значением слева и меняется местами, если значение справа меньше (по условию).
# # Вы берёте одну карту за раз и вставляете её в правильное место среди уже отсортированных карт.
# # file:///C:/Users/Igor/Desktop/%D0%A3%D1%87%D1%91%D0%B1%D0%B0/Skillfactory/insertion_sort.gif

# def insertion_sort(array):
#     for i in range(1, len(array)): # начинаем цикл с i=1 до конца массива. Пропускаем первый элемент (индекс 0), т.к. он считает отсортированным.
#         key = array[i] # Сохраняем текущий элемент, который хотим вставить на правильное место, в переменной key
#         j = i - 1 # Инициализация индекса для сравнения. Устанавливаем j на индекс элемента перед key. Используется для сравнения и сдвига элементов
#
#         # Сдвигаем элементы, которые больше key, на одну позицию вправо
#         while j >= 0 and array[j] > key: # продолжаем сдвигать элементы вправо, пока не найдём правильное место для key
#             array[j + 1] = array[j] # сдвигаем элемент array[j] на одну позицию вправо, чтобы осовобдить место для key
#             j -= 1 # уменьшаем индекс
#
#         # Вставляем key на его правильное место в отсортированной части массива
#         array[j + 1] = key
#
# array = [5, 2, 9, 1, 5, 6]
# insertion_sort(array)
# print("Отсортированный массив:", array)


"""Бинарный поиск"""
# # Это эффективный алгоритм поиска элемента в отсортированном массиве.
# # Делит массив пополам последовательно, пока не найдёт нужный элемент.

# def binary_search(array, target):
#     low = 0
#     high = len(array) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if array[mid] == target:
#             return mid  # Элемент найден
#         elif array[mid] < target:
#             low = mid + 1  # Ищем в правой половине
#         else:
#             high = mid - 1  # Ищем в левой половине
#
#     return -1  # Элемент не найден
#
# # Пример использования
# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 5
# result = binary_search(sorted_array, target)
# print(f"Элемент {target} найден на индексе: {result}")


"""Асинхронные функции"""
# # async и await - ключевые слова в Python, используемые для написания аснхронного кода. Они позволяют писать код, который
# # Они позволяют писать код, который может выполнять операции ввода-вывода (I/O) без блокировки выполнения программы.
# # Это особенно полезно для работы с сетевыми запросами, файловыми операциями и другими задачами, которые могут занять много времени.
# # Возвращают объект типа `coroutine`, который можно запускать с помощью 'await' и 'asyncio.run()'

# # Ключевое слово await используется для ожидания завершения асинхронной операции. Когда используем await,
# # Выполнение функции приостанавливается до тех пор, пока не завершится операция, которую вы ожидаете.
# import asyncio
#
# async def fetch_data():
#     print('Fetching data...')
#     await asyncio.sleep(2)
#     print('Data fetched!')
#     return {"data": 42}
#
# async def main():
#     result = await fetch_data() # Ожидание завершения fetch_data
#     print(f'Result: {result}')
#
# if __name__ == '__main__':
#     asyncio.run(main())



"""aiohttp"""
# # aiohttp - асинхронная библиотека для работы с HTTP в Python, позволяющая выполнять асинхронные HTTP-запросы и создавать
# # асинхронные веб-серверы. Она построена на основе asyncio, что позволяет эффективно обрабатывать множество соединений
# # одновременно, не блокируя выполнение программы.
# # Позволяет выполнять асинхронные GET, POST и другие HTTP-запросы, что делает его идеальным для работы с API и веб-сервисами.
# # Можно использовать aiohttp для создания собственного веб-сервера, способного обрабатывать множество запросов одновременно.
# # Поддерживает WebSocket.

# import aiohttp # работаем с http в асинхронном режиме
# import asyncio # асинхронный код в Python
#
# async def fetch(url): # асинхронная функция, принимающая url аргументом
#     async with aiohttp.ClientSession() as session:
#         """Создаем асинхронную сессию для выполнения HTTP-запросов.
#         'async with' гарантирует закрытие сессии после завершения работы."""
#
#         async with session.get(url) as response:
#             """Выполняем асинхронный GET-запрос к указанному URL. Ответ сохраняем в переменной 'response'"""
#             return await response.json() # извлекаем и возвращаем JSON-данные из ответа (await позволяет дождаться завершения операции)
#
# async def main(): # определяем основную асинхронную функцию, которая будет запускаться в конце
#     url = 'https://jsonplaceholder.typicode.com/posts'
#
#     response = await fetch(url) # вызываем функцию 'fetch' и ждёт её завершения, получая ответ
#
#     for post in response[:5]: # перебираем первые 5 постов из полученного ответа
#         print(f'Post ID: {post['id']}, Title: {post['title']}')
#
# if __name__ == '__main__': # проверяем, что скрипт выполняется как основная программа
#     asyncio.run(main()) # запускаем функцию main(), которая инициирует выполнение всего кода.


"""Какие вы знаете способы выполнять код параллельно/асинхронно?"""
# # 1. Threading - позволяет создавать потоки (threads) для выполнения кода параллельно. Это полезно для задач, требующих
# # Это полезно для задач, требующих много времени на ожидание (например, ввод-вывод). Не эффективен для CPU-bound задач из-за GIL
# import threading
#
# def worker():
#     print('some print')
#
# thread = threading.Thread(target=worker)
# thread.start()
# thread.join()


# # 2. multiprocessing - позволяет создавать процессы, которые могут выполняться параллельно и не подвержены GIL.
# # Это хороший выбор для CPU-bound задач.
# from multiprocessing import Process
#
# def worker():
#     print('some print')
#
# if __name__ == '__main__':
#     process = Process(target=worker)
#     process.start()
#     process.join()

# # 3. asyncio - позволяет писать асинхронный код с использованием async и await.
# # Полезно для задач, связанных с вводом-выводом (например, сетевые запросы).
# import asyncio
#
# async def worker():
#     print('Работа в асинхронной функции')
#     await asyncio.sleep(3)
#
# asyncio.run(worker())

# # 4. concurrent.futures - предоставляет высокоуровневый интерфейс для выполнения параллельных задач с использованием
# # потоков (ThreadPoolExecutor) или процессов (ProcessPoolExecutor).
# from concurrent.futures import ThreadPoolExecutor
#
# def worker():
#     print('Работа в пуле потоков')
#
# with ThreadPoolExecutor() as executor:
#     executor.submit(worker)

# # Модуль joblib - используется для параллельного выполнения задач, особенно в контексте научных вычислений и машинного
# # обучения. Поддерживает как потоки, так и процессы.
# from joblib import Parallel, delayed
#
# def worker(i):
#     return i * i
#
# results = Parallel(n_jobs=2)(delayed(worker)(i) for i in range(9+1))


"""Миграции данных"""
# # Миграция - процесс переноса данных из одной БД в другую или изменение структуры БД с сохранением данных.
# # В конетексте Django - способ управления изменениями в моделях и их отражения в БД.
# # Миграции – механизм, посредством которого обеспечивается управление изменениями в структуре базы данных, связанными с изменениями в моделях приложения.
# # Благодаря миграциям можно автоматически создавать и применять изменения в базе данных (добавление, изменение, удаление полей таблиц).

# Основные команды:
# 1. python manage.py makemigrations - создание новых миграций;
#
# 2. python manage.py makemigrations <app_name> - создание новых миграций для указанного приложения;
#
# 3. python manage.py makemigrations –merge - объединение миграций в одну с целью разрешения конфликтов;
#
# 4.python manage.py migrate - применение миграций в БД (+ создание самой базы при первом запуске);
#
# 5. python manage.py migrate <app_name> <migration_name> - откат миграций до указанного состояния (предыдущая миграция);
#
# 6. python manage.py migrate <app_name> zero - обнуление миграций для указанного приложения;
#
# 7. python manage.py showmigrations - демонстрация списка миграций для каждого приложения;



"""Как в request появляется атрибут user?"""
# # В Django атрибут user в объекте request появляется благодаря middleware, который обрабатывает аутентификацию пользователей.
# # Когда пользователь выполняет запрос, Django проходит через цепочку middleware, и один из них - 'AuthenticationMiddleware`
# # Этот Middleware - проверяет, если ли у запроса сессия + извлекает идентификатор сессии + загружает объект пользователя
# # из базы данных и добавляет его в объект request как атрибут user.

"""Как работают сигналы?"""
# # Сигналы в Джанго - это механизм, позволяющий различным частям приложения взаимодействовать друг с другом, не
# # создавая жёсткой зависимости. Сигналы позволяют отправлять уведомления о событиях, таких как создание, изменение,
# # или удаление объектов. Сигналы определяются в Django с помощью модуля `django.dispatch`. Наиболее часто используемые
# # сигналы включают:

# # pre_save, post_save
# # pre_delete, post_delete
# # m2m_changed

# # Пример использования сигнала
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import MyModel
#
# @receiver(post_save, sender=MyModel)
# def my_handler(sender, instance, created, **kwargs):
#     if created:
#         print(f'Создан новый объект: {instance}')



"""Что такое декораторы?"""
# # Декораторы - это функции, позволяющие изменять или расширять поведение других функций или методов.
# # Декораторы принимают функцию в качестве аргумента и возвращают новую функцию, которая добавляет некоторую дополнительную
# # функциональность.

# @decorator
# def function_to_decorate():
#     pass
#
# # Равно следующему коду
# def function_to_decorate():
#     pass
#
# function_to_decorate = decorator(function_to_decorate)

# # Пример

# def my_decorator(func):
#     def wrapper():
#         print('Что-то происходит до вызова функции')
#         func()
#         print('Что-то происходит после вызова функции')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('Привет из say_hello')
#
# say_hello()


"""Что такое List Comprehension?"""
# # List Comprehension - удобный и лаконичный способ создания списков в Python,
# # Позволяющий создавать новый список, применяя выражение к каждому элементу итерируемого объекта в 1 строке кода.
# new_list = [expression for item in iterable if condition]
# # expression - выражение, которое вычисляется для каждого элемента
# # item - переменная, принимающая значение каждого элемента из iterable
# # iterable - любой итерируемый объект
# # condition - необязательное условие, фильтрующее элементы

# # Создание списка квадратов только чисел
# new_list = [x**2 for x in range(1, 10) if x % 2 == 0]
#
# print(new_list)


"""Опишите, как будет работать приложение, в котором надо реализовать:
- Регистрация пользователей
- Зарегистрированные пользователи могут создавать посты
- Незарегистрированные пользователи могут читать посты """

# import reg # Подробнее в этом файле

# 1. Структура приложения. Основные компоненты:
# - Модели, Представления, Шаблоны, URL-адреса
#
# 2. Модели
# - Создаём модель User и Post
#
# 3. Создаём регистрацию пользователей:
# - Форма регистрации
# - Представление регистрации
#
# 4. Создание постов:
# - Создаём форму PostForm
# - Представление для создания поста
#
# 5. Незарегистрированные пользователи смогут читать посты:
# - Представление для списка постов
#
# 6. URL-адреса
# - Настройка маршрутов
#
# 7. Настройка шаблонов
#
# 8. Настройка аутентификации
#
# 8. Защита представлений
#
# 8. Запуск приложения



"""Перечислите методы DJango ORM"""
# import DjangoORM_Methods # Список в этом файле

# all()
# get()
# get_or_create()
# update()
# update_or_create()
# delete()
# create()
# bulk_create()
# exclude()
# filter(**kwargs)
# order_by(**kwargs)
# values()
# value_list()
# aggregate()
# distinct()
# first()
# last()
# count()
# save()
#
# exists()
# annotate()
# iterator()
# transaction.atomic()
# prefetch_related()


"""Как записать в базу данных сразу множество объектов"""
# # Ответ: с помощью метода bulk_create() модели. Он добавляет несколько экземпляров модели за один запрос к БД

# from django.db import models
#
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     published_date = models.DateField()
#
#
# # # В другом файле
#
# from myapp.models import Book
#
# books_to_create = [
#     Book(title='Book 1', description='Author 1', published_date='2023-01-01'),
#     Book(title='Book 2', description='Author 2', published_date='2023-02-01'),
#     Book(title='Book 3', description='Author 3', published_date='2023-03-01'),
# ]
#
# # # Сохраняем все объекты в БД за один запрос
# Book.objects.bulk_create(books_to_create)

"""Что такое FBV и CBV в Django?"""
# # Пример FBV
# from django.http import HttpResponse
# from django.shortcuts import render
#
# def my_view(request):
#     # Логика обработки запроса
#     return HttpResponse("Hello, World!")
#
# # # Пример CBV
# from django.http import HttpResponse
# from django.views import View
# class MyView(View):
#     def get(self, request):
#         return HttpResponse("Hello, world!")


"""Функция map"""
# iter_list = [1, 2, 3, 4, 5]
# result = map(lambda x: x * 2, iter_list)
# print(list(result))


# def double(x):
#     return x * 2
#
# iter_list = [1, 2, 3, 4, 5]
#
# double_result = map(double, iter_list)
#
# print(list(double_result))

# iter_list = ['Игорь', 'Андрей', 'Виктор']
#
# def say_hello(name):
#     return 'Привет, ' + name
#
# result = map(say_hello, iter_list)
#
# print(list(result))

# # Применение функции к нескольким итерируемым объектам

# def add(x, y):
#     return x + y
#
# numbers = [i for i in range(1, 10+1)]
# numbers_two = [i for i in range(11, 20+1)]
#
# result = map(add, numbers, numbers_two)
# print(list(result)) # Здесь сумма 1 элемента из numbers и 1 элемента numbers_two, и так до конца списка


"""Виды форматирования строк"""
# name = 'Igor'
# age = 28
#
# # Интерполяция (шаблонные строки) (добавлен в Python 3.6, самый новый способ)
# print(f'My name is {name}, I\'m {age} years old')
#
# # Оператор % (пришёл из C)
# print('My name is %s, I\'m %d years old' % (name, age))
#
# # str.format() (введён в Python 2.7)
# print('My name is {}, I\'m {} years old'.format(name, age))
#
# # str.Template
#
# from string import Template
#
# template = Template('My name is $name, I\'m $age years old')
# formatted_string = template.substitute(name=name, age=age)
#
# print(formatted_string)

"""Примеры GET и POST запросов"""
# # GET
# GET /search?q=python HTTP/1.1
# Host: example.com

# # POST
# POST /submit HTTP/1.1
# Host: example.com
# Content-Type: application/x-www-form-urlencoded
#
# name=John&surname=Smith


"""Что такое copy и deepcopy"""
# # Методы, используемые для создания копий объектов. Copy - поверхностно, deepcopy - основательно
# import copy
#
# original_list = [1, 2, [3, 4]]
# # copy_list = copy.copy(original_list)
# copy_list = copy.deepcopy(original_list)
#
# original_list[2][0] = 'changed'
#
# print(original_list)
# print(copy_list)


"""Отличие is от =="""
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a == b) # True
# print(a is b) # False
# print(id(a))
# print(id(b))

"""Реализуйте функцию sort_pair, которая принимает пару (кортеж из двух значений) и возвращает пару,
значения которой расположены строго в порядке возрастания."""
# def sort_pair(pair):
#     # Сортируем значения в кортеже и возвращаем их как новый кортеж
#     return tuple(sorted(pair))
#
# # Примеры использования
# print(sort_pair((5, 1)))  # (1, 5)
# print(sort_pair((2, 2)))  # (2, 2)
# print(sort_pair((7, 8)))  # (7, 8)

"""Кортежи"""
# # Основное применение - когда нужно вернуть сразу несколько значений
# def div_mod(a, b):
#     quotient = a // b
#     modulo = a % b
#     return (quotient, modulo)
#
# print(div_mod(13, 4))

# # Распаковка или деструктуризация кортежа
# name_and_age = ('Bob', 42)
#
# (name, age) = name_and_age
# name  # 'Bob'
# age   # 42


"""Выбрать случайный символ из строки"""
# from random import choice
#
# string = 'abcde'
# char = choice(string)
#
# print(char)


"""Определить количество гласных в тексте"""
# # Корректный вариант
# from symbols import is_vowel
#
# def count_vowels(text):
#     count = 0
#     for i in text:
#         if is_vowel(i):
#             count += 1
#     return count

# # Альетрнативный вариант
# def count_vowels(s):
#     g = 'aeoiuy'
#     return len(list(filter(lambda x: x in g, s.lower())))
#
# print(count_vowels('London is the capital of Great Britain'))

"""Палиндром"""
# # Решение ИИ
# import re
# def is_palindrome(word):
#     # Удаляем все не буквенные символы и пробелы, приводим к нижнему регистру
#     cleaned_word = re.sub(r'\s+', '', word.lower()) # Удаляем пробелы
#     return cleaned_word == cleaned_word[::-1]
#
# print(is_palindrome('а лис он умен крыса сыр к нему носила'))

# # Мой вариант
# def is_palindrome(word):
#     if word.lower() == word[::-1].lower():
#         return True
#     else:
#         return False
#
# print(is_palindrome('ишак ищет у тещи каши'))

# ишак ищет у тещи каши
# а лис он умен крыса сыр к нему носила


"""Реализуйте функцию filter_string(). Она принимает на вход строку и символ и возвращает новую строку,
в которой удален переданный символ во всех его позициях.
Если строка не содержит указанный символ, то она возвращается без изменений."""
# def filter_string(text, symbol):
#     # Удаляем все вхождения символа и обрезаем пробелы
#     return text.replace(symbol, '').replace(symbol.lower(), '').strip()
#
# text = 'I look back if you are lost'
# filter_string(text, 'i')  # 'look back f you are lost'
# filter_string(text, 'O')  # 'I lk back if yu are lst'


# # Моё решение
# def filter_string(string, symbol):
#     new_string = ''
#
#     for i in string.lower():
#         if i != symbol.lower():
#             new_string += i
#         else:
#             pass
#
#     return new_string.strip()
#
# print(filter_string('look back if you are lost', 'l'))

# # Решение ИИ
# def filter_string(string, symbol):
#     # Удаляем все вхождения символа и обрезаем пробелы
#     return string.replace(symbol, '').replace(symbol.lower(), '').strip()
#
# print(filter_string('look back if you are lost', 'l'))


"""Цикл for"""
# # Количество упоминаний символа в строке без учёта регистра
# def chars_count(text, char):
#     result = 0 # поскольку ищем сумму, начальное значение 0
#     for current_char in text:
#         # Приводим всё к нижнему регистру
#         if current_char.lower() == char.lower():
#             result += 1
#     return result
#
# print(chars_count('hexlet!', 'e'))
# print(chars_count('hExlet!', 'e'))
# print(chars_count('hExlet!', 'E'))


# # Функция переворота строки

# def reverse_string(text):
#     # Начальное значение
#     result = ''
#     # char - переменная, в которую записывается текущий символ
#     for char in text:
#         # Соединяем в обратном порядке
#         result = char + result
#
#     return result
#
# print(reverse_string('go!'))


# # Перебор символов в строке
# text = 'igor'
# for symbol in text[::-1]:
#     print(symbol)


# # Вывод слова без переменной
# for _ in range(1, 4):
#     print('Hooray!')


# # Вывод обратной последовательности
# for i in range(5, -1, -1):
#     print(i)


"""Поиск суммы значений в диапазоне"""
# # Вариант через for
# sum = 0
#
# for i in range(6):
#     sum += i
# print(sum)

# # Вариант через while
# sum = 0
# i = 0
#
# while i < 10:
#     sum += i
#     i += 1
#
# print(sum)


"""Реализуйте функцию has_char().
Она должна проверять, содержит ли строка указанную букву (вне зависимости от регистра).
Функция принимает два параметра:"""

# Решение учителя
# def has_char(string, char):
#     return char.lower() in string.lower()
#
# print(has_char('abracadabra', ''))

# # Моё решение
# def has_char(string, char):
#
#     index = 0
#
#     while index < len(string):
#         if string[index] == char.lower() or string[index] == char.upper():
#             return True
#         index += 1
#
#     return False
#
#
# print(has_char('abracadabra', 'A'))



"""Алгоритм проверки простоты числа (делится нацело на себя и на единицу)"""
# def is_prime(number):
#     if number < 2:
#         return False
#     divider = 2
#     while divider <= number / 2:
#         if number % divider == 0:
#             return False
#         divider += 1
#
#     return True
#
# def show_prime(number):
#     if is_prime(number):
#         return 'простое'
#     else:
#         return 'составное'
#
# # Ввод числа от пользователя
# user_input = int(input("Введите число: "))
#
# # Определение чётности
# parity = 'чётное' if user_input % 2 == 0 else 'нечётное'
#
# # Результат вывода
# print(f'Число {user_input} - {show_prime(user_input)} {parity} число')



"""Функция, считающая количество вхождений подстроки в строку"""
# # Решение учителя

# def count_chars(string, char):
#     index = 0
#     count = 0
#
#     while index < len(string):
#         if string[index] == char:
#             # Считаем только подходящие символы
#             count += 1
#         # Счётчик увеличивается в любом случае
#         index += 1
#
#     return count
#
# print(count_chars('abracadabra', 'a'))


# # Моё решение:
# def count_chars(string, word_count):
#     lst = []
#
#     for i in string:
#         if i == word_count:
#             lst.append(i)
#
#     return len(lst)
#
# print(count_chars('abracadabra', 'b'))


"""Декларативный способ - ЧТО? - фокусировка на результате"""
# string = 'igor'
# print(string[::-1])

"""Императивный способ - КАК? - фокусировка на процессе"""
# def reverse_string(string):
#     index = len(string) - 1
#     reversed_string = '' # НЭ
#
#     while index >= 0:
#         current_char = string[index]
#         reversed_string += current_char
#         index -= 1
#
#     return reversed_string
#
# print(reverse_string('Game Of Thrones'))
#
# string = 'Game Of Thrones'
# print(string[::-1])



# Реализуйте функцию, извлекающую из строки подстроку указанной длинны
# def get_substr(string, length):
#     index = len(string) - 1
#     result_string = ''
#
#     while index >= 0:
#         result_string = string[:length]
#         index -= 1
#
#     return result_string
#
# print(get_substr('If I look back I am lost', 7)) # If I lo


"""Обход строк"""
# Напечатайте каждую буквы слова в отдельной строке
# def print_name_by_symbol(name):
#     i = 0
#
#     # Такая проверка будет выполняться до конца строки,
#     # включая последний символ. Его индекс len(name) - 1.
#     while i < len(name):
#         # Обращаемся к символу по индексу
#         print(name[i])
#         i += 1
#
# name = 'Arya'
# print_name_by_symbol(name)


# Функциональный способ переворачивания строки
# def reverse_string(string):
#     index = len(string) - 1
#     reversed_string = '' # Нейтральный элемент
#
#     while index >= 0:
#         current_char = string[index]
#         reversed_string += current_char
#         index -= 1
#
#     return reversed_string
#
# print(reverse_string('Game Of Thrones'))


"""Агрегирование данных """
# Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку и возвращает получившуюся строку:
# def join_numbers_from_range(start, finish):
#     result = []
#     i = start
#
#     while i <= finish:
#         result.append(str(i))
#         i += 1
#
#     return "".join(result)
#
# print(join_numbers_from_range(10, 20)) #5678910

# # Функция умножения строки
# def repeat(text, times):
#     result = '' # Нейтральный элемент
#     i = 1
#
#     while i <= times:
#         # Каждый раз добавляем строку к результату
#         result += text
#         i += 1
#
#     return result
#
# print(repeat('igor', 3))

# # Дублирование строки
# def string_repeat(text, times):
#     result = ''
#     i = 1
#
#     while i <= times:
#         result += text
#         i += 1
#
#     return result
#
# print(string_repeat('abra', 3)) # abraabraabra


# Считаем суммы цифр от start до finish
# def sum_numbers_from_range(start, finish):
#     i = start
#     sum = 0 # Инициализация суммы
#     while i <= finish: # Двигаемся до конца диапазона
#         sum += i # Считаем суммы для каждого числа
#         i += 1 # Переходим к следующему числу в диапазоне
#
#     return sum
#
# print(sum_numbers_from_range(1, 10))


"""Циклы (while)"""
# Выводим n раз строку hello
# def print_hello(n):
#     counter = 0
#     while counter < n:
#         print('Hello')
#         counter += 1
#
# print_hello(2)

# Выводим на экран числа от числа-аргумента до 1

# def print_numbers(last_number):
#     i = 1
#     while last_number >= i:
#         print(last_number)
#         last_number -= 1
#     print('Finished!')
#
# print_numbers(3)

"""Оператор match (проверка переменной на равенство в условии)"""
# # Вариант с оператором | (ИЛИ)
# def match_input(input):
#     match input:
#         case 'start' | 'begin':
#             print('Starting...')
#         case 'stop' | 'end':
#             print('Stopping...')
#         case 'pause':
#             print('Pausing...')
#         case _:
#             print('Invalid input')
#
# match_input('begin')
# match_input('stop')
# match_input('pause')
# match_input('test')


# # Третий вариант
# def count_items(count):
#     result = ''
#
#     match count:
#         case 1:
#             result = 'one'
#         case 2:
#             result = 'two'
#         case 3:
#             result = 'three'
#         case _: # else
#             result = None
#
#     return result
#
# print(count_items(2))

# # Второй вариант
# def count_items(count):
#     match count:
#         case 1:
#             return 'one'
#         case 2:
#             return 'two'
#         case _:
#             return None


# # Первый пример
# status = 'paid'
#
# match status:
#     case 'processing':  # status == 'processing'
#         # Делаем раз
#     case 'paid':  # status == 'paid'
#         # Делаем два
#     case 'new':  # status == 'new'
#         # Делаем три
#     case _:  # else
#         # Делаем четыре


"""Тернарный оператор"""
# def abs(number):
#     return number if number >= 0 else -number
#
# def get_type_of_sentence(sentence):
#     last_char = sentence[-1]
#     return 'question' if last_char == '?' else 'normal'
#
# print(get_type_of_sentence('Hodor'))
# print(get_type_of_sentence('Hodor?'))

"""Определение типа предложения"""
# def get_type_of_sequence(sentense):
#     last_char = sentense[-1]
#
#     if last_char == '?':
#         sentence_type = 'question'
#
#     elif last_char == '!':
#         sentence_type = 'exclamation'
#
#     else:
#         sentence_type = 'normal'
#
#     return 'Sentense type is ' + sentence_type
#
# print(get_type_of_sequence('Hodor'))
# print(get_type_of_sequence('Hodor?'))
# print(get_type_of_sequence('Hodor!'))

"""Нелькальная переменная"""
# def outer_function():
#     x = 10 # Нелокальная переменная
#
#     def inner_function():
#         """Изменяем значение x"""
#         nonlocal x # переменная x нелокальная (хотим изменить X, а не создавать новую локальную переменную)
#         x += 5 # изменяем значение x
#
#     inner_function() # вызываем внутреннюю функцию
#     return x # возвращаем изменённое значение x
#
# result = outer_function()
# print(result)


"""Локальные и глобальные переменные"""
# age = 5
#
# def generate():
#     # age = 10
#     return age + 3
#
# result = generate()
# print(result)



"""Аннотация типов"""
# def concat(first: str, second: str) -> str:
#     return first + second
#
# a = 'Ig'
# b = 'or'
#
# print(concat(a, b))


"""Возвращение последнего символа в строке"""
# def get_last_char(text):
#     return text[-1]
#
# name = 'Hexlet'
#
# print(get_last_char(name))


"""Создание объекта (ООП)"""
# class Dog:
#     species = "Canis familiaris" # классовый атрибут
#
#     def __init__(self, name):
#         self.name = name # атрибут - переменная, хранящая данные, связанные с объектов: атрибуты могут быть экземплярными и классовыми (общими для всех объектов)
#     # экземплярные атрибуты создаются внутри метода __init__ и относятся к конкретному объекту.
#     def bark(self): # метод - функция внутри класса, описывающая поведение объектов. Могут принимать параметры и изменять состояние объекта или выполнять действия
#         return f"{self.name} says woof!"
#
# # Создание объекта класса Dog
# my_dog = Dog("Buddy") # объект - экземпляр класса, содержащий данные и поведение
# print(my_dog.name) # Buddy
# print(my_dog.bark()) # Buddy says woof!
# print(my_dog.species) # Canis familiaris

"""Работа с созданным объектом"""
# class Dog:
#     about = "Canis Familiaris" # классовый атрибут
#
#     def __init__(self, name, age):
#         """Конструктор для объявления атрибутов"""
#         self.name = name # экземплярный атрибут
#         self.age = age
#
#     def __str__(self):
#         """Человекочитаемое предсталвение"""
#         return f'Dog(name={self.name}, age={self.age})'
#
#     def bark(self):
#         """Лай"""
#         return f'{self.name} says woof!'
#
# my_dog = Dog("Buddy", 12)
# print(my_dog.name) # Buddy
# print(my_dog.age) # 21
# print(my_dog)
# print(my_dog.about) # Canis ...
# print(my_dog.bark()) # Buddy says woof!


"""Документация по функции"""
# print(len.__doc__)

"""Пример побочного действия в функции"""
# count = 0
#
# def increment():
#     global count
#     count += 1
#
# print(count) # 0
# increment()
# print(count) # 1