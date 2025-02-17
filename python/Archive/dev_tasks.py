"""Напишите с помощью Django ORM запрос к таблице Author, поле age у которых равен 32 (число), взяв только поле name """
# Author.objects.filter(age=32).values("name")

"""Из модели Author необходимо вывести пользователей моложе 25 лет"""
# Author.objects.filter(age__lte=25)

"""Получаем время с момента заказа товара до момента его получения покупателем"""
# from datetime import datetime, timezone
# def finish_order(self):
#     self.time_out = datetime.now()  # получаем текущее время
#     self.complete = True  # устанавливаем флаг 'завершён'
#     self.save()  # сохраняем объект, передав значение в базу данных

"""Считаем время выполнения заказа"""
# def get_duration(self):
#     from datetime import datetime, timezone
#     if self.complete:
#         return (self.time_out - self.time_in).total_seconds() // 60
#     else:  # если заказ не отдан...
#         return (datetime.now(
#             timezone.utc) - self.time_in).total_seconds() // 60  # ... возвращаем время с момента оформления до текущего момента.


"""Получаем время, прошедшее с момента заказа товара до его получения покупателем: взято из проекта eshop (django), файл: models.py"""
# from datetime import datetime
# def finish_order(self):
#     """Получаем время с момента заказа товара до момента его получения покупателем"""
#     self.time_out = datetime.now()  # получаем текущее время
#     self.complete = True  # устанавливаем флаг 'завершён'
#     self.save()  # сохраняем объект, передав значение в базу данных


"""Вернуть фамилию из строки типа Иванов Иван Иванович"""
# def get_last_name(self):
#     return self.full_name.split()[0]


"""Парсер (подтягиваем данные из сохранённого документа)"""
# import requests # отправление запросов на сервер и получение ответа
# import lxml.html # обработка данных HTML и XML
# from lxml import etree # модуль etree позволяет создавать элементы XML/HTML и их подэлементы (полезно, если пытаемся написать XML/HTML-файлы или манипулировать ими)
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser()) # попытаемся спарсить файл с помощью html-парсера.
#
# ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li') # помещаем в аргумент метода findall скопированный xpath. Здесь мы получим все элементы списка новостей (все заголовки и их даты). Findall возвращает список многих подходящих элементов
#
# for li in ul:
#     """Создаём цикл, в котором будем выводить название каждого элемента из списка"""
#     a = li.find('a') # в каждом элементе находим расположение заголовка новости, у нас это тег <a> (т.е. гиперссылка). Метод find возвращает первый подходящий элемент
#     time = li.find('time')
#     print(f"""{time.get('datetime')} --- {a.text}""")


"""Парсер"""
# import requests # отправление запросов на сервер и получение ответа
# import lxml.html # обработка данных HTML и XML
# from lxml import etree # модуль etree позволяет создавать элементы XML/HTML и их подэлементы (полезно, если пытаемся написать XML/HTML-файлы или манипулировать ими)
#
# html = requests.get('https://www.python.org/').content # получаем html главной страницы официального сайта python, content используется для получения содержимого страницы (он позволяет получить информацию в виде байтов, то есть в итоге у нас будет вся информация, не только строковая).
#
# tree = lxml.html.document_fromstring(html) # анализирует документ по заданной строке. При этом всегда создаётся правильный html-документ, что означает, что родительским узлом ялвяется <html>, а также есть тело и, возможно, заголовок.
# title = tree.xpath('/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]/a/text()')
#
# # title = tree.xpath('/html/head/title/text()') # забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html>
#
# print(title)



"""Алгоритм сортировки пузырьком (надо отсортировать от большего к меньшему)"""
# принцип работы https://skrinshoter.ru/sOTmmt4OT2I
# from random import randint
# def bubble(array):
#     for i in range(N-1):
#         for j in range(N-i-1):
#             if array[j] > array[j+1]:
#                 buff = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = buff
#     return(array)
# N = 5
# a = []
# for i in range(N):
#     a.append(randint(1, 100))
# print(bubble(a))


"""Бинарный поиск"""
# def recursive_binary_search(arr, target):
#     mid = len(arr) // 2
#     if len(arr) == 1:
#         print(arr)
#         return mid
#     elif arr[mid] == target:
#         print(arr)
#         return mid
#     else:
#         if arr[mid] < target:
#             callback_response = recursive_binary_search((arr[mid:]), target)
#             print(arr)
#             return mid + callback_response
#         else:
#             print(arr)
#             return recursive_binary_search((arr[mid:]), target)
# print(recursive_binary_search([10, 20, 30, 40, 50, 60], 60))

