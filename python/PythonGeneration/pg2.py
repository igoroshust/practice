"""Имеется 100 рублей. Сколько быков, коров и телят можно купить на все эти деньги, если плата за быка – 10 рублей,
за корову – 5 рублей, за телёнка – 0.5 рубля и надо купить 100 голов скота?"""
# for B in range(1, 11):
#     for K in range(1, 21):
#         for T in range(1, 200):
#             if B*10 + K*5 + T*0.5 == 100:
#                 if B + K + T == 100:
#                     print(B, K, T)

"""Вывести пирамиду цифр"""
# num = int(input())
# index = 1
#
# for i in range(1, num+1):
#     print(i * str(i))


"""Равнобедренный треугольник"""
# n = int(input())
#
# # Верхняя часть треугольника
# for i in range(1, n // 2 + 2):  # От 1 до n//2 + 1 включительно
#     print('*' * i)
#
# # Нижняя часть треугольника
# for i in range(n // 2, 0, -1):  # От n//2 до 1
#     print('*' * i)


"""Вевести число в формате num num num - num раз"""
# num = int(input())
#
# for i in range(num):  # Внешний цикл для строк
#     for j in range(3):  # Внутренний цикл для трех чисел в строке
#         print(num, end=' ')  # Печатаем число num с пробелом
#     print()  # Печатаем новую строку после завершения внутреннего цикла


"""Вывести звёздочки от меньшей к большей с помощью вложенных циклов"""
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


"""Вложенные циклы"""
# for i in range(3):
#     for j in range(3):
#         print(i, j)


"""Вывести числа от 1 до num, исключив значения danger_range"""
# num = int(input())
#
# danger_range_1 = [i for i in range(5, 9+1)]
# danger_range_2 = [i for i in range(17, 37+1)]
# danger_range_3 = [i for i in range(78, 87+1)]
#
# result = []
#
# for i in range(1, num+1):
#     if (i in danger_range_1) or (i in danger_range_2) or (i in danger_range_3):
#         pass
#     else:
#         result.append(str(i))
#
# print('\n'.join(result))

"""Найти наименьший делитель (кроме 1)"""
# num = int(input())
# division = 2
#
# while True:
#     if num % division == 0:
#         print(division)
#         break
#     else:
#         division += 1


"""Дано натуральное число.
Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию"""
# num = input()
# reverse_result = num[::-1]
#
# # Проверяем, упорядочены ли цифры по неубыванию
# for i in range(len(reverse_result) - 1):
#     if reverse_result[i] > reverse_result[i + 1]:
#         print('NO')
#         break
# else:
#     print('YES')

"""Определить, все ли значения списка равны"""
# # Решение ИИ
# num = input()
#
# if len(set(num)) == 1:
#     print('YES')
# else:
#     print('NO')


# # Моё решение:
# num = input()
# result = []
#
# for i in num:
#     result.append(i)
#
# st = set(result)
#
# if len(st) >= 2:
#     print('NO')
# else:
#     print('YES')


"""Дано натуральное число. Напишите программу, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры"""
# num = input()
# result = []
# mult = 1
#
# for i in num:
#     result.append(int(i))
#
# for k in result:
#     mult *= int(k)
#
#
# sum_digit = sum(result)
# len_digit = len(result)
# average = sum(result) / len(result)
# min_max_sum = result[0] + result[-1]
#
#
# print(
#     sum_digit,
#     len_digit,
#     mult,
#     average,
#     result[0],
#     min_max_sum,
#     sep='\n',
# )


"""Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке"""
# num = input()
# result = [num[::-1]]
# test = ''.join(result)
#
# for i in test:
#     print(i)


"""Пример перебора цифр числа в обратном порядке"""
# num = 123456789
# total = 0
# while num != 0:
#     last_digit = num % 10
#     if last_digit > 4:
#         total += 1
#
#     num = num // 10 # Движение справа-налево по числу
#
# print(total)


"""Программа, определяющая, есть ли в числе цифра 7"""
# num = int(input())
# has_seven = False # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num //= 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')


"""Получение цифр шестизначного числа"""
# number = 123456
# n_1 = number // 100000
# n_2 = (number // 10000) % 10
# n_3 = (number // 1000) % 10
# n_4 = (number // 100) % 10
# n_5 = (number // 10) % 10
# n_6 = number % 10


