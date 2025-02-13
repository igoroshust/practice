"""Ход ферзём в шахматах"""
# queen_cell_column = int(input())
# queen_cell_row = int(input())
#
# request_cell_column = int(input())
# request_cell_row = int(input())
#
# # Проверяем, что запрашиваемая клетка находится на доске
# if 1 <= request_cell_column <= 8 and 1 <= request_cell_row <= 8:
#     # Проверяем, может ли ферзь сделать такой ход
#     if (queen_cell_column == request_cell_column) or \
#        (queen_cell_row == request_cell_row) or \
#        (abs(queen_cell_column - request_cell_column) == abs(queen_cell_row - request_cell_row)):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')  # Если запрашиваемая клетка вне границ доски


"""Ход конём в шахматах"""
# knight_cell_column = int(input())
# knight_cell_row = int(input())
#
# request_cell_column = int(input())
# request_cell_row = int(input())
#
# # Проверяем, что запрашиваемая клетка находится на доске
# if 1 <= request_cell_column <= 8 and 1 <= request_cell_row <= 8:
#     # Проверяем, может ли конь сделать такой ход
#     if (abs(knight_cell_column - request_cell_column) == 2 and abs(knight_cell_row - request_cell_row) == 1) or \
#        (abs(knight_cell_column - request_cell_column) == 1 and abs(knight_cell_row - request_cell_row) == 2):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')  # Если запрашиваемая клетка вне границ доски


"""Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли слон попасть с
первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки"""
# # Ход слона: https://skrinshoter.ru/sUAXfDSCvaR

# bishop_cell_column = int(input())
# bishop_cell_row = int(input())
#
# request_cell_column = int(input())
# request_cell_row = int(input())
#
# # Проверяем, что запрашиваемая клетка находится на доске
# if 1 <= request_cell_column <= 8 and 1 <= request_cell_row <= 8:
#     # Проверяем, находится ли запрашиваемая клетка на одной диагонали со слоном
#     if abs(bishop_cell_column - request_cell_column) == abs(bishop_cell_row - request_cell_row):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')  # Если запрашиваемая клетка вне границ доски



"""Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
Если число находится вне диапазона [1;10], то программа должна вывести текст «ошибка» (без кавычек)"""

# array = {
#     1: 'I',
#     2: 'II',
#     3: 'III',
#     4: 'IV',
#     5: 'V',
#     6: 'VI',
#     7: 'VII',
#     8: 'VIII',
#     9: 'IX',
#     10: 'X',
# }
#
# num = int(input())
#
# if 1 <= num <= 10:
#     for i in array:
#         if i == num:
#             print(array[num])
# else:
#     print('ошибка')


"""Заданы две клетки шахматной доски. Напишите программу, которая определяет, имеют ли указанные клетки один цвет или нет.
Если они покрашены в один цвет, то выведите слово «YES» (без кавычек), а если в разные цвета, то «NO» (без кавычек)."""
# # Шахматная доска: https://skrinshoter.ru/sUAJpFeEI7L
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# pillar_1 = [i for i in range(1, 9, 2)] # 1 3 5 7
# pillar_2 = [i for i in range(2, 9, 2)] # 2 4 6 8
#
# a1_result = None
# a2_result = None
#
# if a in pillar_1:
#     if b in pillar_1:
#         a1_result = 'white'
#     else:
#         a1_result = 'black'
# elif a in pillar_2:
#     if b in pillar_1:
#         a1_result = 'black'
#     else:
#         a1_result = 'white'
#
# if c in pillar_1:
#     if d in pillar_1:
#         a2_result = 'white'
#     else:
#         a2_result = 'black'
# elif c in pillar_2:
#     if d in pillar_1:
#         a2_result = 'black'
#     else:
#         a2_result = 'white'
#
# if a1_result == a2_result:
#     print('YES')
# else:
#     print('NO')

# if a in pillar_1 and b in pillar_1:
#     a1_result = 'white'
# elif a in pillar_2 and b in pillar_2:
#     a1_result = 'black'
#
# if c in pillar_1 and d in pillar_1:
#     a2_result = 'white'
# else:
#     a2_result = 'black'
#
# if a1_result == a2_result:
#     print('YES')
# else:
#     print('NO')
#
# print(a1_result)
# print(a2_result)


"""Найти границы пересечения отрезков"""
# # Скриншот с ТЗ: https://skr.sh/sUACRNAoQsX
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
#
# # Находим границы пересечения
# start = max(a1, a2)
# end = min(b1, b2)
#
# # Проверяем, есть ли пересечение
# if start > end:
#     print("пустое множество")
# elif start == end:
#     print(start)  # Общая точка
# else:
#     print(start, end)  # Отрезок пересечения


