"""Вывести количество букв алфавита, переданного цифрой"""
n = int(input())
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

print(alphabet[:n])


"""Сортировка строк в лексикографическом порядке"""
# s1, s2, s3 = input().strip(), input().strip(), input().strip()
#
# # Собираем слова в список
# words = [s1, s2, s3]
#
# # Сортируем слова в лексикографическом порядке
# words.sort()
#
# # Выводим отсортированные слова, разделяя их пробелами
# print(' '.join(words))


"""На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно, не учитывая регистр и игнорируя все небуквенные символы"""
# # Решение ИИ
# s1, s2 = input().strip(), input().strip()
#
#
# def clean_string(s):
#     cleaned = ''
#     for char in s:
#         if char.isalpha():  # Проверяем, является ли символ буквой
#             cleaned += char.lower()  # Приводим к нижнему регистру и добавляем к результату
#     return cleaned
#
#
# # Очищаем обе строки
# cleaned_s1 = clean_string(s1)
# cleaned_s2 = clean_string(s2)
#
# # Сравниваем очищенные строки
# if cleaned_s1 == cleaned_s2:
#     print('YES')
# else:
#     print('NO')


"""Название класса. В школе BEEGEEK названия учебных классов необычные. Они имеют следующий формат:
<номер класса><буква класса>
где <номер класса> должен находиться в диапазоне от 0 (как и все у программистов) до 9 включительно,
а буквой класса могут быть все буквы в диапазоне от «А» до «П» включительно."""
# # Решение ИИ
# import re
#
# # Читаем количество классов
# n = int(input())
#
# # Регулярное выражение для проверки формата класса
# pattern = r'^[0-9][A-П]$'
#
# results = []
#
# for _ in range(n):
#     class_name = input().upper().strip()
#     if re.match(pattern, class_name):
#         results.append('YES')
#     else:
#         results.append('NO')
#
# # Выводим результаты
# for result in results:
#     print(result)


# # Моё решение
# echo_num = int(input())
# echo_str = ''
# dex = 0
#
# alphabet = []
# # alphabet = [chr(i) for i in range(ord('А'), ord('П') + 1)] - можно и так сделать
# numbers = [i for i in range(10)]
# result = []
# start_char = 'а'
#
# for i in range(16):
#     alphabet.append(chr(ord(start_char) + i).upper())
#
# while dex < echo_num:
#     echo_str = input()
#     result.append(echo_str)
#     dex += 1
#
# for i in result:
#     if len(i) >= 3:
#         if i[0].isdigit() and i[1].isdigit():
#             num = str(i[0] + i[1])
#             if (int(num) in numbers) and i[2] in alphabet:
#                 print('YES')
#             else:
#                 print('NO')
#         else:
#             print('NO')
#
#     elif len(i) == 2:
#         if i[0].isdigit() and i[1].isalpha():
#             if (int(i[0]) in numbers) and (i[1].upper() in alphabet):
#                 print('YES')
#             else:
#                 print('NO')
#         else:
#             print('NO')
#
#     elif len(i) <= 1:
#         print('NO')
#
#     else:
#         print('NO')


"""В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму: берет самую "маленькую" и самую "большую"
строки, перемножает Unicode-коды последних символов этих строк и возводит полученное число в квадрат.
Результатом и является "волшебное" число"""

# lst = [input() for i in range(4)]
#
# result = (ord(min(lst)[-1]) * ord(max(lst)[-1]))**2
#
# print(result)


"""Определить максимальную и минимальную строку"""
# # Решение ИИ
# result = []
#
# while True:
#     s = input().strip()
#     if s == 'КОНЕЦ':
#         break
#     result.append(s)
#
# if result: # проверяем, что список не пустой
#     print(f'Минимальная строка ⬇️: {min(result)}')
#     print(f'Максимальная строка ⬆️: {max(result)}')
# else:
#     print("Не было введено ни одной строки.")


# # Моё решение
# s = ''
# result = []
#
# while s != 'КОНЕЦ':
#     s = input()
#     result.append(s)
#
# result = result[:-1]
#
# print(f'Минимальная строка ⬇️: {min(result)}')
# print(f'Максимальная строка ⬆️: {max(result)}')


"""Кодировка символов"""
# # Ввод: Hello, my name is [u-1061][u-1072][u-1082][u-1080]!
# # Вывод: Hello, my name is Хаки!
# s = input()
#
# result = ""
# i = 0
#
# while i < len(s):
#     # Ищем начало конструкции [u-
#     start = s.find("[u-", i)
#
#     if start == -1:  # Если больше нет конструкций, добавляем оставшуюся часть строки
#         result += s[i:]
#         break
#
#     # Добавляем часть строки до конструкции
#     result += s[i:start]
#
#     # Ищем конец конструкции
#     end = s.find("]", start)
#
#     if end == -1:  # Если не нашли закрывающую скобку, добавляем оставшуюся часть строки
#         result += s[start:]
#         break
#
#     # Извлекаем номер символа
#     unicode_number = int(s[start + 3:end])  # +3 для пропуска "[u-"
#
#     # Преобразуем номер в символ и добавляем к результату
#     result += chr(unicode_number)
#
#     # Обновляем индекс для продолжения поиска
#     i = end + 1
#
# print(result)


