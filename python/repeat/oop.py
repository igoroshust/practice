"""Пример ООП"""
# class Dog:
#     # Конструктор - вызывается при создании объекта
#     def __init__(self, name, age):
#         self.name = name # атрибут имени
#         self.age = age # атрибут возвраста
#
#     # Метод, описывающий поведение
#     def bark(self):
#         print(f'{self.name} говорит: Гав!')
#
#     def birthday(self):
#         self.age += 1
#         print(f'С Днём рождения, {self.name}! Теперь тебе {self.age} лет.')
#
# dog1 = Dog('Бобик', 3)
#
# # Вызов методов объекта
# dog1.bark()
# dog1.birthday()

"""Наследование"""
## Создание нового класса на основе существующего
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f'{self.name} издаёт звук')
#
# class Cat(Animal):
#     def speak(self):
#         print(f'{self.name} говорит Мяу!')
#
# cat1 = Cat("Мурка")
# cat1.speak()

"""Инкапсуляция"""
## Инкапсуляция - скрытие внутренней реализации объекта
# (__ создают приватные атрибуты)
# Геттеры и сеттеры - методы доступа к атрибутам объекта, которые широко используются в ООП для инкапсуляции данных.
# Геттеры и сеттеры позволяют контролировать чтение и изменение значений атрибутов, обеспечивая защиту и возможность
# добавлять дополнительную логику при доступе к данным


## Просто пример
# class Person:
#     def __init__(self, name, age):
#         self.__name = name # приватный атрибут
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#
# p = Person("Иван", 30)
# print(p.get_age())
# p.set_age(35)
# print(p.get_age())
# # print(p.__age) # Ошибка! Прямой доступ запрещён

## Пример с getter, setter
# class Person:
#     def __init__(self, name, age):
#         self._name = name # приватный атрибут
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if age > 0:
#             self._age = age
#
# p = Person("Иван", 30)
# print(p.age)
# p.age = 35
# print(p.age)
# # print(p.__age) # Ошибка! Прямой доступ запрещён

"""Полиморфизм"""
## Полиморфизм - способность объектов разных классов иметь методы с одинаковым именем, но разной реализацией.

# class Bird:
#     def speak(self):
#         print("Птица издаёт звук")
#
# class Dog:
#     def speak(self):
#         print("Собака говорит: Гав!")
#
# class Cat:
#     def speak(self):
#         print("Кошка говорит: Мяу!")
#
# def animal_sound(animal):
#     """Функция animal_sound принимает объект любого класса с методом speak()
#         Это и есть полиморфизм"""
#     animal.speak() # вызывается метод speak у любого объекта
#
# bird = Bird()
# dog = Dog()
# cat = Cat()
#
# animal_sound(bird)
# animal_sound(dog)
# animal_sound(cat)

"""Абстракция"""
## Абстрация - выделение общих характеристик и поведения в базовом классе, при этом детали реализации скрываются в подклассах.

# from abc import ABC, abstractmethod
#
# # Абстрактный класс
# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def speak(self):
#         pass # абстрактный метод - должен быть реализован в подклассах
#
# # Конкретные классы-наследники
# class Dog(Animal):
#     def speak(self):
#         print(f'{self.name} говорит: Гав!')
#
# class Cat(Animal):
#     def speak(self):
#         print(f'{self.name} говорит: Мяу!')
#
# dog = Dog("Бобик")
# cat = Cat("Мурка")
#
# dog.speak() # Бобик говорит: Гав!
# cat.speak() # Мурка говорит: Мяу!