"""Определение номера кармана"""
# # Задача: https://skrinshoter.ru/sUAronFU5kZ
# pocket = int(input())
#
# if pocket < 0 or pocket > 36:
#     print('ошибка ввода')
# else:
#     if pocket == 0:
#         print('зеленый')
#     else:
#         # Определяем диапазон и цвет
#         if 1 <= pocket <= 10:
#             color = 'красный' if pocket % 2 != 0 else 'черный'
#         elif 11 <= pocket <= 18:
#             color = 'черный' if pocket % 2 != 0 else 'красный'
#         elif 19 <= pocket <= 28:
#             color = 'красный' if pocket % 2 != 0 else 'черный'
#         elif 29 <= pocket <= 36:
#             color = 'черный' if pocket % 2 != 0 else 'красный'
#
#         print(color)

"""Калькулятор"""
# a, b, operation = int(input()), int(input()), input()
#
# if operation == '+':
#     print(a + b)
# elif operation == '-':
#     print(a - b)
# elif operation == '*':
#     print(a * b)
# elif operation == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(a / b)
# else:
#     print('Неверная операция')


"""Дан порядковый номер месяца (1, 2, ..., 12). Напишите программу, которая выводит на экран количество дней в этом месяце.
Принять, что год является невисокосным"""

# # Решение ИИ
# n = int(input("Введите номер месяца (1-12): "))
#
# # Список, где индекс соответствует номеру месяца (0 - январь, 1 - февраль и т.д.)
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# if 1 <= n <= 12:
#     print(days_in_month[n - 1])  # Выводим количество дней в месяце
# else:
#     print('Некорректное значение')

# # Моё решение:
# n = int(input())
# result = [i for i in range(1, 13)]
#
# if len(str(n)) > 0 or len(str(n)) > 12:
#     if (n in result[:8:2] or n == 8) or (n in result[9::2]):
#         print('31')
#     elif n == 2:
#         print('28')
#     else:
#         print('30')
# else:
#     print('Некорректное значение')

# # Решение ИИ №2
# n = int(input("Введите номер месяца (1-12): "))

# Словарь, где ключ - номер месяца, значение - количество дней
# days_in_month = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }
#
# if n in days_in_month:
#     print(days_in_month[n])  # Выводим количество дней в месяце
# else:
#     print('Некорректное значение')



"""Даны три различных целых числа. Напишите программу, которая находит серединное значение из этих чисел"""
# a, b, c = int(input()), int(input()), int(input())
#
# result = [a, b, c]
# result.sort()
#
# print(result[1])

# a, b, c = int(input()), int(input()), int(input())
#
# result = [a, b, c]
# result.remove(max(result))
# result.remove(min(result))
#
# print(str(result[0]))


"""Даны три целых числа. Определите, сколько среди них совпадающих"""
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif a == c:
#     print(2)
# else:
#     print(0)

# # Второй способ - с использованием каскадного условного оператора и логического оператора or
# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print(3)
# elif a == b or b == c or a == c:
#     print(2)
# else:
#     print(0)

"""Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли король попасть
с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки."""
# # Скриншот хода короля: https://skrinshoter.ru/sUAuNeFuyGK

# # 1 клетка
# a = int(input()) # номер столбца 1 клетки
# b = int(input()) # номер строки 1 клетки
#
# # 2 клетка
# c = int(input()) # номер столбца 2 клетки
# d = int(input()) # номер строки 2 клетки
#
# if ((a == c) or (c == a + 1) or (c == a - 1)) and ((b == d) or (d == b + 1) or (d == b - 1)):
#     print('YES')
# else:
#     print('NO')


"""Даны две различные клетки шахматной доски. Напишите программу, которая определяет, может ли ладья попасть
с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки"""
# # Скриншот: https://skrinshoter.ru/sUAKroqZiSH

# # 1 клетка
# a = int(input()) # номер столбца 1 клетки
# b = int(input()) # номер строки 1 клетки
#
# # 2 клетка
# c = int(input()) # номер столбца 2 клетки
# d = int(input()) # номер строки 2 клетки
#
# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')

"""Напишите программу, которая определяет, является ли год с данным номером високосным. Если год является високосным,
то выведите «YES» (без кавычек), иначе выведите «NO» (без кавычек). Год является високосным, если его номер кратен 4,
но не кратен 100 или не кратен 400"""

# year = int(input())
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')


"""Напишите программу, определяющую, является ли введённое число красивым
Назовём число красивым, если оно является четырёхзначным и делится нацело на 7 или на 17"""
# num = int(input())
#
# if (len(str(num))) == 4 and (num % 7 == 0 or num % 17 == 0):
#     print('YES')
# else:
#     print('NO')

