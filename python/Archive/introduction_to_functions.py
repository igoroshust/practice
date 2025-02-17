'''Локальная  (внутренняя) функция - та, которую можно использовать внутри другой функции.'''
# def print_message():
#     def say_hello(): print('hello')
#     def say_bye(): print('bye')
#     say_hello()
#     say_bye()
# print_message()

'''неопределённое количество параметров передаётся с помощью * (распаковка/упаковка)'''
'''С помощью * можно определить параметр, через который мы можем передать неопределённое количество значений. Это может быть полезно, если мы хотим, чтобы функция получала несколько значений.'''
# def sum(*numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     print(f'sum = {res}')
# sum(1,2,3,4)
# sum(1,3,5)

'''Функция, как тип'''
# def say_hello(): print('hello')
# message = say_hello
# message()d

# def sum(a,b): return a + b
# def mult(a,b): return a * b
# operation = sum
# result = operation(5,6)
# print(result)
#
# operation = mult
# print(operation(5,6))

'''Функция, как параметр функции'''
# def do_operation(a, b, operation)
#     result = operation(a, b)
#     print(f'result = {result}')
# def sum(a,b): return a + b
# def mult(a,b): return a * b
#
# do_operation(5,4, sum)
# do_operation(5,4, mult)

'''Функция, как результат функции'''
# def sum(a, b): return a + b
# def mult(a, b): return a * b
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return mult
# operation = select_operation(1)
# print(operation(10, 6))

'''Рекурсия - это когда функция вызывает саму себя'''
# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x + 1)
#         print(x)
# rec(1)

'''Итераторы и генераторы'''
# Итератор - это объект, который поддерживает функцию next() - next помнит о том, какой элемент будет браться следующим.
# Генератор - это итератор, элементы которого мы можем итерировать только один раз. Генератор - это коллекция, которую можем проитерировать только один раз.
# Итерируемый объект - объект, который представляет возможность поочерёдно обойти свои элементы. Например, список
# Функция iter() - можем получить итератор из итерируемого объекта.
# Итерация - процесс перебора элемента коллекции внутри или какой-то функции, которая также делает перебор.

# a = [i ** 2 for i in range(1, 6)] #генератор списка
# print(a)
# b = (i ** 2 for i in range(1,6))
# print(b)
#
# s = [1,2,3]
# # iter ()
# d = iter(s)
# print(next(d))
#
# # yield (альтернатива return) используется в генераторах, в качестве альтернативы одновременному возвращению целого списка
#
# def cube_numbers(nums):
#     for i in nums:
#         yield(i**3)
#     return cube_list
# cubers = cube_numbers([1,2,3,4,5])
# print(*cubers)
# print(next(cubers))
# print(next(cubers))

'''Декораторы - это функция, которая позволяет обернуть другую функцию, при этом расширить её функциональность, при этом она не изменяет функциональность этого кода.'''
# def my_decor(func):
#     def wrapper(n):
#         print('start')
#         func(n)
#         print('end')
#     return wrapper
# @my_decor # декорирование
# def my_func(numbers):
#     print(numbers ** 2)
# my_func(10)