"""Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево.
К тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами
1, 5, 10, 25. Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку"""
# # Решение ИИ
# count = int(input())
# monets = 0
#
# # Список номиналов монет в порядке убывания
# denominations = [25, 10, 5, 1]
#
# for denomination in denominations:
#     if count == 0:
#         break
#     monets += count // denomination # Количество монет данного номинала
#     count %= denomination # Остаток после использования монет данного номинала
#
# print(monets)


# # Моё решение
# count = int(input())
# monets = 0
#
# while count != 0:
#     if count - 25 >= 0:
#         count -= 25
#         monets += 1
#     elif (count - 10 >= 0) and (count - 25 < 0):
#         count -= 10
#         monets += 1
#     elif (count - 5 >= 0) and (count - 25 < 0) and (count - 10 < 0):
#         count -= 5
#         monets += 1
#     elif (count - 1 >= 0) and (count - 5 < 0) and (count - 25 < 0) and (count - 10 < 0):
#         count -= 1
#         monets += 1
#
# print(monets)


# while (count - 25) >= 0:
#     count -= 25
#     monets += 1
#
#     print(count)
#     print(monets)


"""Вывести количество пятёрок из списка"""
# # Решение ИИ
# count_of_fives = 0
#
# while True:
#     try:
#         a = int(input())
#
#         if a <= 0 or a > 5:
#             break
#
#         if a == 5:
#             count_of_fives += 1
#
#     except ValueError:
#         continue
#
# print(count_of_fives)

# # Моё решение
# grades = []
#
# while True:
#     a = input("Введите оценку (0 для удаления пятерок, любое другое число для выхода): ")
#
#     try:
#         num = int(a)  # Пробуем преобразовать ввод в целое число
#
#         if 0 < num <= 5:
#             grades.append(num)  # Добавляем как целое число
#         elif num == 0:
#             # Удаляем все пятерки из списка
#             grades = [i for i in grades if i != 5]
#             print("Оценки после удаления пятерок:", grades)
#         else:
#             result = ''.join(map(str, grades))  # Преобразуем оценки обратно в строки для вывода
#             print("Количество пятерок:", result.count('5'))
#             break
#     except ValueError:
#         print("Пожалуйста, введите корректное целое число.")


"""Вывод суммы положительных чисел, поданных на вход. Выход из программы при введённых отрицательных числах"""
# numbers = []
#
# while True:
#     a = input()
#
#     if a == '':  # Проверка на пустую строку
#         print("Выход из программы.")
#         break
#
#     try:
#         num = int(a)  # Пробуем преобразовать ввод в целое число
#         if num >= 0:
#             numbers.append(num)
#         else:
#             print(sum(numbers))
#             break
#     except ValueError:
#         print("Пожалуйста, введите корректное целое число.")

"""На вход программе подаётся последовательность целых чисел делящихся на 7, каждое число на отдельной строке. 
Концом последовательности является любое число, не делящееся на 7"""
# # Моё решение
# numbers = []
# a = None
#
# while True:
#     a = input()
#     if int(a) % 7 == 0:
#         numbers.append(a)
#     else:
#         print('\n'.join(numbers))
#         break

# # Решение ИИ
# numbers = []
# while True:
#     a = input(': ')
#
#     try:
#         num = int(a)
#         if num % 7 == 0:
#             numbers.append(a)
#         else:
#             print('\n'.join(numbers))
#             break
#
#     except ValueError:
#         print('Пожалуйста, введите корректное целое число.')
#         continue


"""Вывести последовательность значений списка до введения стоп-слова"""
# words = []
# stop_words = {'хватит', 'стоп', 'достаточно'}
#
# while True:
#     a = input().strip().lower()
#     if a in stop_words:
#         print(len(words))
#         break
#     else:
#         words.append(a)

"""Вывести элементы последовательности пока a != 'КОНЕЦ'"""
# words = []
#
# while True:
#     a = input()
#     if a.lower() == 'конец':
#         break
#     words.append(a)
#
# print('\n'.join(words))




"""Последовательности Фибоначчи"""
# # Считываем натуральное число n
# n = int(input("Введите количество членов последовательности Фибоначчи (n ≤ 100): "))
#
# # Инициализация списка для хранения чисел Фибоначчи
# fibonacci_sequence = []
#
# # Генерация последовательности Фибоначчи
# for i in range(n):
#     if i == 0 or i == 1:
#         fibonacci_sequence.append(1)  # Первые два числа Фибоначчи
#     else:
#         next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
#         fibonacci_sequence.append(next_number)
#
# # Вывод последовательности, разделенной пробелами
# print(" ".join(map(str, fibonacci_sequence)))

