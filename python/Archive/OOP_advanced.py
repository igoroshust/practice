"""Заметки с вебинаров по ООП"""

"""Именованные кортежи"""
from collections import namedtuple

User = namedtuple("User", ["id", "name", "score"]) # создание имён полей для именованного кортежа.

user_1 = User(1, "Ivan", 100)
user_2 = User(2, "Alex", 0)
user_3 = User(3, "Oleg", 10)
user_4 = User(4, "Robert", -50)
user_5 = User(5, "Victor", 30)

print(user_1.id)
print(user_1[0])