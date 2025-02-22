"""Валидация пользователя"""
# # Правильное решение
# s = input()
#
# if (
#     s.startswith('@')
#     and 5 <= len(s) <= 15
#     and s[1:].isalnum()
#     and s.islower()
# ):
#     print('Correct')
# else:
#     print('Incorrect')

# # Моё решение (не прошло тесты, но корректно)
# user_input = input()
#
# # Проверяем условия
# if (user_input[0] == '@') and (5 <= len(user_input) <= 15) and (user_input[1:].islower() and user_input[1:].isalnum()):
#     print('Correct')
# else:
#     print('Incorrect')


"""Проверить номер авто на валидность"""
# s = input()
# flag = 'NO'
# correct_letters = 'АВЕКМНОРСТУХ'
#
# if 9 <= len(s) <= 10:
#     letters = s[0] + s[4:6]
#     digits = s[1:4] + s[7:]
#     underscore = s[6]
#
#     if digits.isdigit() and underscore == '_':
#         flag = 'YES'
#
#     for c in letters:
#         if c not in correct_letters:
#             flag = 'NO'
#             break
#
# print(flag)


"""Удалить ненужные комментарии (пустую строку и строку с пробелами)"""
# # Моё решение
# comments_count = int(input())
# result = []
# count = 1
#
# for _ in range(comments_count):
#     comment = input()
#     if comment.isspace() or comment == '':
#         result.append('COMMENT SHOULD BE DELETED')
#     else:
#         result.append(comment)
#
# for i in result:
#     print(f'{count}: {i}')
#     count += 1

# # Решение ИИ
# comments_count = int(input('Введите количество комментариев: '))
# result = [
#     comment for comment in (input() for _ in range(comments_count))
#     if comment.strip() # Оставляем только непустые комментарии
# ]
#
# for count, comment in enumerate(result, start=1):
#     print(f'{count}: {comment}')


"""На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
а также все символы, находящиеся между ними"""
# s = input()
#
# a = s.find('h')
# b = s.rfind('h')
# c = s.replace(s[a:b+1], '')
#
# print(c)


"""Вывести символ один раз (если он 1), индексы первого и последнего (если его 2), NO - если символа нет"""
# s = input()
# char = 'f'
#
# if s.count(char) == 1:
#     print(s.index(char))
# elif s.count(char) >= 2:
#     print(
#         s.find(char),
#         s.rfind(char),
#         sep=' '
#     )
# else:
#     print('NO')


"""Вывести самый часто встречающийся в строке символ"""
# s = input()
#
# # Словарь для подсчета вхождений символов
# char_count = {}
#
# # Подсчитываем количество вхождений каждого символа
# for char in s:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# # Переменные для хранения символа с максимальным количеством вхождений
# max_char = None
# max_count = 0
#
# # Находим символ с максимальным количеством вхождений
# for char in s:
#     if char_count[char] > max_count:
#         max_count = char_count[char]
#         max_char = char
#     elif char_count[char] == max_count:
#         max_char = char  # Обновляем, чтобы получить последний по порядку
#
# # Выводим результат
# print(max_char)


"""Определить, заканчивается ли адрес на '.com' или '.ru'"""
# s = input()
#
# result = ('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')
# print(result)


"""Определить количество цифр в строке"""
# # Решение ИИ
# s = input()
# numbers_count = sum(1 for i in s if i.isdigit())
# print(numbers_count)


# # Моё решение
# s = input()
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# numbers_count = 0
#
# for i in s:
#     if i in numbers:
#         numbers_count += 1
#
# print(numbers_count)


"""Найти количество непересикающихся сигналов '11' в строке"""
# message_count = int(input())
# odi_messages_count = 0
# odi_signal = '11'
#
# for _ in range(message_count):
#     message = input()
#
#     # Считаем непересекающиеся вхождения '11'
#     count = 0
#     index = 0 # Храним текущую позицию в строке
#
#     while True:
#         index = message.find(odi_signal, index) # поиск начинается с позиции index
#         if index == -1: # выходим из цикла, если вхождений нет
#             break
#         count += 1
#         index += 2 # Пропускаем два символа, чтобы избежать пересечения
#
#     if count >= 3:
#         odi_messages_count += 1
#
# print(odi_messages_count)


"""Определить количество упоминаний символов в строке (ДНК)"""
# s = input()
# formatted_string = s.lower().strip().replace(' ', '')
#
# print(f'''Аденин: {formatted_string.count('а')}
# Гуанин: {formatted_string.count('г')}
# Цитозин: {formatted_string.count('ц')}
# Тимин: {formatted_string.count('т')}''')


"""Подсчитать количество слов в тексте"""
# # Решение ИИ
# s = input()
# words = s.split()
# words_count = len(words)
# print(words_count)