"""Бинарный поиск (код из вебинара)"""
# import timeit
#
# # РђР»РіРѕСЂРёС‚Рј Р•РІРєР»РёРґР°
# a = 50
# b = 130
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# #print(a + b)
#
# from random import randint
#
#
# # РђР»РіРѕСЂРёС‚Рј СЃРѕСЂС‚РёСЂРѕРІРєРё РїСѓР·С‹СЂСЊРєРѕРј
# def bubble(array):
#     for i in range(N-1):
#         for j in range(N-i-1):
#             if array[j] > array[j+1]:
#                 buff = array[j]
#                 array[j] = array[j+1]
#                 array[j+1] = buff
#     return(array)
#
# N=5
# a = []
# for i in range(N):
#     a.append(randint(1, 100))
# print(bubble(a))
#
#
# # РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР°
# def binary_search(lys, val):
#     first = 0
#     last = len(lys)-1
#     index = -1
#     if len(lys) == 1:
#         return lis[0]
#     while (first <= last) and (index == -1):
#         mid = (first+last)//2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
# #print(binary_search([10,20,30,40,50], 20))
# print(timeit.timeit("binary_search([1,4,5,6,7,10,20,30,40,50], 20)", setup="from __main__ import binary_search", number=1))
#
# # РђР»РіРѕСЂРёС‚Рј Р±РёРЅР°СЂРЅРѕРіРѕ РїРѕРёСЃРєР° (СЂРµРєСѓСЂСЃРёРІРЅС‹Р№)
# def recursive_binary_search(arr, target):
#     mid = len(arr) // 2
#     if len(arr) == 1:
#         return mid
#     elif arr[mid] == target:
#         return mid
#     else:
#         if arr[mid] < target:
#             callback_response = recursive_binary_search((arr[mid:]), target)
#             return mid + callback_response
#         else:
#             return recursive_binary_search((arr[:mid]), target)
# #print(recursive_binary_search([10,20,30,40,50,60], 20))
# print(timeit.timeit("recursive_binary_search([1,4,5,6,7,10,20,30,40,50], 20)", setup="from __main__ import recursive_binary_search", number=1))


"""Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
О клиенте известна следующая информация: имя, фамилия, город, баланс.
Далее сделайте вывод о клиентах в консоль в формате:
«Иван Петров. Москва. Баланс: 50 руб.»"""
# class Client:
#     def __init__(self, name="", surname="", city="", balance=0):
#         self.name = name
#         self.surname = surname
#         self.city = city
#         self.balance = balance
#
#     def __str__(self):
#         """Выводим данные о человеке"""
#         return f'{self.name} {self.surname}. {self.city.capitalize()}. Баланс: {self.balance} руб.'
#
# user1291 = Client('Иван', 'Петров', 'москва', 50)
# print(user1291)



"""Пример инкапсуляции данных"""
# class Human:
#     age = None
#
#     def __init__(self, age=4):
#         self.age = age
#
#     def get_age(self):
#             """Добавляем геттер, специальный метод для получения поля"""
#             return self.age
#     def set_age(self, age):
#             """Добавляем сеттер - специальный метод для установки нового значения"""
#             if age > 0 and isinstance(age, int): # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
#                 self.age = age
#
# h = Human()
# h.set_age()
# print(h.get_age())



"""Преобразование кириллицы в латиницу"""
# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh',
#      'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p',
#      'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh',
#      'shch', '', 'y', '', 'e', 'yu', 'ya'
#      ] # список соответствия русских букв литинским названиям
#
# start_index = ord('а') # вспомогательная переменная, принимающая значение кода для первой буквы русского алфавита
# title = "Программирование на Python - лучший курс" # вспомогательная переменная, содержащая переводимый заголовок
# slug = '' # вспомогательная переменная, хранящая преобразование кириллицы в латиницу
#
# for s in title.lower(): # в цикле происходит преобразование символов строки
#     if 'а' <= s <= 'я': # проверка: если текущий символ от А до Я
#         slug += t[ord(s) - start_index] # добавляем соответствующее звучание из списка Т[индекс]
#     elif s == 'ё':
#         slug += 'yo'
#     elif s in " !?;:.,":
#         slug += '-'
#     else:
#         slug += s
#
# while slug.count('--'): # если есть более двух дефисов
#     slug = slug.replace('--', '-') # заменяем два дефиса на один
#
# print(slug)



"""Запрос на введение пароля (с помощью while)"""
# pass_true = "password"
# ps = ""
#
# while ps != pass_true:
#     ps = input("Введите пароль: ")
#
# print("Вход в систему")



"""У нас есть список с данными о росте и весе людей. Нужно отсортировать их по индексу массы тела.
Он вычисляется по формуле: свой рост в метрах возвести в квадрат, затем массу тела в кг. разделить
на полученную цифру"""
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84),
# ]
#
# print(sorted(data, key=lambda x: x[0] / x[1] ** 2))

"""Из списка в предыдущем задании найти кортеж с минимальным индексом массы тела"""
# data = [
#     (82, 1.91),
#     (68, 1.74),
#     (90, 1.89),
#     (73, 1.79),
#     (76, 1.84),
# ]

# print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу




