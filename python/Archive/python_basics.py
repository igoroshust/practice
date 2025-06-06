# import math
# import random
# import time
# import redis
# # redis.

"""Напишите программу, которая развернёт число (тип int)"""
# def revert_int_option_1(num):
#     print('Option 1: Use reversed() method')
#     return int(''.join(list(reversed(str(num)))))
#
# def revert_int_option_2(num):
#     print('Option 2: Use slices')
#     return int(str(num)[::-1])
#
# print(revert_int_option_1(12345))
# print('')
# print(revert_int_option_2(12345))

"""Пример моржового оператора"""
# while (value := input("Введите что-нибудь: ") != ''):
#     print("Хорошо")
# else:
#     print("Пока!")

"""Подсчёт количества  чисел в строке"""
# string = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"
# count = 0
#
# for char in string:
#     if char.isdigit():
#         count += 1
#
# print(count) # Выведет: 158

"""Поэкспериментируйте с модулем time. Выведите в консоль текущее время, попробуйте вывести следующие данные:
только время;
только минуты;
только дату;
только месяц."""
# import time
# local_time = time.localtime()
# print(f"""Время: {local_time}
# Минуты: {local_time.tm_min}
# Дата: {local_time.tm_mday}
# Месяц: {local_time.tm_mon}""")




"""Напишите программу, которая заменяет в списке двузначные числа нулём"""
# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# for i in range(len(digs)):
#     if 10 <= abs(digs[i]) <= 99: # таким образом происходит проверка двузначного числа и при этом неважно, является оно положительным, или отрицательным
#         digs[i] = 0
# print(digs)

# # алтернативный вариант с помощью встроенной функции enumerate()
# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# for i, d in enumerate(digs):
#     if 10 <= abs(d) <= 99: # таким образом происходит проверка двузначного числа и при этом неважно, является оно положительным, или отрицательным
#         digs[i] = 0 # приравниваем полученное число к нулю
# print(digs)

"""Отображение ёлочки астерисков (от меньшего - к большему)"""
# for i in range(1, 7):
#     print('*' * i)

"""Вычисление факториала"""
# n = int(input("Введите целое число от 1 до 100: "))
# p = 1
#
# if 1 > n > 100:
#     print("Число введено неверно")
# else:
#     for i in range(1, n+1):
#         p *= i
#     print(f"Факториал {n}! = {p}")



"""Вычисление суммы: S = 1/2 + 1/3 + 1/4....1/1000"""
# S = 0
# for i in range(2, 1001):
#     S += 1/i
# print(S)

"""Изменение значений элементов списка (на ноль)"""
# d = [1, 2, 3, 4, 5]
# for i in [i**1 for i in range(len(d))]:
#     d[i] = 0
# print(d)

"""Произведение элементов списка"""
# d = [1, 2, 3, 4, 5]
# p = 1
# for x in d:
#     p *= x
# print(p)

"""Прерываем цикл while, когда нашли первое чётное значение в списке (без for)"""
# lst = [1, 3, 5, 19, 11, 23, 16]
# flFind = False
# i = 0
#
# while i < len(lst):
#     print(lst[i])
#     flFind = lst[i] % 2 == 0
#     if flFind:
#         break
#     i += 1
# print(f"Цикл завершён, чётное число {lst[i]}")

"""Проосим пользователя ввести значения и все нечетные значения будут суммироваться. Когда пользователь вводит число 0, программа перестаёт выполняться"""
# s = 0
# d = 1
#
# while d != 0:
#     d = int(input("Введние значение: "))
#     if d % 2 == 0:
#         continue
#     s += d # подсчитываем сумму текущих значений
#     print(f"s = {s}")


"""Запрос на введение пароля (с помощью while)"""
# pass_true = "password"
# ps = ""
#
# while ps != pass_true:
#     ps = input("Введите пароль: ")
#
# print("Вход в систему")


"""Выводим все числа последовательности, кратные 3"""
# N = 20
# i = 1
#
# while i <= N:
#     if i % 3 == 0:
#         print(i)
#     i += 1

"""Вывод отрицательной последовательности цифр"""
# N = -10
# i = -1
# while i >= N:
#     print(i)
#     i -= 1

"""Доступ к последнему элементу строки"""
# text = 'python1'
# print(text[len(text) - 1])

"""Поиск периметра треугольника"""
# a, b, c = map(int, input('Введите стороны треугольника: ').split())
# print(f"Периметр: {a + b + c}")


"""Поиск периметра прямоугольника (первый способ)"""
# length = float(input('Введите длину прямоугольника: '))
# width = float(input('Введите ширину прямоугольника: '))
# print(f"Периметр: {2 * (length + width)}")

"""Поиск периметра прямоугольника (второй способ)"""
# length, width = map(float, input('Введите две стороны прямоугольника: ').split())
# print(f"Периметр: {2 * (length + width)}")
# # важно: стороны вводим через пробел

"""Напишите программу, которая будет запрашивать у пользователя целочисленные значения
и сохранять их в виде списка. Индикатором окончания ввода значений должен служить ноль.
Затем программа должна вывести на экран все введенные пользователем числа (кроме нуля)
в порядке возрастания - по одному значению в строке. Используйте для сортировки либо метод
sort(), либо функцию sorted()."""

