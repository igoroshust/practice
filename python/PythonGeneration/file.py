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