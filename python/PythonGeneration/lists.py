"""На вход программе подаются натуральное число n, а затем n строк.
Напишите программу, которая создает список из символов всех строк, а затем выводит его."""
# # Решение ИИ
n = int(input())
results = []

for _ in range(n):
    s = input()
    results.extend(s) # Добавляем все символы строки в список
    # extend добавляет каждый элемент итерируемой последовательности по отдельности, тогда как append добавляет как единое целое!!!!

print(results)

# # Моё решение
# n = int(input())
# s = ''
# results = []
#
# for _ in range(n):
#     s = input()
#     results.append(s)
#
# join_results = ''.join(results)
#
# end = []
# for i in join_results:
#     end.append(i)
#
# print(end)

"""Вывести k-ую букву в каждой строке"""
# n = int(input())  # Считываем количество строк
# words = []  # Список для хранения строк
#
# # Считываем n строк
# for _ in range(n):
#     s = input()
#     words.append(s)
#
# k = int(input())  # Считываем номер буквы
#
# letters = []  # Список для хранения k-ых букв
#
# # Проходим по всем строкам
# for word in words:
#     if len(word) >= k:  # Проверяем, есть ли k-ая буква
#         letters.append(word[k - 1])  # Добавляем k-ую букву (k-1 для индексации)
#
# print(''.join(letters))  # Объединяем буквы в строку и выводим


"""Вывести чётные элементы списка"""
# n = int(input())
# s = ''
# results = []
#
# for _ in range(n):
#     s = int(input())
#     results.append(s)
#
# srt_results = results[::2]
# print(srt_results)


"""Вывести сумму соседних элементов списка"""
# # Решение ИИ
# n = int(input())
# result = []
#
# # Считываем n целых чисел
# for _ in range(n):
#     s = int(input())
#     result.append(s)
#
# # Создаём список сумм соседних чисел
# sums = []
# for i in range(n - 1):
#     sums.append(result[i] + result[i + 1])
#
# print(sums)

# # Моё решение
# n = int(input())
# s = ''
# result = []
# results = []
# count = 0
# dex = 1
#
# for _ in range(n):
#     s = int(input())
#     result.append(s)
#
# while dex < len(result):
#     for i in result:
#         results.append(result[count] + result[dex])
#     count += 1
#     dex += 1
#
# print(sorted(list(set(results))))

"""Вывести список делителей числа"""
# n = int(input())
# lst = [i for i in range(1, n+1)]
# results = []
#
# for i in lst:
#     if n % i == 0:
#         results.append(i)
#
# print(results)


"""Вывести список кубов поданных на вход чисел"""
# n = int(input())
# s = ''
# numbers_cubes = []
#
# for _ in range(n):
#     s = int(input())
#     numbers_cubes.append(s**3)
#
# print(numbers_cubes)


"""Перемножить каждую букву на её позицию в алфавите"""
# alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# result_alphabet = []
# count = 1
#
# for i in alphabet:
#     i *= count
#     result_alphabet.append(i)
#     count += 1
#
# print(result_alphabet)

"""Работа со списком"""
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# search_numbers = [5, 17]
#
# print(
#     len(numbers), # Длина списка
#     numbers[-1], # Последний элемент
#     numbers[::-1], # В обратном порядке
#     'YES' if search_numbers in numbers else 'NO', # Проверка на наличия
#     numbers[1:-1], # Без первого и последнего символа
#     sep='\n'
# )


"""Удаление элементов списка (внимание на смещение)"""
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
#
# print(colors)


"""Методы списков"""
# # del - удаление элементов списка по определённому индексу
# numbers = [i for i in range(1, 9+1)]
# del numbers[5]
# del numbers[2:4]
# del numbers[::2] # удаляем все элементы на чётных позициях
# print(numbers)


# # extend() - англ. продлевать - расширение списка другим списком
# numbers = [0, 2, 4, 6, 8, 10]
# odds = [1, 3, 5, 7]
#
# numbers.extend(odds)
# print(numbers)