# num = int(input('введите число: '))
# lst = []
# while num != 0:
#     lst.append(num)
#     num = int(input('введите число: '))
# lst.sort()
# print(lst)
# for i in lst: # вывод в каждой новой строке
#     print(i)



"""Площадь и периметр прямоугольного треугольника. 
С клавиатуры вводятся длины двух катетов прямоугольного треугольника. 
Программа должна вычислять площадь и периметр этого треугольника 
и выводить полученные значения на экран"""
# AB = float(input('длина первого катета: '))
# AC = float(input('длина второго катета: '))
# BC = math.sqrt(AB**2 + AC**2)
# S = (AB * AC) / 2
# P = AB + AC + BC
# print('площадь треугольника: ', S)
# print('периметр: ', P)

"""Случайное целое в заданных границах. С клавиатуры вводятся границы числового диапазона.
 Получите случайное целое число в его пределах и выведите его на экран."""
# first_number = int(input('Введите первое число из диапазона: '))
# second_number = int(input('Введите второе число из диапазона: '))
# result = random.randint(first_number, second_number)
# print(result)

"""Сумма цифр трехзначного числа. Написать программу, 
котороая генерирует случайное трехзначное число и вычисляет сумму его цифр"""
# number = random.randint(100, 999)
# number = str(number)
# print(number)
# a = number[0]
# b = number[1]
# c = number[2]
# print(int(a) + int(b) + int(c))
#
# import random
# a = random.randint(100, 999)
# print(f'Случайное число: {a}')
# d1 = a // 100 # первая цифра
# d2 = a % 100 // 10 # вторая цифра
# d3 = a % 10 # третья цифра
# result = d1 + d2 + d3
# print(f'''
# Результат сложения: {d1} + {d2} + {d3} = {result}''')

"""Вычислить массу, плотность или объём.
Написать программу, которая вычисляет массу, плотность или объём, используя формулу m=Vp.
Пользователь выбирает, что он хочет вычислить и вводит два известных параметра."""
# show_choice = int(input('Что вы хотите вычислить? 1 - массу, 2 - плотность, 3 объём \n : '))
# if show_choice == 1:
#     d = float(input('укажите плотность: '))
#     v = float(input('укажите объём: '))
#     result = d * v
#     print('масса равна ' + str(round(result, 3)))
# elif show_choice == 2:
#     m = float(input('укажите массу: '))
#     v = float(input('укажите объём: '))
#     result = m / v
#     print('плотность равна ' + str(round(result, 3)))
# elif show_choice == 3:
#     m = float(input('укажите массу: '))
#     d = float(input('укажите плотность: '))
#     result = m / d
#     print('объём равен ' + str(round(result, 3)))
# else:
#     print('Только значения от 1 до 3')

# ещё один вариант
# a = int(input('Введите параметр массы: '))
# b = int(input('Введите параметр плотности: '))
# c = int(input('Введите параметр объёма: '))
# d = int(input('Что вы хотите вычислить? 1 - массу, 2 - плотность, 3 объём \n : '))
#
# mass = b * c
# density = a / c # плотность
# volume = a / b # объём
#
# if d == 1:
#     print(f"масса равна {round(mass, 3)}")
# elif d == 2:
#     print(f"плотность равна {round(density, 3)}")
# elif d == 3:
#     print(f"объём равен {round(volume, 3)}")
# else:
#     print('Только значения от 1 до 3')


"""Калькулятор.
Написать программу, которая выполняет над двумя вещественными числами одну из четырех
арифметических операций (сложение, вычитание, умножение или деление).
Числа и операцию вводит пользователь."""
# first_number = float(input('Введите первое число: '))
# second_number = float(input('Введите второе число: '))
#
# show_choice = int(input('Выберите операцию: \n [1] - сложение \n [2] - вычитание \n [3] - умножение \n [4] - деление \n : '))
#
# if show_choice == 1:
#     print('Результат сложения: ' + str(round(first_number + second_number)))
# elif show_choice == 2:
#     print('Результат вычитания: ' + str(round(first_number - second_number)))
# elif show_choice == 3:
#     print('Результат умножения: ' + str(round(first_number * second_number)))
# elif show_choice == 4:
#     print('Результат деления: ' + str(round(first_number / second_number)))
# else:
#     print('Только значения от 1 до 4')

"""Количество разрядов числа.
Напишите цикл, который считает количество разрядов введённого с клавиатуры числа."""

"""Найти произведение элементов списка"""
# data = [1, 2, 3, 4, 5]
# mod = 1 # начинаем с 1, потому что при умножении на ноль будет ноль
# for item in data:
#     mod *= item
# print(mod)

"""Напишите программу, которая в последовательности целых чисел определяет максимальное число, кратное 5."""
# lst = [3, 125, 10, 25, 12]
# lst2 = []
# for i in lst:
#     if i % 5 == 0:
#         lst2.append(i)
# print(max(lst2))

# num = int(input('Введите целое число: '))
# lst = []
# maxs = 0
#
# while num != maxs:
#     if num % 5 == maxs and num > maxs:
#         lst.append(num)
#     num = int(input('Введите целое число: '))
# print(f'max value: {max(lst)} \n {max(lst)} % 5 = {max(lst) % 5}')