"""Шифр Цезаря"""
# s = int(input())
# message = input()
# result = []
#
# for i in message:
#     # Вычисляем новый код символа
#     new_char_code = ord(i) - s
#
#     # Если новый код меньше 'a', оборачиваем его
#     if new_char_code < ord('a'):
#         new_char_code += 26 # Оборачиваем в диапазон строчных букв
#
#     result.append(chr(new_char_code))
#
# print(''.join(result))

"""Заменить английские символы на русские и выдать сумму ord"""
# s = input()
#
# russian = ['е', 'у', 'о', 'р', 'а', 'х', 'с', 'Е', 'Т', 'О', 'Р', 'А', 'Н', 'Х', 'С', 'В', 'М']
# english = ['e', 'y', 'o', 'p', 'a', 'x', 'c', 'E', 'T', 'O', 'P', 'A', 'H', 'X', 'C', 'B', 'M']
#
# transform_string = ''
# for i in s:
#     if i.lower() in english:
#         dex = english.index(i)
#         transform_string += russian[dex] # Добавляем заменённый символ
#     else:
#         transform_string += i # Если символ не английский, добавляем его как есть
#
# old_cost = sum(ord(i) for i in s) * 3 # Стоимость старого сообщения
# new_cost = sum(ord(i) for i in transform_string) * 3 # Стоимость нового сообщения
#
# print(f"""Старая стоимость: {old_cost}🐝
# Новая стоимость: {new_cost}🐝""")


"""Подсчитать стоимость сообщения"""
# s = input()
# s1 = []
#
# for i in s:
#     s1.append(ord(i))
#
# result_sum = sum(s1) * 3
#
# print(f"""Текст сообщения: '{s}'
# Стоимость сообщения: {result_sum}🐝""")


"""Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова.
Напишите программу, которая принимает 4 слова и находит среди них самое тяжёлое слово.
Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них."""
# # Моё решение
# s, d, v, g = input(), input(), input(), input()
#
# s1 = []
# d1 = []
# v1 = []
# g1 = []
#
# test = []
#
# for i in s:
#     s1.append(ord(i))
#
# for i in d:
#     d1.append(ord(i))
#
# for i in v:
#     v1.append(ord(i))
#
# for i in g:
#     g1.append(ord(i))
#
# result = {s: sum(s1), d: sum(d1), v: sum(v1), g: sum(g1)}
#
# result_max = max(result.values())
#
# max_key = [key for key, value in result.items() if value == result_max] # находим ключ максимального значения
#
# if len(max_key) > 1:
#     print(''.join(max_key[0]))
# else:
#     print(''.join(max_key))

# # Решение ИИ
# def get_word_weight(word):
#     """Возвращает сумму кодов символов слова по таблице Unicode."""
#     return sum(ord(char) for char in word)
#
# def main():
#     words = [input() for _ in range(4)]
#     max_weight = -1
#     heaviest_word = ""
#
#     for word in words:
#         weight = get_word_weight(word)
#         if weight > max_weight:
#             max_weight = weight
#             heaviest_word = word
#
#     print(heaviest_word)
#
# if __name__ == '__main__':
#     main()


"""Вывод кода всех символов строки"""
# s = input()
# formatted_s = s.strip()
#
# for i in formatted_s:
#     print(ord(i), end=' ')

"""Вывести символ каждого значения диапазона от a до b"""
# a, b = int(input()), int(input())
#
# result = []
# for i in range(a, b+1):
#     result.append(chr(i))
#
# print(' '.join(result))


"""Вывести соседнюю буквы русского алфавита"""
# char = input()
# ord_char = ord(char)
# start_word = 'а'
# result = []
# result_char = ord_char + 1
#
# for i in range(32):
#     result.append((chr(ord(start_word) + i).upper()))
#
# if char == result[-1]:
#     print('Дальше букв нет')
# else:
#     print(chr(result_char))


"""Вывод всех заглавных букв английского алфавита"""
# for i in range(26):
#     print(chr(ord('A') + i))

"""Функции"""
# # ord() - позволяет определить код некоторого символа в таблица символов Unicode. Аргументом является одиночный символ
# num = ord('A')
# print(num) # 65

# # chr() - позволяет определить по коду символа сам символ. Аргументом является численный код
# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110)
# print(chr1, chr2, chr3) # A K n


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
