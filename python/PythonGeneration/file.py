"""Переставить min и max местами"""
# # Моё решение
# entry = list(map(int, input().split()))
#
# min_entry = min(entry)
# max_entry = max(entry)
#
# t1 = entry.index(min_entry)
# t2 = entry.index(max_entry)
#
# entry[t1], entry[t2] = entry[t2], entry[t1]
#
# print(' '.join(map(str, entry)))


# # Решение ИИ
# entry = list(map(int, input().split()))
#
# min_index = 0
# max_index = 0
#
# # Находим индексы min и max
# for i in range(1, len(entry)):
#     if entry[i] < entry[min_index]:
#         min_index = i
#     elif entry[i] > entry[max_index]:
#         max_index = i
#
# # Переставляем min и max местами
# entry[min_index], entry[max_index] = entry[max_index], entry[min_index]
#
# # Выводим результат
# print(' '.join(map(str, entry)))



"""Работа с методами списков"""
# # Описание ТЗ: https://skrinshoter.ru/sUiZqX6qyVv
# # Моё решение
# numbers = [8, 9, 10, 11]
#
# numbers[1] = 17
# numbers.extend([4, 5, 6]) # Добавляем 4 5 6 в конец списка
# numbers.pop(0)
# numbers += numbers # Удаваиваем список
# numbers.insert(3, 25)
#
# print(numbers)



"""Прочитать входные данные и создать из них список чисел"""
# numbers = list(map(int, input().split())) # 1 2 3 4 5
# print(numbers) # [1, 2, 3, 4, 5]


"""Определить количество совпадающих пар"""
# # Решение ИИ

# Читаем входные данные и создаём список чисел
# numbers = list(map(int, input().split()))
#
# # Инициализируем переменную для подсчёта пар
# count = 0
#
# # Проходим по каждому уникальному элементу
# for i in set(numbers):
#     # Подсчитываем количество вхождений текущего элемента
#     occurrences = numbers.count(i)
#     # Если вхождений больше 1, добавляем количество пар
#     if occurrences > 1:
#         count += occurrences * (occurrences - 1) // 2
#
# print(count)




"""Вставить сепаратор между символами строки"""
# # Моё решение
# string = [i for i in input()]
# separator = input()
#
# results = []
#
# for i in string:
#     results.append(i)
#     results.append(separator)
#
# print(''.join(results[:-1]))

# # Решение ИИ
# string = input()
# separator = input()
#
# # Используем join для добавления разделителя между символами
# result = separator.join(string)
#
# print(result)



"""Проверить корректность IP-адреса"""
# # Моё решение
# def correct_ip(string):
#
#     flag = ''
#
#     for i in string:
#         if int(i) <= 255:
#             flag = 'ДА'
#         else:
#             flag = 'НЕТ'
#             break
#
#     return flag
#
#
# print(correct_ip(input().split('.')))

# string = ['ДА' if (int(i) <= 255) for i in input().split('.') else 'НЕТ']
# print(string)

# # Решение ИИ
# def correct_ip(string):
#     # Проверяем, что строка состоит из 4 частей
#     parts = string.split('.')
#     if len(parts) != 4:
#         return 'НЕТ'
#
#     for part in parts:
#         # Проверяем, что часть является числом и в диапазоне от 0 до 255
#         if not part.isdigit() or not (0 <= int(part) <= 255):
#             return 'НЕТ'
#         # Проверяем, что часть не имеет ведущих нулей (например, 01)
#         if len(part) > 1 and part[0] == '0':
#             return 'НЕТ'
#
#     return 'ДА'
#
# print(correct_ip(input()))


# # Решение ИИ в одной строке
# def correct_ip(string):
#     return 'ДА' if len(parts := string.split('.')) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 and (len(part) == 1 or part[0] != '0') for part in parts) else 'НЕТ'
#
# print(correct_ip(input()))

"""Вывести количество плюсов"""
# # Моё решение
# def return_plus(text):
#
#     formatted_text = text.split()
#     asterisks = []
#
#     for i in formatted_text:
#         asterisks.append("+" * int(i))
#
#     return '\n'.join(asterisks)
#
# print(return_plus(input()))

# # Решение ИИ
# def return_plus(text):
#     return '\n'.join('+' * int(i) for i in text.split())
#
# print(return_plus(input(': ')))



