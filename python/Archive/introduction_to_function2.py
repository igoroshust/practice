









"""Возвращение куба числа из списка"""
# def cube_num(nums):
#     """Возвращение куба числа из списка"""
#     cube_list = []
#     for i in nums:
#         cube_list.append(i ** 3)
#     return cube_list # return возвращает данные целиком, yield возвращает генератор.
# cubes = cube_num([1, 2, 3, 4, 5])
# print(cubes)

# def cube_num(nums):
#     """Функция возвращает генератор"""
#     for i in nums:
#         yield(i ** 3)
# cubes = cube_num([1, 2, 3, 4, 5])
# print(cubes)
# print(next(cubes)) # 1
# print(next(cubes)) # 8
# print(next(cubes)) # 27
"""Когда мы снова вызываем next() генератора, функция cube_num возобновляет выполнение с того места, где она ранее остановилась на yield, и функция будет выполняться до тех пор, пока не найдётся yield до момента 'stop iteration'"""

"""Генератор списка"""
# a = [i ** 2 for i in range(1,6)]
# print(a)

# """Выражения генератора"""
# a = (i ** 2 for i in range(1,6))
# print(a)

# s = [1, 2, 3]
# d = iter(s)
# print(next(d)) # 1
# print(next(d)) # 2
# print(next(d)) # 3

# def rec(x):
#     """Пример рекурсии, принцип работы https://skrinshoter.ru/sNH487uCfLS?a """
#     if x < 4:
#         print(x)
#         rec(x + 1)
#         print(x)
# rec(1)


# def rec(x):
#     """Пример рекурсии"""
#     print(x)
#     rec(x + 1)
#     print(x) # 999 и ошибка
# rec(1)


# def do_operation(a, b, operation):
#     """Функция, как параметр функции"""
#     result = operation(a, b)
#     print(f'result = {result}')
# def sum(a, b): return a + b
# def mult(a, b): return a * b
# do_operation(5, 4, sum) # если в качестве третьего аргумента будет sum, то a и b сложатся; если mul - будет вычеслено произведение.


# def say_hello():
#     """Функция, как тип"""
#     print('hello')
# message = say_hello
# message()
#
# def sum(a, b):
#     """Функция, как тип"""
#     return a + b
# operation = sum
# print(operation(5, 6))





# def print_message():
#     """Пример локальных функций"""
#     def say_hello(): print('hello')
#     def say_bye(): print('bye')
#     say_hello()
#     say_bye()
# print_message()

# def sum_list(data):
#     '''Подсчёт суммы элементов списка'''
#     count = 0
#     for i in data:
#         count += i
#     return count
# print(sum_list([1, 2, 3, 4, 5, 6, 7]))

# def even_list(data):
#     """Функция, отображающая только чётные элементы списка"""
#     lst = [] # создаём список, в который записываем найденные чётные числа.
#     for i in data:
#         if i % 2 == 0:
#             lst.append(i)
#     return f'Перечень чётных чисел: {lst}' # возвращаем список
# print(even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


'''Поиск площади круга'''
# import math
# pi_const = round(math.pi, 2)
# def area_of_circle_simple(radius):
#     return pi_const*(radius**2)
# print(area_of_circle_simple(5))
#
#
#
# def display_info(name, age): # здесь не пишем значения. Тут заготовка.
#     return "Hello! My name is {name}, my age is {age}" # Здесь шаблон
# display_info('Tom', 23) # здесь значения переменных
# display_info('Bob', 30)