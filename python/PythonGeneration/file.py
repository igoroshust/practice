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