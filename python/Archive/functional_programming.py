"""Отсортировать словарь по значениям"""
# d = {2 : "c", 1 : "d", 4: "a", 3 : "b"}
# print(dict(sorted(d.items(), key=lambda x: x[1])))

"""Отсортировать словарь по ключам"""
# d = {2 : "c", 1 : "d", 4: "a", 3 : "b"}
# print(dict(sorted(d.items())))

"""Возвести первые 10 натуральных числе в квадрат при помощи lambda-функции"""
# print(list(map(lambda x: x**2, range(1, 11))))

"""Необходимо вывести только чётные элементы из заданного списка"""
# L = [-2, -1, 0, 1, -3, 2, -3]
#
# def even(x):
#     return x % 2 == 0
#
# result = filter(even, L)
#
# print(list(result))


"""Необходимо из заданного списка вывести только положительные элементы"""
# def positive(x):
#     return x > 0 # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # возвращается итератор, т.е. перечисление или приведение к списку
# print(list(result)) # [1, 2]

"""С помощью методоа строки str.lower переведите все элементы списка в нижний регистр"""
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))

"""Как работает функция filter() под капотом (псевдокод!)"""
# def filter(func, cont):
#     outp = []
#     for x in cont: # проходим циклом по итерируемому объекту
#         if func(x): # проверяем условие для каждого элемента
#             outp.append(x) # если True, добавляем в новый список
#     return outp

"""Как работает функция map() под капотом (псевдокод!)"""
# # сигнатура функции map(function, iter1, iter2, ...)
# def map_(func, some_list):
#     # some_list // объект, над которым будет производиться преобразование
#     # func // функция, которая должна выполняться над каждым объектом
#     some_list = [1, 2, 3]
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp


"""Подумайте, как нужно записать логическое выражение, используя all([ ]) и any([ ]) над списком четности,
если его результат будет истинным тогда и только тогда, когда в списке есть хотя бы один четный и хотя бы один нечетный элемент."""
# L = [1, 2, 3, 4, 5]
# any(L) and not all(L)

"""Напишите программу, чтобы в список сохранялось True, если элемент четный, и False, если элемент нечётный"""
# L = [int(input('Введите значение: ')) % 2 == 0 for i in range(5)]
# print(L)


"""Пример инпута внутри генератора списка"""
# L = [input() for i in range(5)] # запрашиваем у пользователя значения и фиксируем их в списке

"""Пример создания матрицы посредством генератора списков"""
# M = [[i+j for j in range(5)] for i in range(5)]
# print(M)

"""Пример генератора списка (вывод квадратов нечётных чисел)"""
# squares = [i**2 for i in range(1,10) if i % 2 == 1]
# print(squares)

"""Пример замыкания функции"""
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# add_10 = outer_function(10)
# print(add_10(5))


"""Кастомноый итератор"""
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         '''Возвращает объект итератора'''
#         return self
#
#     def __next__(self):
#         '''Возвращает следующий элемент или прекращает итерирование'''
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
# my_list = [1, 2, 3, 4, 5]
# my_iterator = MyIterator(my_list)
#
# for i in my_iterator:
#     print(i)



"""Проверка наличия элемента во вложенных списках"""
# def nested_list_contains(nested_list, target):
#     for item in nested_list:
#         if item == target:
#             return True
#         elif isinstance(item, list):
#             if nested_list_contains(item, target):
#                 return True
#         return False
#
# my_list = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]
# result = nested_list_contains(my_list, 5)
# print(result)



"""Рассчитать сумму чека"""
# def calculate_total(**kwargs):
#     '''saddd'''
#     total = 0
#     for item, price in kwargs.items():
#         total += price
#     return total

# order_total = calculate_total(apple=0.5, banana=0.25, orange=0.75)
# print("Общая стоимость заказа:", order_total)

"""Поиск среднего арифметического (формула: сумма аргументов/их количество)"""
# def average(a, b):
#     return (a+b)/2
# print(average(4, 2))
# второй вариант:
# def average(*args):
#     if len(args) == 0:
#         return 0 # если аргументов нет, возвращаем 0
#     return sum(args) / len(args)
# print(average(2,4,6,8))

"""Запаковка элементов списка"""
# numbers = [1, 2, 3, 4, 5]
# first, second, *rest = numbers
# # Оператор * означает, что остаток списка запакуется в одну переменную
# print(first)
# print(second)
# print(rest)


"""Запаковка/распаковка кортежа"""
# person = ('Сидоров Пётр Петрович', 30, 'Москва')
# print(person)
#
# # распаковка из кортежа
# fio, age, region = person
# print(fio)
# print(age)
# print(region)



"""Область видимости функций"""
# # Global scope
# x = 0
#
# def outer():
#     # enclosed scope
#     x = 1
#     def inner():
#         # local scope
#         x = 2
#         print(x)
#     inner()
#     print(x)
#
# outer()
# print(x)




