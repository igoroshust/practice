"""Средние значения"""
# # ТЗ Наглядно: https://skrinshoter.ru/sUCsKOJZHAG
# import math
#
# a, b = float(input()), float(input())
#
# average_arif = (a + b) / 2
# average_geom = math.sqrt(a * b)
# average_garm = (a * b)*2 / (a + b)
# average_sqrt = math.sqrt(((a**2) + (b**2)) / 2)
#
# print(average_arif)
# print(average_geom)
# print(average_garm)
# print(average_sqrt)


"""Определить площадь круга и длину окружности по заданному радиусу"""
# # # ТЗ наглядно: https://skrinshoter.ru/sUCDGZox5LJ
# import math
#
# R = float(input())
#
# S = math.pi * (R**2)
# C = (2 * math.pi) * R
#
# print(S)
# print(C)



"""Найти Евклидово расстояние"""
# # ТЗ: https://skrinshoter.ru/sUCJIc6SOd5

# import math
#
# x1, x2, y1, y2 = float(input()), float(input()), float(input()), float(input())
#
# result = math.sqrt(
#     ((x1 - y1)**2) + ((x2 - y2)**2)
# )
#
# print(result)


"""Проверить наличие подстроки в строке"""
# string = input()
# day1 = 'суббота'
# day2 = 'воскресенье'
#
# if (day1 in string) or (day2 in string):
#     print('YES')
# else:
#     print('NO')

# # Упрощение кода
# print('YES' if 'суббота' in string or 'воскресенье' in string else 'NO')

"""Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет,
 можно ли из длин этих строк построить арифметическую прогрессию."""

# string1, string2, string3 = input(), input(), input()
#
# lengths = [len(string1), len(string2), len(string3)]
#
# lengths.sort()
#
# if 2 * lengths[1] == lengths[0] + lengths[2]:
#     print('YES')
# else:
#     print('NO')

"""Определение самого короткого и самого длинного города"""
# # Вариант 1
# city1, city2, city3 = input(), input(), input()
#
# cities = [city1, city2, city3]
#
# shortest_city = min(cities, key=len)
# longest_city = max(cities, key=len)
#
# print(shortest_city)
# print(longest_city)


# # Вариант 2
# cities = [input() for _ in range(3)]
#
# sorted_cities = sorted(cities, key=len)
#
# shortest_city = sorted_cities[0]
# longest_city = sorted_cities[-1]
#
# print(shortest_city)
# print(longest_city)






# # Вариант 3
# city1, city2, city3 = input(), input(), input()
#
# result = {len(city1): city1, len(city2): city2, len(city3): city3}
#
# # Находим максимальный и минимальный ключи
# max_key = max(result.keys())
# min_key = min(result.keys())
#
# # Получаем соответствующие значения
# max_value = result[max_key]
# min_value = result[min_key]
#
# print(min_value)
# print(max_value)


"""Определить манхеттенское расстояние между двух домов"""
# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
#
# formula = abs(p1 - q1) + abs(p2 - q2)
#
# print(formula)
#

"""Определить интересное трехзначеное число (наибольшее число - наименьшее = среднее)"""
# num = int(input())
#
# # Извлекаем цифры
# first_digit = num // 100
# middle_digit = (num // 10) % 10
# last_digit = num % 10
#
# # Создаем список цифр
# digits = [first_digit, middle_digit, last_digit]
#
# # Находим максимальное, минимальное и среднее значение
# max_digit = max(digits)
# min_digit = min(digits)
# middle_digit = sum(digits) - max_digit - min_digit  # Средняя цифра
#
# # Проверяем условие
# if (max_digit - min_digit) == middle_digit:
#     print('Число интересное')
# else:
#     print('Число неинтересное')


"""Напишите программу, которая упорядочивает три числа от большего к меньшему."""
# a, b, c = int(input()), int(input()), int(input())
#
# result = [a, b, c]
#
# sorted_result = sorted(result, reverse=True)
#
# for i in sorted_result:
#     print(i)

"""Определить наименьшее и наибольшее число в списке"""
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
#
# result = [a, b, c, d, e]
#
# print(f'Наименьшее число = {min(result)}')
# print(f'Наибольшее число = {max(result)}')


"""Дано положительное действительное число. Выведите его дробную часть."""
# # Например, число: 123123.456789 нужно вывести 0.456789

# num = input()
# dot = '.'
# result = []
#
# for i in num[::-1]:
#     if i != dot:
#         result.append(i)
#     elif i == dot:
#         print('0.' + ''.join(result[::-1]))
#         break

# # Решение ИИ
# num = float(input("Введите положительное число: "))
#
# # Вычисляем дробную часть
# fractional_part = num - int(num)
#
# # Выводим дробную часть
# print(fractional_part)



"""Вывести символ после точки"""
# # например, 221312312.55324234 (должно вывести 5)
# num = input()
# dot = '.'
#
# for i in num:
#     if i == dot:
#         a = num.index(i)
#         print(num[a + 1])


"""На вход программе подаётся число  n – количество собачьих лет.
Напишите программу, которая вычисляет возраст собаки в человеческих годах по следующему алгоритму:
в течение первых двух лет собачий год равен 10.5 человеческим годам, после этого каждый год собаки равен 4 человеческим годам"""

# dogs_age = float(input())
# result = 0
#
# if dogs_age <= 2:
#     result = dogs_age * 10.5
#     print(result)
# else:
#     result = ((dogs_age - 2) * 4) + (2 * 10.5)
#     print(result)


"""Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта"""
# Формула: https://skrinshoter.ru/sUBgAh7TbXO
# temp = float(input())
#
# tc = 5/9 * (temp - 32)
#
# print(tc)


"""Вычислить обратное число"""
# Считываем число с клавиатуры
# number = float(input("Введите число: "))
#
# # Проверяем, является ли число нулем
# if number == 0:
#     print("Обратного числа не существует")
# else:
#     # Вычисляем и выводим обратное число
#     inverse_number = 1 / number
#     print(f"Обратное число: {inverse_number}")


"""Напишите программу, определяющую время встречи двух старушек, идущих навстречу друг другу"""
# s = float(input())
# v1 = float(input())
# v2 = float(input())
#
# time_to_meet = s / (v1 + v2)
#
# print(time_to_meet)

"""Числа с плавающей точкой"""
# # 12345.67 => 1.234567 * 10^4, плавающая точка позволяет изменять масштаб числа