# # Моё решение
# s = input()
# space = s.count(' ')
# print(space + 1)


"""Подсчёт количества символов в нижнем регистре"""
# text = input()
# count = 0
#
# for i in text:
#     if i.islower():
#         count += 1
#
# print(count)


"""Определить, входит ли слово 'хорош' в любом из регистров в строку"""
# text = input()
# formatted_text = text.lower().replace(' ', '')
#
# search_word = 'хорош'
#
# if search_word in formatted_text:
#     print('YES')
# else:
#     print('NO')


"""Определить, что имя и фамилия (поданые одной строкой с пробелом) начинаются с верхнего регистра"""
# initiate = input()
# space = initiate.find(' ')
#
# if initiate[0].isupper() and initiate[space + 1].isupper():
#     print('YES')
# else:
#     print('NO')


"""Методы строк"""
# # capitalize() - первые символ с заглавной, остальные - с маленькой.
# s = 'foO BaR BAZ quX'
# print(s.capitalize())

# # swapcase() - меняет регистр каждого символа на противоположный
# s = 'foO BaR BAZ quX'
# print(s.swapcase())

# # title() - возвращает копию строки, где первый символ каждого слова переводится в верхний регистр
# s = 'the sun also rises'
# print(s.title())

# # lower() - возвращает строку с символами в нижнем регистре
# s = 'the sun also rises'.upper()
# print(s.lower())

# # islower() - проверяет регистр на соответствие нижнем

# # upper() - возвращает строку с символами в верхнем регистре
# s = 'the sun also rises'.lower()
# print(s.upper())

# # isupper() - проверяет регистр на соответствие верхнему



"""Разрезать строку на 2 равные части и переставить их местами"""
# import math
# num = input()
#
# cut = math.ceil(len(num) / 2)
#
# first_side = num[:cut]
# second_side = num[cut:]
#
# result_side = second_side + first_side
#
# print(result_side)


"""Пример работы со строкой"""
# num = input()
#
# print(
#     len(num), # Общее количество символов в строке
#     num * 3, # Исходная строка, повторённая 3 раза
#     num[0], # Первый символ строки
#     num[:3], # Первые три символа строки
#     num[-3:], # Последние три символа строки
#     num[::-1], # Строка в обратном порядке
#     num[1:-1], # Строка с удалённым первым и последним символами
#     num[::-1][::2],  # Все символы через один в обратном порядке
#     sep='\n'
# )


"""Определить, является ли строка палиндромом"""
# num = input()
#
# formatted_num = num.lower().strip().replace(' ', '')
#
# if formatted_num == formatted_num[::-1]:
#     print('YES')
# else:
#     print('NO')


"""Перевести десятичное число в двоичное"""
# decimal_number = int(input())
#
# # Перевод в двоичную систему счисления
# binary_number = bin(decimal_number)[2:]  # Убираем префикс '0b'
#
# # Вывод двоичного представления
# print(binary_number)


"""Определить количество гласных и согласных букв в предложении"""
# text = input()
#
# # Список гласных букв
# vowels = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
#
# # Список согласных букв
# consonants = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
#
# vowels_count = 0
# consonants_count = 0
#
# for i in text.upper():
#     if i in vowels:
#         vowels_count += 1
#     elif i in consonants:
#         consonants_count += 1
#     else:
#         pass
#
# print(f'Количество гласных букв равно {vowels_count}')
# print(f'Количество согласных букв равно {consonants_count}')


"""Определить количество одинаковых символов в строке"""
# char = input()
# index = 1
# count = 0
#
# while index < len(char):
#     for i in char[index]:
#         if i == char[index - 1]:
#             count += 1
#     index += 1
#
# print(count)

# while index < len(char):
#     for i in char:
#         if i == char[index]:
#             count += 1
#     index += 1
#
# print(count)

# for i in char[index]:
#     if (char[index - 1] == i) or (i == char[index + 1]):
#         count += 1
#     index += 1
#
# print(count)




"""Определить, сколько раз символы '+' и '*' встречаются в строке"""
# char = input()
# count_plus = 0
# count_asterisk = 0
#
# symbols = ['+', '*']
#
# for i in char:
#     if i == symbols[0]:
#         count_plus += 1
#     elif i == symbols[1]:
#         count_asterisk += 1
#     else:
#         pass
#
# print(f'Символ + встречается {count_plus} раз')
# print(f'Символ * встречается {count_asterisk} раз')


"""Проверить наличие числа в строке"""
# num = input()
# formatted_string = num.replace(' ', '') # Удаляем все пробелы
#
# if formatted_string.isalpha():
#     print('Цифр нет')
# else:
#     print('Цифра')