"""Декоратор, выводящий время работы функции"""
# from time import time, sleep
# def my_timer(func):
#     def wrapper():
#         start_time = time()
#         func()
#         print(f"Время работы функции: {time() - start_time}с.")
#     return wrapper
# @my_timer
# def my_func():
#     sleep(1)
#
# my_func()



"""Пример декоратора"""
# def decorator_function(original_function):
#     def wrapper():
#         print("Текст до вызова функции")
#         original_function()
#         print("Текст после вызова функции")
#     return wrapper
#
# @decorator_function
# def my_function():
#     print("Оригинальная функция")
#
# my_function()



"""Пример замыкания функции"""
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# closure = outer_function(10)
# print(closure(10))
#

"""Генератор бесконечной последовательности (while)"""
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
# print(infinite_sequence())


"""Извлечение значений из словаря"""
# my_dict = {"a": 1, "b": 2, "c": 3}
#
# # for key in my_dict:
# #     print(key)
#
# # for key, value in my_dict.items(): # метод items() возвращает пары ключ-значение [('key', 'value')]
# #     print(f"key: {key}, value: {value}")
#
# for value in my_dict.values():
#     print(value)


"""Пример нелокальной функции"""
# def outer():
#     n = 5 # nonlocal
#     def inner():
#         # nonlocal n # переопределение нелокальной переменной
#         n = 25 # local
#         print(n)
#     inner()
#     print(n)
# outer()



"""Пример распаковки элементов"""
# def print_person(name, age, company):
#     print(f"name: {name}, age: {age}, company: {company}")
# person = ('tom', 38, 'google')
# print_person(*person)

"""Пример распаковки элементов словаря"""
# def print_person(name, age):
#     print(f"name: {name}, age: {age}")
# person = {'name': 'Igor', 'age': 27}
# print_person(**person)

"""Отображение ключ-значения словаря"""
# def func(**kwargs):
#     for key in kwargs:
#         print(f"{key}: = {kwargs[key]}")
# func(name='tom', age='38', company='apple')


"""Функция, как результат функции"""
# def sum_(a, b): return a + b
# def mult(a, b): return a * b
# def select_operation(choice):
#     if choice == 1:
#         return sum_
#     elif choice == 2:
#         return mult
# operation = select_operation(1)
# print(operation(10, 6))
#
# operation = select_operation(2)
# print(operation(10, 6))


"""Функция, как параметр функции"""
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result: {result}")
# def sum_(a, b): return a + b
# def mult(a, b): return a * b
# do_operation(5, 4, sum)
# do_operation(5, 4, mult)

"""Функция, как тип"""
# def say_hello(): print('hello')
# message = say_hello
# message()


"""Пример работы цикла for (под капотом)"""
# for i in gen:
#     print(i)
#
# try:
#     while True:
#         print(gen.next())
# except StopIteration:
#     pass


"""Напишите декоратор, который будет сохранять результаты выполнения декорируемой функции в словаре.
Словарь должен находиться в nonlocal области в следующем формате: по ключу располагается аргумент функии, по значению -
результат работы функции. Например, {n: f(n)}.
И при повторном вызове функции будет брать значение из словаря, а не вычислять заново.
То есть словарь можно считать промежуточной памятью на время работы программы, где будут храниться ранее вычисленные значения.
Исходная функция, которую нужно задекорировать имеет следующий вид и выполняет простое умножение на число 123456789.:

def f(n):
   return n * 123456789"""

# def cache(func):
#     cache_dict = {}
#     def wrapper(num):
#         nonlocal cache_dict
#         if num not in cache_dict:
#             cache_dict[num] = func(num)
#             print(f"Добавление результата в кэш: {cache_dict[num]}")
#         else:
#             print(f"Возвращение результата из кэша: {cache_dict[num]}")
#         print(f"Кэш {cache_dict[num]}")
#         return cache_dict[num]
#     return wrapper
#


"""Напишите декоратор, который будет подсчитывать количество вызовов декорируемой функции. Для хранения переменной содержащей количество
вызовов используйте nonlocal область декоратора."""
# def counter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f"Функция {func} была вызвана {count} раз")
#     return wrapper
#
# @counter
# def say_word(word):
#     print(word)
#
# say_word("Oo!!!")
# say_word("Oo!!!")



"""Шаблон для декоратора"""
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print("Этот код будет выполняться перед каждым вызовом функции")
#         result = fn(*args, **kwargs)
#         print("Этот код будет выполняться после каждого вызова функции")
#         return result
#     return wrapper


"""Замер времени выполнения системной функции для возведения числа в степень 2 и соответствующего оператора"""
# import time
#
# def decorator_time(fn):
#     def wrapper():
#         print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f"Функция выполнилась. Время: {dt:.10f}")
#         return dt # задекорированная функция будет возвращать время работы
#     return wrapper
#
# def pow_2():
#     return 10000000 ** 2
#
# def in_build_pow():
#     return pow(10000000, 2)
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow())
#
# pow_2()
#
# in_build_pow()