"""Проверить, все ли числа являются чётными в последовательности"""
# Считываем 10 целых чисел
# numbers = [int(input()) for _ in range(10)]
# 
# # Проверяем, являются ли все числа четными
# all_even = True  # Флаг, который будет указывать, все ли числа четные
# 
# for i in numbers:
#     if i % 2 != 0:  # Если число нечетное
#         all_even = False  # Устанавливаем флаг в False
#         break  # Прерываем цикл, так как мы уже знаем, что не все числа четные
# 
# # Выводим результат
# if all_even:
#     print('YES')
# else:
#     print('NO')

"""Вывести два самых больших числа в последовательности"""
# n = int(input())
# 
# numbers = [int(input()) for i in range(n)]
# 
# max_number_one = max(numbers)
# numbers.remove(max_number_one)
# max_number_two = max(numbers)
# 
# print(max_number_one)
# print(max_number_two)


"""Напишите программу вычисления знакочередующейся суммы"""
# # Пример: https://skrinshoter.ru/sUDahHc1rZi
# Ввод натурального числа n
# n = int(input())
#
# # Инициализация переменной для хранения суммы
# result = 0
#
# # Вычисление знакочередующейся суммы
# for i in range(1, n + 1):
#     if i % 2 == 0:  # Если i четное
#         result -= i
#     else:           # Если i нечетное
#         result += i
#
# # Вывод результата
# print(result)


"""Вывести сумму всех делителей числа"""
# n = int(input())
# division = []
#
# for i in range(1, n+1):
#     if n % i == 0:
#         division.append(i)
#
# sum_division = sum(division)
# print(sum_division)

"""Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел."""
# # Первый вариант
# from functools import reduce
#
# numbers = [int(input()) for i in range(10)]
# multiply = []
# mult = 1
#
# for i in numbers:
#     if i != 0:
#         multiply.append(i)
#     elif i == 0:
#         pass
#
# for k in multiply:
#     mult *= k
#
# print(mult)

# # Вариант ИИ
# from functools import reduce
#
# numbers = [int(input()) for _ in range(10)]
# mult = reduce(lambda x, y: x * y if y != 0 else x, numbers, 1)
# print(mult)


"""Высчитать факториал"""
# # Первый вариант
# import math
#
# print(math.factorial(int(input())))

# # Второй вариант
# n = int(input())
# total = 1
#
# for i in range(1, n+1):
#     total *= i
#
# print(total)



""" Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), квадрат которых оканчивается на
2, 5 или 8"""
# n = int(input())
#
# square = []
#
# for i in range(1, n+1):
#     if (i**2 % 10 == 2) or (i**2 % 10 == 5) or (i**2 % 10 == 8):
#         square.append(i)
#
# square_sum = sum(square)
# print(square_sum)



"""На вход программе подаётся натуральное число n.
Напишите программу, которая вычисляет значение выражения"""
# # Формула: https://skrinshoter.ru/sUDHiBVIhnM
# import math
#
# n = int(input())
# result = [1]
#
# for count in range(2, n+1):
#     result.append(1/count)
#
# sum_result = sum(result)
#
# output = sum_result - math.log(n)
#
# print(output)

"""На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
Напишите программу, которая подсчитывает сумму введённых чисел (не включая само число n)."""
# n = int(input())
#
# n_sum = [sum(int(input()) for i in range(n))]
#
# print(n_sum[0])

"""Подсчёт количества чисел в диапазоне от a до b (включительно), куб которых оканчивается на 4 или 9"""
# a = int(input())
# b = int(input())
#
# cubes = 0
#
# for i in range(a, b+1):
#     if (i**3 % 10 == 4) or (i**3 % 10 == 9):
#         cubes += 1
#
# print(cubes)

"""Найти наибольшее число"""
# largest = 0
# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
#
# print('Наибольшее число равно', largest)


"""Определение числа - простое или сложное"""
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


"""Определить, сколько чисел больше 10"""
# counter = 0
#
# for _ in range(20):
#     if _ > 10:
#         counter += 1
#
# print(f'{counter} чисел больше 10')



"""Вывести таблицу умножения"""
# number = int(input())
# count = 1
#
# for i in range(1, 10+1):
#     print(f'{number} x {count} = {number*count}')
#     count += 1


"""Вывести все целые числа от m до n включительно в порядке возрастания, если m < n, иначе в обратном порядке"""
# m = int(input()) # 10
# n = int(input()) # 5
#
# if m < n:
#     for i in range(m, n+1):
#         print(i)
# elif m > n:
#     for i in range(m, n-1, -1):
#         print(i)
# elif m == n:
#     print(m)



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
