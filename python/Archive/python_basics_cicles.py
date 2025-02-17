"""Напишите программу, которая на вход принимает последовательность целых чисел и возвращает True,
если все числа равны нулю, и False, если найдется хотя бы одно ненулевое число."""
# L = list(map(int, input().split()))
# print(not any(L))


"""Напишите программу, которая на вход принимает последовательность целых чисел, и возвращает True,
если все числа ненулевые, и False, если хотя бы одно число равно 0"""
# L = list(map(int, input().split()))
# print(all(L))


"""Напишите программу, которая проверяет, является ли число целым, находится ли в определённом промежутке
(от 100 до 999 включительно) и делится на 2 и 3 одновременно."""
# решение с использованием нескольких if
# a = int(input('Введите число: '))
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")

# решение с использованием логических операторов и операторов сравнения
# a = int(input('Введите число: '))
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print(f"Число {a} удовлетворяет запросу")

# решение с помощью функции all([])
# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print(f"Число {a} удовлетворяет требованиям")


"""Напишите программу, которая на вход принимает текст и выводит количество уникальных символов"""
# text = input('Введите текст: ')
# unique = set(text)
# print("Количество уникальных символов в тексте: ", len(unique))


"""Пример использования цикла for в условных конструкциях"""
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
# c = []
#
# for i in a:
#     if i <= 5:
#         b.append(i)
#     else:
#         c.append(i)
# print(b)
# print(c)




"""Напишите функцию, которая будет возвращать количество делителей числа а.
Пример ввода: 5
Пример вывода программы: 2"""
# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# get_multipliers(5)  # 2
# get_multipliers(4)  # 3


"""Напишите функцию, которая печатает “обратную лесенку” следующего типа:
n = 3
***
**
*
"""
# решение учителя
# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
# reverse_stair(5)
#
# # моё решение
# def check_num(a, n):
#     for i in range(a, 0, -1):
#         print(i * n)
#         i -= 1
# check_num(3, '*')



"""Проверить, является ли число n делителем числа а"""
# def check_num(a, n):
#     if a % n == 0:
#         print(f"Число {a} является делителем числа {n}, потому что {a}/{n} = {round(a/n)}")
#     else:
#         print(f"Число {a} не является делителем числа {n}")
# check_num(180, 36)



"""Возврести числа из списка в третью степень"""
# def cube_numbers(nums):
#     cube_list = []
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
#
# print(cube_numbers([1, 2, 3, 4, 5]))

"""Определение чётности введённого числа (рекурсивный способ)"""
# def check(n):
#     if (n < 2):
#         return (n % 2 == 0)
#     return check(n-2)
# n = int(input('Введите число: '))
# if (check(n) == True):
#     print('Число чётное')
# else:
#     print('Число нечётное')


"""Игра счастливое/несчастливое число"""
# import random
#
# game = True
# while game:
#     a = int(input('Enter your number: '))
#     if a == random.randint(0, 10):
#         print('You win!')
#         break
#     else:
#         print('You lose!')

"""Вывести все значения/ключи словаря"""
# my_dict = {
#     "first_el": "apple",
#     "second_el": "banana"
# }
# for value in my_dict.values(): # .values() выводит значения, .keys() - ключи, .items() выводит список пар
#     print(value)
# вывод пар ключ значение
# for key, value in my_dict.items():
#     print(f"{key} --- {value}")

"""Найти наименьшее значение в списке"""
# a = [3, 2, 1, -5, 4, 3, 2, 6, 7, -3, -5, 8, 1]
# s = a[0]
#
# for i in a:
#     if i < s:
#         s = i
# print(s)

"""Вывод всех нечётных/чётных элементов списка"""
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in lst:
#     if not i % 2: # если нужно вывести чётные, то: if not i % 2
#         print(i)
# # P.S. x % 2 выдаёт нечетные потому, что если x % 2 == 0, то 0 - это false, а если not x % 2, то это True