"""Пример декоратора"""
# def my_decorator(a_function_to_decorate):
#     def wrapper():
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#
#         return result
#
#     return wrapper
# def my_function():
#     print("Я - оборачиваемая функция!")
#     return 0
# print(my_function())
#
# decorated_function = my_decorator(my_function)
# print(decorated_function())


"""Пример преимущества выражения-генератора над генератором списка (память)"""
# a = [i**2 for i in range(1, 100000000)] # это генератор списка, при вызове он будет высчитывать значения и заносить в память. Если объём большой (как здесь), будешь ошибка.
# b = (i**2 for i in range(1, 100000000)) # это выражение-генератор, при вызове он вернёт <generator ....>, но при next() он будет заносить элементы в память по факту каждой итерации и затем чистить.
# it = iter(b)
# for x in it:
#     print(x)

"""Поиск среднего арифметического"""
# def get_list():
#     for i in range(1, 10):
#         a = range(1, 11)
#         yield sum(a) / len(a)
#
# a = get_list()
# print(list(a))

"""Пример функции-генератора"""
# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x # yield возвращает текущее значение x, замораживает состояние функции до следующего вызова функции next()
# a = get_list()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

"""Выражения-генераторы (возводим в квадрат каждое значение в диапазоне от 1 до 5)"""
# b = (i**2 for i in range(1,6))
# print(next(b))
# ещё пример
# c = (i for i in range(100000)) # такой способ помогает избежать ошибки
# for i in c:
#     print(i)


"""Отображение перечня животных с помощью генератора"""
# def my_animal_generator():
#     yield 'корова'
#     print('---')
#     for animal in ['кот', 'собака', 'медведь']:
#         yield animal
#     print('---')
#     yield 'кит'
#
# a = my_animal_generator()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


"""Создайте генератор, который по переданному списку создаёт последовательность,
 в которой элементы этого списка бесконечно циклично повторяются."""
# def repeat_list(list_):
#     list_values = list_.copy()
#     while True:
#         values = list_values.pop(0)
#         list_values.append(value)
#         yield value
#
# for i in repeat_list([1, 2, 3]):
#     print(i, end=" ")

"""Создать функцию-генератор, возвращающую бесконечную последовательность натуральных чисел.
По умолчанию, она начинается с единицы и шагом 1, но пользователь может указать любой шаг и любое число в качестве аргумента функции,
с которого будет начинаться последовательность."""
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

"""Фибоначчи с помощью функции-генератора"""
# def fib():
#     a, b = 0, 1
#     yield a # F0
#     yield b # F1
#
#     while a < 100 and b < 100: # можно записать здесь while True:
#         a, b = b, a + b
#         yield b
#
# for num in fib():
#     print(f"{num}  ")

"""Пример некорректной работы функции, которая будет возвращать разный результат при каждом вызове (из-за списка)"""
# def incorrect_func(name_args=[]):
#     print("Аргументы функции до изменения:", name_args)
#     name_args.append(1)
#     print("Аргументы функции после изменения:", name_args)
#
# incorrect_func()
# print("---")
# incorrect_func()

"""Если внутри функции нужно использовать списки, то этот момент можно обойти следующим образом (+ к вышестоящему примеру)"""
# def correct_func(name_arg=None):
#     if name_arg is None:
#         name_arg = []
#     print("Аргумент до изменения:", name_arg)
#     name_arg.append(1)
#     print("Аргумент после изменения:", name_arg)
#
# correct_func()
# print("---")
# correct_func()
# print("---")
# correct_func([123])
# print("---")
# correct_func(name_arg=[123])

"""Поиск значения чисел Фибоначчи"""
# def rec_fibb(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     return rec_fibb(n - 1) + rec_fibb(n - 2)
#
# print(rec_fibb(20)) # получится 55, потому что 10 - номер элемента в последовательности: 1,1,2,3,5,8,13,21,34,55(№10),89,144

"""С помощью рекурсивной функции найдите сумму чисел от 1 до n"""
# def rec_sum(n):
#     if n == 1:
#         return 1
#     return n + rec_sum(n - 1)

"""Развернуть строку с помощью рекурсивной функции"""
# def reverse_str(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + reverse_str(string[:-1]) # return n[::-1]
# print(reverse_str('Igor'))

"""Дано натуральное число N. Вычислите сумму его цифр."""
# def sum_digit(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sum_digit(n // 10)
# print(sum_digit(6)) # 6

"""Функция-сумматор значений переданных аргументов"""
# def adder(*nums):
#     sum_ = 1
#     for i in nums:
#         sum_ *= i
#     return sum_
#
# print(adder(2, 8)) # 16