"""Вывести разделы адресной строки"""
# Например: C:\Windows\Users.... вывести C: WINDOWS USERS
# def result_paths(path):
#
#     result = '\n'.join(path.split('\\'))
#
#     return result
#
# print(result_paths(input()))

"""Вывести ФИО"""
# # Моё решение
# fio = input()
#
# formatted_fio = fio.split()
#
# print(''.join(f'{formatted_fio[0][0]}.{formatted_fio[1][0]}.{formatted_fio[2][0]}.'))


# # Решение ИИ
# fio = input("Введите ФИО: ")
#
# formatted_fio = fio.split()
# initials = []
#
# for name in formatted_fio:
#     initials.append(name[0] + '.')
#
# print(' '.join(initials))


"""Вывести слова предложения построчно"""
# print((text := '\n'.join(input().split())))


"""Преобразовать строку из CamelCase в snake_case"""
# def convert_to_python_case(text: str) -> str:
#
#     results_string = []
#
#     for i in text:
#         if i.isupper():
#             if results_string: # Если это не первый символ, добавляем _
#                 results_string.append('_')
#             results_string.append(i.lower())
#         else:
#             results_string.append(i)
#
#     return ''.join(results_string)
#
# print(
#     convert_to_python_case(input())
# )

"""Корректность скобочной последовательности"""
# def is_correct_bracket(text):
#     balance = 0 # Счётчик для отслеживания баланса скобок
#
#     for char in text:
#         if char == '(':
#             balance += 1 # Увеличиваем счётчик для открывающейся скобки
#         elif char == ')':
#             balance -= 1 # Уменьшаем счётчик для закрывающей скобки
#
#         if balance < 0: # Если баланс становится отрицательным, значит, есть лишняя скобка
#             return 0
#
#     # В конце баланс должен быть равен нулю
#     return balance == 0
#
# print(
#     is_correct_bracket(input())
# )



"""Проверка значений в строке"""
# # Задача: https://skrinshoter.ru/sUhc2hDtCgF

# def is_prime(num):
#     """Проверка, является ли число простым"""
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def is_palindrome(text: str) -> bool:
#     """Проверка, является ли число палиндромом"""
#     # Создаём таблицу перевода для удаления нежелательных символов
#     translation_table = str.maketrans('', '', '.,!?-')
#
#     # Форматируем текст: приводим к нижнему регистру, удаляем пробелы и нежелательные символы
#     formatted_text = text.lower().replace(' ', '').translate(translation_table)
#
#     return formatted_text == formatted_text[::-1]
#
# def is_valid_password(password):
#     """Проверяем валидацию пароля"""
#
#     # Проверяем количество двоеточий
#     if password.count(':') != 2:
#         return False
#
#     l = password.find(':')
#     r = password.rfind(':')
#
#     count = 0
#     for i in password:
#         if i == ':':
#             count += 1
#
#     first_number = password[:l]
#     second_number = password[l+1:r]
#     third_number = password[r+1:]
#
#
#     if is_palindrome(first_number) and is_prime(int(second_number)) and (int(third_number) % 2 == 0):
#         return True
#     else:
#         return False
#
# print(
#     is_valid_password('1221:101:22:0000')
# )



"""Предикат-палиндром с заменой знаков препинания"""
# def is_palindrome(text: str) -> bool:
#     # Создаём таблицу перевода для удаления нежелательных символов
#     translation_table = str.maketrans('', '', '.,!?-')
#
#     # Форматируем текст: приводим к нижнему регистру, удаляем пробелы и нежелательные символы
#     formatted_text = text.lower().replace(' ', '').translate(translation_table)
#
#     return formatted_text == formatted_text[::-1]
#
# print(
#     is_palindrome(input())
# )



"""Вернуть True, если строки равны и отличаются на 1 символ"""
# def is_one_away(word1, word2):
#     # Проверяем, равны ли длины слов
#     if len(word1) != len(word2):
#         return False
#
#     difference_count = 0
#
#     # Итерируемся по символам обоих слов
#     for char1, char2 in zip(word1, word2):
#         if char1 != char2:
#             difference_count += 1
#             # Если различий больше 1, возвращаем False
#             if difference_count > 1:
#                 return False
#
#     # Возвращаем True, если различий ровно 1
#     return difference_count == 1
#
# print(is_one_away(input(), input()))



