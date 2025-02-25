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