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