"""Поиск факториала числа (произведение данного числа и всех предшествущих до 1)
Пример факториала:
5! = 5*4*3*2*1
"""
# f = 5
# s = 1
# # range(1, a+1) = [1, 2, 3, 4, 5]
# for x in range(1, f+1):
#     s *= x
# print(s)

"""Факториал числа с помощью функции"""
# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
# print(fact(4))

"""Алгоритмический способ посчитать сумму значений элементов списка"""
# lst = [1, 2, 3, 4, 5]
# s = 0
# for i in lst:
#     s += i
# print(s)

"""Способ посчитать сумму значений элементов списка при помощи функции"""
# lst = [1, 2, 3, 4, 5]
# def _sum():
#     s = 0
#     for i in lst:
#         s += i
#     return s
# a = _sum()
# print(a)

"""Вывести элементы списка с помощью while"""
# a = [1, "Hello", 5]
# count = len(a) # длина списка
# while count != 0:
#     count -= 1
#     print(a[count])


"""Написать программу, которая проверяет наличие числа N в значении X"""
# def has_digit(one, two):
#     while True:
#         k = one % 10
#         if k == two:
#             return f"Содержит {two}"
#         if one < 10:
#             return f"Не содержит {two}"
#         one = one // 10
# print(has_digit(1204, 9))

"""Найти в списке чётный элемент"""
# lst = [1, 5, 3, 6, 0, -4]
#
# flFlag = False
# i = 0
#
# while i < len(lst):
#     flFlag = lst[i] % 2 == 0
#     if flFlag:
#         break
#     i += 1
# print(flFlag)


"""Напишите программу, которая выводит количество символов в строке"""
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
#
# count = {} # для подсчёта символов и их количества
# for letter in text:
#     if letter in count: # если символ уже встречался, то увеличиваем его количество на 1
#         count[letter] += 1
#     else:
#         count[letter] = 1
# print(count)

# for char, cnt in count.items():
#     print(f"Символ {char} встречается {cnt} раз")




"""Напишите программу, которая выводит значение каждого элемента списка со значением его массива """
# list_ = [-5, 2, 3, 4, 1, True, 14]
# for i in range(len(list_)): # for i in list_[1, 2, 3, 4, 5, 6, 7]
#     print("Значение элемента", list_[i])
#     print("Индекс элемента", i)
#     print("---")
# print("Конец цикла")

#c помощью функции enumerate()
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # функция enumerate возвращает данные в виде кортежей, где на 1 месте стоит индекс, затем - значение
# # [(0, -5), (1, 2), (2, 4), (3, 8), (4, 12), (5, -7), (6, 5)]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value) # с помощью индекса получаем значение элемента.
#     print("---")
# print("Конец цикла")



"""Дана двумерная матрица 3x3 (двумерный массив).
Необходимо определить максимум и минимум каждой строки, а также их индексы."""
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
#
# for row in random_matrix:
#     min_index = 0 # индекс кандидата (по алгоритму изначально кандидат - это первый элемент, поэтому индекс 0)
#     min_value = row[min_index] # сам кандидат, его значение (по алгоритму это первый элемент, поэтому можно написать row[0]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements: ", min_value_rows) # минимальные элементы
# print("Their indices: ", min_index_rows) # их индексы
# print("Maximal elements: ", max_value_rows) # максимальные элементы
# print("Their indices: ", max_index_rows) # их индексы





"""Пример работы с вложенными циклами"""
# matrix = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print() # этот принт относится к циклу for row in matrix:

# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[1][0])
# print(matrix[1][1])
# print(matrix[2][0])
# print(matrix[2][1])

"""Напишите программу, которая будет печатать лесенку следующего типа:
n = 3
*
**
***
"""
# s = 0
# n = 4
# for i in range(1, n+1):
#     print('*' * i)


"""Найти сумму всех натуральных чисел от 1 до N включительно"""
# s = 0 # переменная-счётчик, в которой считается сумма
# n = 5
# # заводим цикл for, в котором мы будет проходить по всем числам от одного до N
# for i in range(1, n + 1):
#     print("Значение суммы на предыдущем шаге: ", s)
#     print("Текущее число: ", i)
#     s = s + i # суммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", s)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна", s)