"""Пример распаковки кортежей с помощью zip()"""
# zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
# list1, list2 = zip(*zipped)
# print(list1)
# print(list2)



"""Проверить корректность пароля: длина менее 8 символв, заглавная буква, строчная буква, цифра"""
# # Решение ИИ
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#
#     has_upper = False
#     has_lower = False
#     has_digit = False
#
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#
#         if has_upper and has_lower and has_digit:
#             return True
#
#     return False
#
# print(is_password_good(input("Введите пароль: ")))


# # Моё решение
# def is_password_good(password):
#
#     isupper_count = 0
#     islower_count = 0
#     isdigit_count = 0
#
#     if len(password) >= 8:
#         for i in password:
#             if i.isupper():
#                 isupper_count += 1
#             elif i.islower():
#                 islower_count += 1
#             elif i.isdigit():
#                 isdigit_count += 1
#
#     if isupper_count and islower_count and isdigit_count:
#         return True
#     else:
#         return False
#
# print(is_password_good(input()))





"""Корни уравнения"""
# import math
#
# def solve(a, b, c):
#     # Вычисляем дискриминант
#     D = b**2 - 4*a*c
#
#     # Находим корни в зависимости от значения дискриминанта
#     if D > 0:
#         x1 = (-b + math.sqrt(D)) / (2 * a)
#         x2 = (-b - math.sqrt(D)) / (2 * a)
#         return f"{min(x1, x2)} {max(x1, x2)}"  # Возвращаем корни в порядке возрастания, разделенные пробелом
#     elif D == 0:
#         x = -b / (2 * a)
#         return f"{x} {x}"  # Возвращаем двойной корень дважды
#
# # Пример использования
# print(solve(int(input()), int(input()), int(input())))


"""Вернуть длину окружности и площадь круга"""
# from math import pi
#
# def get_circle(r):
#     return 2 * pi * r, pi * (r ** 2)
#
# # Получаем значения из функции
# circumference, area = get_circle(float(input()))
#
# print(circumference, area)


"""Найти середину отрезка"""
# def get_middle_point(x1, y1, x2, y2):
#     return (x_1 + x_2) / 2, (y_1 + y_2) / 2
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


"""Написать функцию, которая возвращает первое простое число больше поданого на вход"""
# def is_prime(num):
#
#     lst = [i for i in range(1, num + 1)]
#     count = 0
#
#     for i in lst:
#         if num % i == 0:
#             count += 1
#
#     if count == 2:
#         return True
#     else:
#         return False
#
#
# def get_next_prime(num):
#     current = num + 1
#
#     while True:
#         if is_prime(current):
#             return current
#         current += 1
#
# print(get_next_prime(int(input())))



"""Напишите, пожалуйста, программу (функцию или метод), которая будет печатать числа от 0 до 1000, кратные трём и не кратные пяти, сумма цифр в которых меньше десяти."""
# Моё решение
# def show_numbers():
#
#     numbers = [i for i in range(1001) if i % 3 == 0 and i % 5 != 0]
#     correct_result = []
#
#     for i in numbers:
#         if len(str(i)) < 2: # Подразумевается, что числа меньше 10 по умолчанию попадают в correct_result
#             correct_result.append(i)
#
#         elif len(str(i)) == 2: # Проверяем условие для двухзначных чисел
#             if int(str(i)[0]) + int(str(i)[1]) < 10:
#                 correct_result.append(i)
#
#         elif len(str(i)) == 3: # Проверяем условие для трёхзначных чисел
#             if int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) < 10:
#                 correct_result.append(i)
#
#     return correct_result
#
# result = show_numbers()
# print(result)


# Решение ИИ
# def sum_of_digits(n):
#     return sum(int(digit) for digit in str(n))
#
# def show_numbers():
#     correct_result = []
#     for i in range(1001):
#         if i % 3 == 0 and i % 5 != 0 and sum_of_digits(i) < 10:
#             correct_result.append(i)
#     return correct_result
#
# result = show_numbers()
# print(result)