"""Определить, относится ли X к промежуткам"""
# # Промежутки: https://skrinshoter.ru/sUAOtBIYdQZ

# if -2 >= x > -30 or 25 >= x > 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


"""Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти,
в которой она находится"""
# # Четверти наглядно: https://skrinshoter.ru/sUAQpcohxAT

# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')





"""Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны"""
# num = 998
#
# first_letter = num // 100
# middle_letter = (num % 100) // 10
# last_letter = num % 10
#
# empty_set = {first_letter, middle_letter, last_letter}
#
# if len(empty_set) != 1:
#     print('Числа различны')
# else:
#     print('Числа равны')

"""Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным."""
# num = int(input())
#
# if 100 <= num <= 999:
#     print('Число является трёхзначным')
# else:
#     print('Число не является трёхзначным')


"""Таблица истиности операторов 'and' и 'or'"""
# +-------+-------+---------+--------+
# |   A   |   B   | A and B | A or B |
# +-------+-------+---------+--------+
# | True  | True  |  True   |  True  |
# | True  | False |  False  |  True  |
# | False | True  |  False  |  True  |
# | False | False |  False  |  False |
# +-------+-------+---------+--------+

# Приоритет: not -> and -> or
"""Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел."""
# a = int(input())
# b = int(input())
# c = int(input())
#
# result = []
#
# if a > 0:
#     result.append(a)
# if b > 0:
#     result.append(b)
# if c > 0:
#     result.append(c)
#
# print(sum(result))

"""Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
сумма первой и последней цифр равна разности второй и третьей цифр"""
# num = int(input()) # 1234
#
# first_letter = num // 1000 # 1
# second_letter = (num % 1000) // 10**2
# third_letter = (num % 100) // 10**1
# last_letter = num % 10 # 4
#
#
# if (first_letter + last_letter) == (second_letter - third_letter):
#     print('ДА')
# else:
#     print('НЕТ')


"""Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел"""
# num1, num2, num3 = int(input()), int(input()), int(input())
#
# counter = 0
# if num1 % 2 == 0:
#     counter += 1
# if num2 % 2 == 0:
#     counter += 1
# if num3 % 2 == 0:
#     counter += 1
#
# print(counter)


"""Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр"""
# digit = int(input()) # 0
#
# a = digit // 10 # 1
# b = digit % 10 # 0
#
# if a == b:
#     print('Равны')
# else:
#     print('Не равны')


"""Напишите программу, которая выводит прямоугольник, по периметру состоящий из звёздочек (*).
Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно."""
# w = '*' * 20
# h = '*' * len(w)
#
# h = h[:1] + (' ' * (len(w)-2)) + h[-1]
#
# print(w)
# print(h)
# print(h)
# print(w)



"""Напишите программу для нахождения цифр пятизначного числа."""
# num = int(input())
#
# first_digit = num // 10000
# second_digit = (num % 10**4) // 10**3
# third_digit = (num % 10**3) // 10**2
# four_digit = (num % 10**2) // 10**1
# last_digit = num % 10
#
# print(first_digit)
# print(second_digit)
# print(third_digit)
# print(four_digit)
# print(last_digit)


"""Дано трехзначное число abc‾, в котором все цифры различны.
Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа."""

# # Считываем трехзначное число
# number = input("Введите трехзначное число: ")
#
# # Проверяем, что число трехзначное и все цифры различны
# if len(number) == 3 and len(set(number)) == 3:
#     # Извлекаем цифры
#     a, b, c = number[0], number[1], number[2]
#
#     # Генерируем и выводим все перестановки
#     print(f"{a}{b}{c}")
#     print(f"{a}{c}{b}")
#     print(f"{b}{a}{c}")
#     print(f"{b}{c}{a}")
#     print(f"{c}{a}{b}")
#     print(f"{c}{b}{a}")
# else:
#     print("Ошибка: Введите трехзначное число с различными цифрами.")

"""Напишите программу, в которую вводится трехзначное число и которая выводит на экран его цифры (через запятую)."""
# num = int(input(': '))
#
# first_digit = num // 100
# central_digit = (num // 10) % 10
# last_digit = num % 10
#
# print(first_digit, central_digit, last_digit, sep=', ')


"""Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа."""
# num = int(input(': '))
# first_digit = num // 10
# last_digit = num % 10
#
# first_digit, last_digit = last_digit, first_digit
# reversed_digit = f'{first_digit}{last_digit}'
#
# print(reversed_digit)