"""Исправить ошибку (9 строка), чтобы цикл не был бесконечным."""
# employee = 5
# i = 1
# while i < employee:
#     if i > 1:
#         print('There are', i, 'people in the department') # В отделе i человек
#     if i == 1:
#         print('There are', i, 'people in the department') # В отделе i человек
#     i += 1


"""Олег положил тысячу рублей в банк под 8% годовых с ежегодной капитализацией процентов.
Капитализация процентов означает, что проценты за каждый год прибавляются к сумме вклада
 и в следующем году также участвуют в начислении процентов.
Определите, через сколько лет сумма на счете Олега составит не менее трёх тысяч рублей."""
# bill = 1000
# year = 0
#
# while bill <= 3000:
#    procent = (bill / 100) * 8
#    bill = bill + procent
#    year += 1
#    print(round(bill))
# print('year: ', year)
# print('score: ', round(bill))

"""Напишите программу, которая считает неотрицательные степени двойки до тех пор,
пока это число не станет больше 10 000.
В ответ запишите количество итераций, которые проделывает цикл."""
# n = 2
# while 2**n <= 10000:
#    n += 1
#    print('считаем...')
# print('количество итераций: ', n)


"""Принудительное завершение цикла с помощью break"""
# n = 1
# while True: # в данноц программе это условие всегда True, цикл будет бесконечным
#     print('Hello World!')
#     n += 1
#     if n > 10: # условие, при достижении которого цикл while будет принудительно завершен.
#         break

"""Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000"""
# n = 1
# s = 0
# while n**2 < 1000:
#     n += 1
#     s += n
#     print('Считаю...')
# print('Максимальное натруальное число, квадрат которого меньше 1000: ', n-1)


"""Написать цикл, который будет складывать натуральные числа, пока их сумма не превысит 500"""
# n = 1 # текущее натуральное число, с которого начинается сложение натуральных чисел
# s = 0 # это переменная-счётчик, в которой считается сумма чисел
# while s < 500:
#     s += n # увеличиваем сумму
#     n += 1 # так как сумма не достигла нужного значения, то увеличиваем переменную-счётчик.
#     print('Ещё считаю...')
# print("Сумма равна: ", s)
# print("Количество чисел: ", n-1)


"""Вывод строчных символов из численного диапазона."""
# def join_numbers_from_range(start, finish):
#     i = start
#     memory = ''
#     while i <= finish:
#         memory = memory + str(i)
#         i = int(i) + 1
#     print(memory)
# join_numbers_from_range(0,11)

"""Пример работы match"""
# def get_number_explanation(text):
#     match text:
#         case 666:
#             print('devil number')
#         case 42:
#             print('answer for everything')
#         case 7:
#             print('prime number')
#         case _:
#             print('just a number')
# get_number_explanation(7)



"""Match"""
# status = 'processing'
# match status:
#     case 'processing':
#         print('1')
#     case 'paid':
#         print('2')
#     case 'new':
#         print('3')
#     case _:
#         print('4')

"""Нормализация url-адреса"""
# def normalize_url(url):
#     if url[:8] == 'https://':
#          return url
#     elif url[:7] == 'http://':
#      return url.replace(url[:7], 'https://')
#     else:
#         return f'https://{url}'
#
# normalize_url('http://yandex.ru')


"""Рекомендации по одежде в зависимости от температуры (моё решение)"""
# wear = ['Пуховик', 'Пальто', 'Дождевик', 'Зонт', 'Резиновые сапоги', 'Футболка', 'Шорты']
# temperature = int(input('Укажите текущую температуру \n : '))
#
# if temperature >= 20 and temperature <= 30:
#     a = int(input('Есть осадки? \n : '))
#     if a == 1:
#         print(f"Вам нужно надеть: {wear[-2]}, {wear[-1]} и {wear[2]}")
#     elif a == 2:
#         print(f"Вам нужно надеть: {wear[-2]} и {wear[-1]}")
# if temperature < 20:
#     b = int(input('Температура выше 0 градусов? \n : '))
#     if b == 1:
#         print(f"Нужно надеть {wear[0]}")
#     elif b == 2:
#         c = int(input('Есть осадки? \n : '))
#         if c == 2:
#             print(f"Вам нужно надеть {wear[1]}")
#         elif c == 1:
#             d = int(input('Осадки сильные? \n : '))
#             if d == 2:
#                 print(f"Вам нужно надеть {wear[1]} и {wear[0]}")
#             elif d == 1:
#                 print(f"Вам нужно надеть {wear[0]}, {wear[4]} и {wear[3]}")
# else:
#     print(False)