"""Определить, является ли число простым"""
# # Моё решение
# def is_prime(num):
#
#     lst = [i for i in range(1, num + 1)]
#     count = 0
#
#     for i in lst:
#         if num % i == 0:
#             count += 1
#
#     if count == 2:
#         return True
#     else:
#         return False
#
# print(is_prime(int(input())))

# # Решение ИИ
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# print(is_prime(int(input())))

# # Решение ИИ (sympy)
# from sympy import isprime # pip install sympy
# print(isprime(int(input())))

# # Решение ИИ (any). any() - проверяет, что в итерируемом объекте есть хотя бы 1 True и возвращает True, иначе False
# def is_prime(num):
#     if num < 2:
#         return False
#     return not any(num % i == 0 for i in range(2, int(num**0.5) + 1))
#
# print(is_prime(29))
# print(is_prime(30))


"""Определить невырожденный треугольник"""
# # Моё решение
# def is_valid_triangle(side1, side2, side3):
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         return True
#     else:
#         return False
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# # Решение ИИ
# def is_valid_triangle(a, b, c):
#     return (a + b > c) and (a + c > b) and (b + c > a)
#
# # Вызываем функцию
# print(is_valid_triangle(int(input()), int(input()), int(input())))




"""Объединение строк в отсортированный список"""
# # Моё решение
# def merge():
#     n = int(input())
#     combined = []
#
#     for _ in range(n):
#         text = input().split()
#         for i in text:
#             combined.append(int(i))
#
#     combined.sort()
#     return ' '.join(map(str, combined))
#
# print(merge())

# # Решение ИИ
# def merge():
#     n = int(input())
#
#     # Используем генератор для чтения и преобразования входных данных
#     combined = (int(i) for _ in range(n) for i in input().split())
#
#     # Сортируем и объединяем в строку
#     return ' '.join(map(str, sorted(combined)))
#
# print(merge())



"""Слияние списоков"""
# # Решение ИИ
# def merge(list1, list2):
#     # Объединяем списки и преобразуем элементы в целые числа
#     combined = [int(x) for x in list1 + list2]
#     # Сортируем объединённый список
#     combined.sort()
#     return combined
#
# print(merge(input('Введите первый список: ').split(), input('Введите второй список: ').split()))


# # Моё решение
# def merge(list1, list2):
#     results = list1 + list2
#     res = list(map(int, results))
#     res.sort()
#     return res
#
# print(merge(input().split(), input().split()))



"""Вывести индексы совпадений в строке"""
# # Моё решение
# def find_all(target, symbol):
#     words = []
#
#     for index, char in enumerate(target):
#         if char.lower() == symbol.lower():
#             words.append(index)
#
#     return words
#
# print(find_all(input(), input()))


# # Решение ИИ
# def find_all(target_string, target_symbol):
#     return [index for index, char in enumerate(target_string) if char.lower() == target_symbol.lower()]
#
# print(find_all('abracadabra', 'a'))


"""Вернуть список всех делителей числа"""
# # Моё решение
# def get_factors(num):
#     divisions = []
#     divide = [i for i in range(1, num+1)]
#
#     for i in divide:
#         if num % i == 0:
#             divisions.append(i)
#
#     return divisions
#
# print(
#     get_factors(1)
# )

# # Решение ИИ
# def get_factors(num):
#     divisions = []
#
#     for i in range(1, int(num**0.5) + 1):
#         if num % i == 0:
#             divisions.append(i)
#             if i != num // i: # Добавляем парный делитель, если он не равен i
#                 divisions.append(num // i)
#
#     divisions.sort()
#     return divisions
#
# print(get_factors(1))


"""Определить количество дней в месяце"""
# # Решение ИИ
# def get_days(number):
#     sequence = {
#         1: 31,
#         3: 31,
#         5: 31,
#         7: 31,
#         8: 31,
#         10: 31,
#         12: 31,
#         4: 30,
#         6: 30,
#         9: 30,
#         11: 30,
#         2: 28,
#     }
#
#     result = sequence.get(number)
#
#     if result is None:
#         print('Некорректное значение')
#     return result
#
# print(get_days(int(input())))


# # Моё решение
# def get_days(number):
#     result = None
#
#     if number in (1, 3, 5, 7, 8, 10, 12):
#         result = 31
#     elif number in (4, 6, 9, 11):
#         result = 30
#     elif number == 2:
#         result = 28
#     else:
#         print('Некорректное значение')
#
#     return result
#
# print(get_days(int(input())))



