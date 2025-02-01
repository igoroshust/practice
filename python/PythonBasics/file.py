class Dog:
    about = "Canis Familiaris" # классовый атрибут

    def __init__(self, name, age):
        self.name = name # экземплярный атрибут
        self.age = age

    def __str__(self):
        return f'Dog(name={self.name}, age={self.age})'

    def bark(self):
        return f'{self.name} says woof!'

my_dog = Dog("Buddy", 12)
print(my_dog.name) # Buddy
print(my_dog.age) # 21
print(my_dog)
print(my_dog.about) # Canis ...
print(my_dog.bark()) # Buddy says woof!



"""Создание объекта (ООП)"""
# class Dog:
#     species = "Canis familiaris" # классовый атрибут
#
#     def __init__(self, name):
#         self.name = name # атрибут - переменная, хранящая данные, связанные с объектов: атрибуты могут быть экземплярными и классовыми (общими для всех объектов)
#     # экземплярные атрибуты создаются внутри метода __init__ и относятся к конкретному объекту.
#     def bark(self): # метод - функция внутри класса, описывающая поведение объектов. Могут принимать параметры и изменять состояние объекта или выполнять действия
#         return f"{self.name} says woof!"
#
# # Создание объекта класса Dog
# my_dog = Dog("Buddy") # объект - экземпляр класса, содержащий данные и поведение
# print(my_dog.name) # Buddy
# print(my_dog.bark()) # Buddy says woof!
# print(my_dog.species) # Canis familiaris


"""Документация по функции"""
# print(len.__doc__)

"""Пример побочного действия в функции"""
# count = 0
#
# def increment():
#     global count
#     count += 1
#
# print(count) # 0
# increment()
# print(count) # 1