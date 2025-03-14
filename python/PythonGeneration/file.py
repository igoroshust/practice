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