"""Преобразовать расстояние из киллометров в мили"""
# def convert_to_miles(km):
#     if len(str(km * 0.6214)) <= 7:
#         return km * 0.6214
#     else:
#         return round(km * 0.6214, 3)
#
# print(convert_to_miles(1))
# print(convert_to_miles(5))
# print(convert_to_miles(10))



"""Вывести сумму чисел введённого числа"""
# # Решение ИИ
# def print_digit_sum(num: int) -> None: # None указывает, что функция ничего не возвращает.
#     # Вычисляем сумму цифр с помощью генератора
#     digit_sum = sum(int(i) for i in str(num))
#     print(digit_sum)
#
# # Запрос ввода от пользователя
# num = int(input('Введите число: '))
# print_digit_sum(num)


# # Моё решение
# def print_digit_sum(num):
#     lst = []
#     for i in str(num):
#         lst.append(int(i))
#     print(sum(lst))
#
# print_digit_sum(7)


"""Вывести ФИО"""
# def print_fio(name: str, surname: str, patronymic: str) -> str:
#     print(
#         surname[0].upper(), name[0].upper(), patronymic[0].upper(),
#         sep=''
#     )
#
# print_fio('игорь', 'ошуст', 'неизвестно')



"""Реализуйте звёздный треугольник"""
# def draw_triangle(fill, base):
#     # Вывод верхней части треугольника
#     for i in range(1, base // 2 + 2): # (base // 2) - целочисленное деление основания на 2. Получаем целое число, равное половине основания.
#         # Добавляем 2, чтобы включить в диапазон не только половину, но и самую верхнюю строку, содержащую `5` символов (в случае с 9)
#         # Получается диапазон от 1 до 5 (включительно).
#         print(fill * i)
#
#     # Вывод нижней части треугольника
#     for i in range(base // 2, 0, -1): # (base // 2) - начинаем с половины основания, что соотстветвует количеству символовв первый строке нижней части треугольника.
#         # 0 - продолжаем цикл до 1 включительно, поэтому указываем 0, которое не включается в диапазон.
#         # -1 - уменьшаем i на 1 при каждой итерации
#         print(fill * i)
#
# # Пример вызова функции
# draw_triangle('*', 9)


"""Вывести лесенку звёздочек от 1 до 10"""
# # Моё решение
# def draw_triangle(ast, count):
#     while count <= 10:
#         print(ast * count)
#         count += 1
#
# draw_triangle('*', 1)

# # Решение ИИ
# def draw_triangle(symbol, height):
#     """Рисуем треугольник"""
#     for count in range(1, height + 1):
#         print(symbol * count)
#
# # Вызов функции с высотой 10
# draw_triangle('*', 10)


"""Сделать прямоугольник с вырезом"""
# def draw_box(width, height):
#     # Печатаем верхнюю границу
#     print('*' * width)
#
#     # Печатаем боковые границы
#     for _ in range(height - 2):
#         print(f'*{(width - 2) * ' '}*')
#         # print('*' + ' ' * (width - 2) + '*')
#
#     # Печатаем нижнюю границу
#     print('*' * width)
#
# # Вызов функции
# draw_box(10, 14)



"""Поисковый запрос"""
# n = int(input())
# lines = []
#
# # Считываем строки
# for _ in range(n):
#     line = input()
#     lines.append(line)
#
# # Считываем поисковый запрос
# query = input().lower()
#
# # Ищем строки запроса
# results = []
# for line in lines:
#     if query in line.lower():
#         results.append(line)
#
# print('\n'.join(results))



"""Вывести только уникальные числа из списка"""
# n = int(input())
# numbers = []
#
# for i in range(n):
#     x = input()
#     if x not in numbers:
#         numbers.append(x)
#
# print('\n'.join(numbers))



"""Вывести числа по формуле"""
# n = int(input("Введите количество чисел: "))
# results = []
# xs = []
#
# for _ in range(n):
#     x = int(input("Введите число: "))
#     f = x**2 + 2 * x + 1
#     xs.append(x)
#     results.append(f)
#
# print("Введенные числа:")
# print('\n'.join(map(str, xs)))
# print("\nРезультаты:")
# print('\n'.join(map(str, results)))