"""Рекомендации по одежде в зависимости от температуры (решение учителя решение)"""
# temperature = int(input('Введите температуру: '))
# # для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
# # если температура < 0, то про дождь спрашивать бессмысленно
# if temperature > 0:
#     rainy = input("Дождь идёт?: ") == "Да"
# # если идёт дождь, нужно уточнить, насколько он серьёзный
#     if rainy:
#         heavyRain = input("Сильный дождь?: ") == "Да"
# decision = "Не решил, что брать. Останусь дома"
# if (temperature) > 20 and (temperature < 30):
#     if rainy:
#         decision = "Взять футболку, шорты и дождевик"
#     else:
#         decision = "Взять футболку и шорты"
# elif temperature > 0:
#     if rainy:
#         if heavyRain:
#             decision = "Взять пальто, резиновые сапоги и зонт"
#         else:
#             decision = "Взять пальто и дождевик"
#     else:
#         decision = "Взять пальто"
# else:
#     decision = "Взять пуховик"
# print(decision)


"""Проверить, является ли строка палиндромом"""
# number = 111
# string = str(number)
# if string == string[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')
# второй способdef check_pal(text):
# #     text = text.lower()
# #     text = text.replace(" ", "")
# #     if text == text[::-1]:
# #         return True
# #     else:
# #         return False
# # print(check_pal('Кит на море не романтик'))
#

"""Тернарный оператор"""
# a = 10
# b = 333
# c = 123
#
# # if a <= 45 or b <= 45 or c <= 45:
# #     print(True)
# # else:
# #     print(False)
#
# result = True if a <= 45 or b <= 45 or c <= 45 else False
# print(result)



"""Определение сезона по введённому месяцу"""
# month = int(input(': '))
# if month in [3, 4, 5]:
#     print('Весна')
# elif month in [6, 7, 8]:
#     print('Лето')
# elif month in [9, 10, 11]:
#     print('Осень')
# elif month in [12, 1, 2]:
#     print('Зима')

"""Встроенные типы данных:"""
# Логический тип: bool
# Числовые типы: int, float, complex
# Последовательности: list, tuple, range
# Строки (строковые последовательности): str
# Бинарные типы: bytes, bytearray, memoryview
# Множества: set, frozenset
# Коллекции: dict
# Пустой тип: None

"""Определить, является ли предложение палндромом. За один проход по строке"""
# s = 'А лис, он умен - крыса сыр к нему носила'
# start, end = 0, len(s) - 1
# while start < end:
#     startChar, endChar = s[start].lower(), s[end].lower()
#     # пропускаем символы, не являющиеся буквами или цифрами
#     if startChar.isalnum() and endChar.isalnum():
#         if startChar != endChar:
#             print(False)
#             break
#         else:
#             start, end = start + 1, end - 1
#             continue
#     start, end = start + (not startChar.isalnum()), end - (not endChar.isalnum())
# else:
#     print(True)

"""Есть список целых чисел и целевое значение. Нужно вернуть индексы двух элементов списка, которые в сумме дают целевое значение."""
# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     n = target - nums[i]
#     if n in nums[i+1:]:
#         print(i, nums.index(n, i+1))
#         break


"""В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов."""
# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

"""Отлов исключения"""
# a = [1, "Hello", 5, 6, ['my list', 5]]
# it = iter(a)
# try:
#     while True:
#         print(next(it))
# except StopIteration:
#     pass