# # ИЛИ ТАК
# num = int(input())
# last_digit = num % 10
# first_digit = num // 10
#
# print('Искомое число =', last_digit * 10 + first_digit)

"""Напишите программу, в которой реализована сумма цифр двузначного числа"""
# num = int(input('Введите число: ')) # 46
# first_digit = num // 10 # 4
# last_digit = num % 10 # 6
# add = first_digit + last_digit
# print(f'Сумма чисел {first_digit} и {last_digit} = {add}')


"""Напишите программу, определяющую число десятков и единиц в двузначном числе."""
# num = int(input('Введите число: '))
# first_digit = num // 10
# last_digit = num % 10
# print('Число десятков = ', first_digit)
# print('Число единиц = ', last_digit)


"""Получение цифр"""
# # Для двузначного числа
# num = 17
# a = num % 10
# b = num // 10
# print(a) # 7
# print(b) # 1
#
# # # Для трёхзначного числа
# num = 754
# a = num % 10 # Последняя цифра
# b = (num % 100) // 10 # Серединная цифра
# c = num // 100 # Первая цифра
# print(a)
# print(b)
# print(c)

# # Алгоритм нахождения n-значных чисел
# Последняя цифра: (num % 10**1) // 100;
# Предпоследняя цифра: (num % 10**2) // 10**1;
# Предпредпоследняя цифра: (num % 10**3) // 10**2;
# .....
# Вторая цифра: (num % 10**n-1) // 10**n-2;
# Первая цифра: (num % 10**n) // 10**n-1.


"""В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная,
начинается с 1"""

# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20],
#     [21, 22, 23, 24],
#     [25, 26, 27, 28],
#     [29, 30, 31, 32],
#     [33, 34, 35, 36],
# ]
#
# number = 2
# found = False
# i = 0
# j = 0
#
# while i < len(lst):
#     while j < len(lst[i]):
#         if lst[i][j] == number:
#             found = True
#             print(f"{lst.index(lst[i+1])}")
#             break
#         j += 1
#     if found:
#         break
#     i += 1
#     j = 0
#
# if not found:
#     print(f'Число {number} не найдено.')


# # Решение ИИ
# Считываем номер места
# place_number = int(input("Введите номер места: "))
#
# # Проверяем, что номер места в допустимом диапазоне
# if 1 <= place_number <= 36:
#     # Вычисляем номер купе
#     coupe_number = (place_number - 1) // 4 + 1
#     print(coupe_number)
# else:
#     print("Номер места должен быть от 1 до 36.")


# Материалы Поколения Пайтон: https://disk.yandex.ru/d/phzgG4GoBFfNCg
# # Аргументы - конкретные значения, передаваемые функции при её вызове.

"""Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах в следующем формате:
<исходное кол-во минут> мин - это <полное кол-во часов> час <оставшееся кол-во минут> минут. Формат входных данных На вход программе подаётся целое число – количество минут.
Формат выходных данных Программа должна вывести текст в соответствии с условием задачи."""
# # Считываем количество минут
# total_minutes = int(input("Введите количество минут: "))
#
# # Вычисляем полное количество часов и оставшиеся минуты
# hours = total_minutes // 60  # Полное количество часов
# minutes = total_minutes % 60   # Оставшиеся минуты
#
# # Формируем и выводим результат
# print(f"{total_minutes} мин - это {hours} час {minutes} минут.")


"""Множественное присваивание"""
# Подходит, когда нужно 'обменять' значения переменных
# name1 = 'Gvido'
# name2 = 'Igor'
#
# name1, name2 = name2, name1
#
# print(name1)
# print(name2)

"""Вывести на экран астериски"""
# asterisk_count = [i for i in range(1, 7+1)]
# result = []
#
# for i in asterisk_count:
#     i = i * '*'
#     result.append(i)
#
# print("\n".join(result))

"""Напишите программу, которая находит полное число метров по заданному числу сантиметров."""
# sm = int(input())
# m = sm // 100
#
# print(m)

"""n школьников делят k k мандаринов поровну, неделящийся остаток остается в корзине. 
Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
Формат входных данных На вход программе подаются два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.
Формат выходных данных Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику, 
и количество мандаринов, которое останется в корзине, каждое на отдельной строке."""

# Вычисляем количество мандаринов на каждого школьника и остаток
# if n > 0:  # Проверяем, что количество школьников больше 0
#     mandarins_per_student = k // n  # Количество мандаринов на каждого школьника
#     remaining_mandarins = k % n      # Остаток мандаринов
# else:
#     mandarins_per_student = 0
#     remaining_mandarins = k
#
# # Выводим результаты
# print(mandarins_per_student)
# print(remaining_mandarins)