"""Как сделать соотношение пароля и логина из списка?"""
"""Решение учителя"""
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
# PWD = ['4242', '1313']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username: ")
#     password = input('Введите ваш пароль: ')
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
# def has_access(func):
#     def wrapper():
#         if username in USERS:
#             print("Авторизован как", username)
#             func()
#         else:
#             print("Доступ пользователю", username, "запрещен")
#     return wrapper
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()

"""Моё решение"""
# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
# PWD = ['4242']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username: ")
#     password = input('Введите ваш пароль: ')
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#     return wrapper
# def has_access(pwd):
#     def wrapper():
#         if password:
#             print('Добро пожаловать в систему')
#             pwd()
#         else:
#             print('Пароль неверный')
#     return wrapper
#
# @is_auth
# @has_access
# def from_db():
#     print("some data from database")
#
# from_db()




#----------------------------------------------------------------игра крестики-нолики---------------------------------------------------------------
"""
Первый вариант реализации
-------------------------------------

Что и где храним?
Что делаем с данными?
Вывод программы?
Ввод пользователя - спрашиваем данные, проверям данные, возвращаем координаты или возвращаемся к запросу данных
"""

# def greet():
#     print(f"""
# Приветствуем Вас
# в игре
# крестики-нолики
# ----------------
# формат ввода: x, y
# x - номер строки
# y - номер столбца
# """)

# def show_field():
#     """Создаём функцию для вывода поля"""
#     print(f"""
#   | 0 | 1 | 2 |
# ---------------""")
#     for i, row in enumerate(field):
#         row_str = f" {i} | {' | '.join(row)} | "
#         print(row_str)
#         print("---------------")
#     print()
#
# def ask():
#     while True:
#         cords = input("\nВаш ход: ").split() # считываем координаты
#
#         if len(cords) != 2:
#             print("Введите 2 координаты!")
#             continue
#
#         x, y = cords
#
#         if not(x.isdigit()) or not(y.isdigit()):
#             print("Введите числа!")
#             continue
#
#         x, y = int(x), int(y)
#
#         if 0 > x or x > 2 or 0 > y or y > 2:
#             print("Координаты вне диапазона!")
#             continue
#
#         if field[x][y] != " ":
#             print("Клетка занята!")
#             continue
#
#         return x, y
#
# def check_win():
#     win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
#                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
#                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
#     for cord in win_cord:
#         symbols = []
#         for c in cord:
#             symbols.append(field[c[0]][c[1]])
#         if symbols == ["X", "X", "X"]:
#             print("Выиграл X!!!")
#             return True
#         if symbols == ["0", "0", "0"]:
#             print("Выиграл 0!!!")
#             return True
#     return False
#
# greet()
# field = [[" "] * 3 for i in range(3)] # создаём вложенные списки для определения полей в игре
# num = 0
# while True:
#     num += 1
#     show_field()
#     if num % 2 == 1:
#         print("Ходит крестик")
#     else:
#         print("Ходит нолик")
#
#     x, y = ask()
#
#     if num % 2 == 1:
#         field[x][y] = "X"
#     else:
#         field[x][y] = "0"
#
#     if check_win():
#         break
#
#     if num == 9:
#         break
#         print("Ничья") # если кол-во ходов равно 9, объявляется ничья


"""
Второй вариант реализации
-------------------------
Поле
Опрос точки
Хранение координат
Кто выйграл
Взаимодействие блоков
"""

# def show_field(f):
#     num ='  0 1 2'
#     print(num)
#     #zip
#     for row,i in zip(f,num.split()):
#         print (f"{i} {' '.join(str(j) for j in row)}")
#
# def users_input(f,user):
#     while True:
#         place=input(f"Ходит {user} .Введите координаты:").split()
#         if len(place)!=2:
#             print('Введите две координаты')
#             continue
#         #is digit str
#         if not(place[0].isdigit() and place[1].isdigit()):
#             print('Введите числа')
#             continue
#         x, y = map(int, place)
#         if not(x>=0 and x<3 and y>=0 and  y<3):
#             print('Вышли из диапазона')
#             continue
#         if f[x][y]!='-':
#             print('Клетка занята')
#             continue
#         break
#     return x,y
#
#
# def win_position(f,user):
#     f_list=[]
#     print(f)
#     for l in f:
#         f_list+=l
#     print(f_list)
#     positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
#     indices = set([i for i, x in enumerate(f_list) if x == user])
#
#     for p in positions:
#         if len(indices.intersection(set(p)))==3:
#             return True
#     return False
#
#
# def start(field):
#
#     count=0
#     while True:
#         show_field(field)
#         if count%2==0:
#             user='x'
#         else:
#             user = 'o'
#         if count<9:
#             x, y = users_input(field,user)
#             field[x][y] = user
#
#         elif count==9:
#             print ('Ничья')
#             break
#         if win_position(field,user):
#             print(f"Выйграл {user}")
#             break
#         count+=1
#
# field = [['-'] * 3 for _ in range(3)]
#
# start(field)





















