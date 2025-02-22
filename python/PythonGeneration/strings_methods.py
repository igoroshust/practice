"""Методы строк"""
# # isspace() - метод определяет, состоит ли строка только из пробельных символов
# s1 = '               '
# print(s1.isspace())

# # isupper() - проверяет, являются ли все буквенные символы исходной строки заглавными (верхний регистр)
# # + isupper() игнорирует все небуквенные символы.
# s = 'asdj'
# print(s.isupper())

# # islower() - проверяет, являются ли все буквенные символы исходной строки строчными (в нижнем регистре)
# # + islower() игнорирует все небуквенные символы
# s = 'asdj'
# print(s.islower())

# # islower() - определяет, являются ли все буквенные символы исходной строки строчными (в нижнем регистре)
# s = 'asdj'
# print(s.islower())

# # isdigit() - метод определяет, состоит ли исходная строка только из цифровых символов
# s = '123'
# print(s.isdigit())

# # isalpha() - метод определяет, состоит ли строка только из буквенных символов
# s1 = 'ABCabc'
# print(s1.isalnum())

# # isalnum() - проверяет, состоит ли строка из буквенно-цифровых символов
# # также isalnum() возвращает True, если строка состоит только из буквенных или только из цифровых символовы
# s1 = 'abc123'
# s2 = 'abc#*$*123'
# print(s1.isalnum()) # True
# print(s2.isalnum()) # False

# # replace(<old>, <new>, [count]) - возвращает копию <s> СО ВСЕМИ вхождениями подстроки <old>, заменёнными на <new>.
# # count - необязательный параметр, определяющий количество замен.
# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault'))

# # strip() - возвращает копию строки <s> с удалёнными пробелами в начале и в конце строки.
# s = '     foo bar foo baz foo qux      '
# print(s.strip())
# # Плюс strip может удалять символы
# s = '-+-+abc+-+-'
# print(s.strip(('+-'))) # abc

# # lstrip() - возвращает копию строки <s> с удалёнными пробелами В НАЧАЛЕ строки.
# s = '     foo bar foo baz foo qux      '
# print(s.lstrip())

# # rstrip() - возвращает копию строки <s> с удалёнными пробелами В КОНЦЕ строки.
# s = '     foo bar foo baz foo qux      '
# print(s.rstrip())

# # index(<sub>, <start>, <end>) - идентичен find, но вызывает ошибку ValueError: substring not found, если <sub> не найден.
# s = 'foo bar foo baz foo qux'
# print(s.index('b'))
# print(s.index('l')) # ValueError: substring not found

# # rindex(<sub>, <start>, <end>) - идентичен index, но ищет первое значение, начиная с края строки.
# s = 'foo bar foo baz foo qux'
# print(s.rindex('foo'))
# print(s.rindex('l')) # ValueError: substring not found

# # find(<sub>, <start>, <end>) - находит индекс первого вхождения подстроки <sub> в исходной строке <s>
# s = 'foo bar foo baz foo qux'
# print(s.find('foo')) # 0

# # rfind(<sub>, <start>, <end>) - находит индекс первого вхождения подстроки <sub> в <s> с конца
# s = 'foo bar foo baz foo qux'
# print(s.rfind('foo')) # 16

# # endswith(<suffix>, <start>, <end>) - определяет, заканчивается ли строка <suffix>. True or False.
# s = 'foobar'
# print(s.endswith('ar'))


# # startswith(<suffix>, <start>, <end>) - определяет, начинается ли исходная строка s подстрокой <suffix>. True or False
# s = 'foobar'
# print(s.startswith('foo'))

# # count(<sub>, <start>, <end>) - считает количество непересекающихся вхождений подстроки <sub> в исходную строку <s>
# s = 'foo goo moo'
# print(s.count('oo'))

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