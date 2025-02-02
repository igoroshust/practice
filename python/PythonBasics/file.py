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