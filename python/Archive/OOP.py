"""Пример реализации очереди"""
# Создадим класс Queue - нужная нам очередь
# class Queue:
#     # Конструктор нашего класса, в нём происходит нужная инициализация объекта
#     def __init__(self, max_size):
#         self.max_size = max_size  # размер очереди
#         self.task_num = 0  # будем хранить сквозной номер задачи
#
#         self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
#         self.head = 0  # указатель на начало очереди
#         self.tail = 0  # указатель на элемент следующий за концом очереди
#
#     def is_empty(self):
#         return self.head == self.tail and self.tasks[self.head] == 0
#
#     def size(self):
#         if self.is_empty():  # если она пуста
#             return 0  # возвращаем ноль
#         elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
#             return self.max_size  # значит очередь заполнена
#         elif self.head > self.tail:  # если хвост очереди сместился в начало списка
#             return self.max_size - self.head + self.tail
#         else:  # или если хвост стоит правее начала
#             return self.tail - self.head
#
#     def add(self):
#         self.task_num += 1  # увеличиваем порядковый номер задачи
#         self.tasks[self.tail] = self.task_num  # добавляем его в очередь
#         print(f"Задача №{self.tasks[self.tail]} добавлена")
#
#         # увеличиваем указатель на 1 по модулю максимального числа элементов
#         # для зацикливания очереди в списке
#         self.tail = (self.tail + 1) % self.max_size
#
#     def show(self):  # выводим приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} в приоритете")
#
#     def do(self):  # выполняем приоритетную задачу
#         print(f"Задача №{self.tasks[self.head]} выполнена")
#         # после выполнения зануляем элемент по указателю
#         self.tasks[self.head] = 0
#         # и циклично перемещаем указатель
#         self.head = (self.head + 1) % self.max_size
#
# size = int(input("Определите размер очереди: "))
# q = Queue(size)
#
# # Используем клас
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", q.size())
#     elif cmd == "add":
#         if q.size() != q.max_size:
#             q.add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.show()
#     elif cmd == "do":
#         if q.is_empty():
#             print("Очередь пустая")
#         else:
#             q.do()
#     elif cmd == "exit":
#         for _ in range(q.size()):
#             q.do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")



"""Программа, проверяющая корректность зактыия скобок в строке"""
# def par_checker(string):
#     stack = [] # инициализируем стек
#
#     for s in string: # читаем строку посимвольно
#         if s == "(": # если открывающая скобка, то..
#             stack.append(s) # .. добавляем её в стек
#         elif s == ")": # если встретилась закрывающая скобка, то проверяем..
#             if len(stack) > 0 and stack[-1] == "(": # .. пуст ли стек и является ли верхний элемент - открывающей скобкой.
#                 stack.pop() # удаляем из стека
#             else:
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось, возращаем True (иначе - False).
#     return len(stack) == 0
#
# print(par_checker('())'))


"""Рекурсия стека LIFO"""
# def p(n):
#     if n == 0:
#         return
#     else:
#         p(n-1)
#         print(n)
# p(5)
# # 1
# # 2
# # 3
# # 4
# # 5



"""Напишите контекстный менеджер, который умеет безопасно работать с файлами.
В конструктор объекта контекстного менеджера передаются два аргумента: первый — путь к файлу, который надо открыть,
второй — тип открываемого файла (для записи, для чтения и т. д.).
При входе в контекстный менеджер должен открываться файл, и возвращаться объект для работы с этим файлом.
При выходе из контекстного менеджера файл должен закрываться."""
# class OpenFile:
#     def __init__(self, path, type):
#         self.file = open(path, type)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
# with OpenFile('hello.txt', 'wt') as f:
#     f.write('Мой контекстный менеджер делает тоже самое!')

"""Склейка пути"""
# import os
#
# start_path = os.getcwd()
# print(os.path.join(start_path, 'test'))


"""Создать класс Square. Добавить в конструктор класса Square собственное исключение NonPositiveDigitException,
унаследованное от ValueError, которое будет срабатывать каждый раз, когда сторона квадрата меньше или равна 0."""

# class ValueError(Exception):
#     pass
# class NonPositiveDigitException(ValueError):
#     def __init__(self):
#         print("Сторона квадрата меньше либо равна нулю.")
# class Square:
#     def __init__(self, NonPositiveDigitException, size):
#         self.size = size
#         # super().__init__()
#
# a = Square('message', 0)
#
# try:
#     if a.size <= 0:
#         NonPositiveDigitException()
#     else:
#         print("Сторона квадрата больше 0")
# finally:
#     pass


"""Пример работы с собственными исключениями"""
# class ParentException(Exception): # создание пустого класса-исключения-потомка, наследуемого от Exception
#     def __init__(self, message, error):
#         super().__init__(message) # вызов конструктора родительского класса
#         print(f"Errors: {error}")
#
# class ChildException(ParentException): # создание пустого класса-исключения-наследника от ParentException
#     def __init__(self, message, error):
#         super().__init__(message, error)
#
# try:
#     raise ChildException("message", "error") # поднимаем исключение-наследник
#
# except ParentException as e: # отлов родителя
#     print(e) # вывод информации об исключении


"""Принцип написания отлова собственного исключения"""
# class MyException(Exception): # создание пустого класса-исключения
#     pass
#
# try:
#     raise MyException("Message") # поднятие исключения
# except MyException as e: # отлов исключения
#     print(e) # вывод информации об исключении

"""Отличие __repr__ от __str__"""
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Cat(name={self.name}, age={self.age})'
#
#     def __repr__(self):
#         return f'Cat(name={self.name!r}, age={self.age!r})'
#
# a = Cat('igor', 5)
# print(a.__str__())
# print(a.__repr__())


"""Пример реализации полиморфизма (classmethod)"""
# class MathUtils:
#
#     A = 10
#
#     @classmethod
#     def add(cls, x, y):
#         return x + y + cls.A
#
#     @classmethod
#     def multiply(cls, x, y):
#         return x * y * cls.A
#
# one = MathUtils.add(5, 3)
# two = MathUtils.multiply(4, 6)
#
# print(one)
# print(two)


"""Пример моржового оператора"""
# if a := int(input(': ')) > 10:
#     print(f'{a}')
# else:
#     print(f'{a}')

"""raise (вызов исключения)"""
# age = int(input('Сколько тебе лет?\n : '))
# if age > 100 or age <= 0:
#     raise ValueError("Тебе не может быть столько лет")
#
# print(f"Тебе {age} лет!")


"""Try-except"""
# try:
#     print("Текст в опасном блоке")
#     a = int(input('a: '))
#     b = int(input('b: '))
#     c = a / b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)
#     print("Текст в теле except")
# else:
#     print("Текст в теле else, который выполнится, если в try всё прошло хорошо")
# finally:
#     print("Текст, который будет выведен в любом случае")


"""Создайте скрипт, который будет в input() принимать строки и их необходимо будет конвертировать в числа.
Добавьте try-except на то, чтобы строки могли быть конвертированы в числа. 
В случае удачного выполнения скрипта должно быть выведено сообщение: «Вы ввели правильное число».
В конце скрипта обязательно напишите: «Выход из программы»."""
# #помещаем код, который может генерировать исключения в блок try
# try:
#     i = int(input('Введите число:\t'))
# #в случае возникновения исключения ValueError выведем соответствующий текст
# except ValueError as e:
#     print('Вы ввели неправильное число')
# #если исключения ValueError не будет то выведем текст, что все в порядке
# else:
#     print(f'Вы ввели {i}')
# #в любом случае, независимо от наличия/отсутствия исключений выполним код
# finally:
#     print('Завершение программы')


"""Пример удобств (стат.методов) внутри класса"""
# class StaticClass:
#     @staticmethod # прописываем, чтобы избежать ошибки
#     def GET_BAR(): # константа
#         return "bar"
#
# print(StaticClass.GET_BAR())
#
# # sm = StaticClass() # если создать экземпляр класса и присвоить ему статический метод, то будет ошибка
# # sm.bar() # TypeError
# # StaticClass.bar()


"""Декомпозиция задачи на примере выделения сущностей по методу Аббота.
Мама моет Машу"""
# class Washable:
#     """Класс тех, кого можно мыть"""
#     def __init__(self) -> None:
#         self.dirtlevel = 0
#
#     def setDirtLevel(self, level):
#         self.dirtLevel = level
#
#     def getDirtLevel(self):
#         return self.dirtLevel
# class Washer:
#     """Класс тех, кто может мыть"""
#     def __init__(self) -> None:
#         pass
#
#     def wash(self, washable):
#         if washable.getDirtLevel() > 0:
#             washable.setDirtLevel(0)
#
# if __name__ == "__main__":
#     """Программа, в которой Мама моет Машу"""
#     masha = Washable()
#     masha.setDirtLevel(5)
#
#     mom = Washer()
#     mom.wash(masha)
#
#     print(f"Mom washes Masha")

"""Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
О клиенте известна следующая информация: имя, фамилия, город, баланс.
Далее сделайте вывод о клиентах в консоль в формате:
«Иван Петров. Москва. Баланс: 50 руб.»"""

# class Client: # тут может быть проблема с отступом
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
#     def get_info(self):
#         """Получаем информацию о человеке (без кошелька)"""
#         return f"""Фамилия: {self.surname}
# Имя: {self.name}
# Город: {self.city.capitalize()}
# """
#
# user1291 = Client('Иван', 'Петров', 'москва', 50)
# user1292 = Client('Игорь', 'Ошуст', 'Чита')
# user1293 = Client('Вероника', 'Апришникова', 'адлер')
#
# figures = [user1292, user1293]
# for figure in figures:
#     print(figure.get_info())



"""Создайте класс одной из геометрических фигур (например, прямоугольника), где в конструкторе задаются атрибуты:
начальные координаты x, y, width и height (или другие в зависимости от выбранной фигуры).
Создайте метод, который возвращает атрибуты прямоугольника как строку ( постарайтесь применить магический метод __str__).
 Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100 метод должен вернуть строку
 Rectangle : 5, 10, 50, 100."""
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return str(f"{self.x}, {self.y}, {self.width}, {self.height}")
#
#     def get_area(self):
#         """Метод, который рассчитывает площадь фигуры"""
#         return f"Площадь равна {self.width * self.height}"
#
# rect = Rectangle(1, 2, 3, 4)
# print(rect) # вывод строки
# print(rect.get_area()) # вывод площади



"""Примеры использования методов __eq__ и __str__"""
# class Dot:
#     """Хранение информации о точках на плоскости в системе координат x, y"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         """Необходимо сравнивать точки между собой..."""
#         return self.x==other.x and self.y==other.y
#
#     def __str__(self):
#         """...И выводить их для пользователя"""
#         return f'Dot: {self.x,self.y}'
#
# # посмотрим на поведение экземпляров класса
# p1=Dot(1,2)
# p2=Dot(1,2)
# print(p1==p2) # True - точки успешно сравниваются между собой
# print(str(p1)) # информация об экземпляре класса
# print(p2) # информация об экземпляре класса


"""Пример полиморфизма. Расчёт площади фигур на основе полиморфизма"""
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def get_area(self):
#         return self.a * self.b
#
# class Square:
#     """Создаём квадрат, который принимает одну сторону в качестве аргумента"""
#     def __init__(self, a):
#         self.a = a
#     def get_area_square(self):
#         return self.a ** 2 # возведение в степень **2
# # Выполняем в другом файле
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def get_square(self):
#         return self.a * self.b
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_area_square(self):
#         return self.a ** 2
#
# class Circle:
#     def __init__(self, a):
#         self.a = a
#
#     def get_area_circle(self):
#         return (self.a ** 2) * 3.14

# Запускаем в отдельном файле
# from script import Rectangle, Square, Circle
#
# rect_1 = Rectangle(10, 5)
# rect_2 = Rectangle(15, 10)
# square_1 = Square(10)
# square_2 = Square(5)
# circle_1 = Circle(1)
# circle_2 = Circle(2)
# print(f"""Площадь первого прямоугольника равна: {rect_1.get_square()}
# Площадь второго прямоугольника равна: {rect_2.get_square()}
# Площадь первого квадрата равна: {square_1.get_area_square()}
# Площадь второго квадрата равна: {square_2.get_area_square()}
# Радиус первого круга равен: {circle_1.get_area_circle()}
# Радиус второго круга равен: {circle_2.get_area_circle()}""")
#
# figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
# for figure in figures:
#     if isinstance(figure, Square):
#         print(figure.get_area_square())
#     elif isinstance(figure, Rectangle):
#         print(figure.get_square())
#     else:
#         print(figure.get_area_circle())
#
# print(rect_1==rect_2) # перегрузка операторов


"""Пример обращения к атрибутам родительского класса через экземпляры в другом файле"""
# class Cat:
#     def __init__(self, name="", sex="", age=0):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_sex(self):
#         return self.sex
#
#     def get_age(self):
#         return self.age
# class Dog(Cat):
#     """Создайте класс Dog с помощью наследования класса Cat. Создайте метод get_pet() таким образом, чтобы он возвращал только имя и возраст.
#     Далее сделайте вывод этой информации в консоль."""
#     def __init__(self, name, gender, age):
#         super().__init__(name)
#         self.gender = gender
#         self.age = age
#
#     def get_pet(self):
#         return f'{self.name} {self.age}'
#
# dog_1 = Dog("Felix", "boy", 2)
# print(dog_1.get_pet())

# # В другом файле
# # from script import Cat
# #
# # nibelung=Cat("Басик", "Девочка", 5)
# #
# # print(nibelung.get_name())
# # print(nibelung.get_sex())
# # print(nibelung.get_age())


"""Импорт классов"""
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_width(self):
#         return self.width
#
#     def get_height(self):
#         return self.height
#
#     def get_area(self):
#         """Метод, рассчитывающий площадь"""
#         return self.width * self.height
#
# # Запускаем в другом файле
# from script import Rectangle
#
# r1 = Rectangle(10, 5)
#
# print(f"""
# r1.width = {r1.width}
# r1.height = {r1.height}
# r1.get_width = {r1.get_width()}
# r1.get_height = {r1.get_height()}
# r1.get_area = {r1.get_area()}""")


"""Пример множественного наследования (в обратном порядке)"""
# class Room1:
#     def get_room(self):
#         print("room1")
#
# class Room2:
#     def get_room(self):
#         print("room2")
#
#     def get_room2(self):
#         print('room2 for flat')
#
# class Kitchen:
#     def get_kitchen(self):
#         print('kitchen')
#
# class Flat(Kitchen,Room1,Room2):
#     pass
#
# f=Flat()
# f.get_kitchen()
# f.get_room()
# f.get_room2()

"""Пример множественного наследования №2"""
# class Room:
#     def get_room(self):
#         print('room')
#
# class Room1(Room):
#     def get_room(self):
#         print('room1')
#
# class Room2(Room):
#     def get_room(self):
#         print('room2')
#
# class Flat(Room1,Room2):
#     pass
#
# print(Flat.mro()) # метод класса, показывающий порядок наследования
#
# f=Flat()
# f.get_room()

"""Пример переопределения атрибута или метода родительского класса из дочернего"""
# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.event_type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_discription(self):
#         print("This is generic event.")
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_views = number_of_views
#
#     def show_discription(self):
#         print("This event means someone has browsed an item.")
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=142342341239, session_id="0:DKjjdsALJwqijIRJWQIjirj", number_of_views=6)
#     test_view_event.show_discription()
#     print(test_view_event.type)


'''Пример работы конструкции if __name__ == "__main__":'''
# class MyClass:
#     def f(self):
#         return 155
# mc2=MyClass()
# print("Этот текст будет доступен извне:", mc2.f())
#
# if __name__ == "__main__":
#     mc=MyClass()
#     print("Этот текст скрыт при просмотре извне:", mc.f())

# запускам в отдельном файле код:
# from script import MyClass
# if __name__ == "__main__":
#     m=MyClass()
#     print("Текст внутри файла OOP", m.f())

'''Пример работы конструкции if __name__ == "__main__": '''
# class MyClass():
#     def f(self):
#         return 155
# mc2=MyClass()
# print("It's for test too", mc2.f())
#
# if __name__ == "__main__":
#     mc=MyClass()
#     print("It's only for test", mc.f())

"""Наследование (пример)"""
# class One:
#     a = 1
#
# class Two (One):
#     pass
# print(Two.a)

"""Наследование (пример)"""
# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
# class Food (Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=5)
# print(eggs.is_available())


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


# class Event:
#     """Мы ходим обрабатывать некоторые события из уже известных нам логов событий"""
#     def __init__(self, timestamp=0, event_type="", session_id=""): # для каждой переменной задаём значение по умолчанию (сразу после имени аргумента метода)
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         """Данный метод позволяет инициализировать объект напрямую"""
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
# # допустим, мы распарсили логи и получили список словарей вроде такого:
# events = [
#     {
#         "timestamp": 151312312399,
#         "type": "itemViewEvent",
#         "session_id": "0:NfjidjFOIJSijoiewjroiEJDJqw"
#     },
#     {
#         "timestamp": 232030403099,
#         "type": "itemViewEvent",
#         "session_id": "0:MasdhihasdioHOQWIHEDJqw"
#     },
#     {
#         "timestamp": 401203123012,
#         "type": "itemViewEvent",
#         "session_id": "0:DKoskadPOKADOSKqew"
#     }
# ]
#
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)






# class Product:
#     def __init__(self, name, category, quantity_in_stock): # init - это метод
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self): # is_available - это метод
#         return True if self.quantity_in_stock > 0 else False
#
# eggs = Product("eggs", "food", 5) # создаём экземпляр класса под названием eggs, в который передаём имя, категорию, остаток через запятую
# print(eggs.is_available()) # возвращает True, потому что количество яиц на складе > 0






# class User:
#     def __init__(self, name, email): # метод __init__ заранее определяет атрибуты новых экземпляров (self, произвольный набор аргументов, как обычная функция).
#         self.name = name
#         self.email = email
#
# peter = User(name="Peter Robertson", email="peterroberson@gmail.com") # присваиваем значения обязательным(!) атрибутам класса
# print(peter.name)
# print(peter.email)

# class User: # создание класса
#     number_of_fingers = 5 # атрибут класса
#     number_of_eyes = 2 # атрибут класса
#
# lancelot = User() # экземпляр класса
# print(lancelot.number_of_fingers) # экземпляр с атрибутом



"""Тир (игра)"""
# import pygame
# import random as rnd
# class Pos:
#     """Класс позиции элемента, хранящий значения x и y"""
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
# # абстракция - класс произвольной фигуры с полями позиция и цвет
# class Figure:
#     def __init__(self, pos) -> None:
#         self.setPos(pos)
#
#     def setPos(self, pos):
#         self.pos = pos
#
#     def getPos(self):
#         return self.pos
#
#     def setColor(self, color):
#         self.color = color
#
#     def getColor(self):
#         return self.color
#
#     def isIn(self, x, y) -> bool:
#         """Метод, указывающий на форму, при выполнении метода класс возвращает True, если точка, переданная x и y лежит внутри фигуры и
#         False в противном случае, поскольку класс Figure не имеет формы, то всегда возвращает False"""
#         return False
#
# class Square(Figure):
#     """Класс прямоугольника с шириной и высотой"""
#     def __init__(self, pos, w, h) -> None:
#         super().__init__(pos)
#         self.w = w
#         self.h = h
#
#     def getWidth(self):
#         return self.w
#
#     def getHeight(self):
#         return self.h
#
#     def isIn(self, x, y) -> bool:
#         """isIn в этом случае возвращает True, если точка лежит между границами прямоугольника"""
#         _pos = super().getPos()
#         if (_pos.x < x) and ( (_pos.x + self.w) > x) and (_pos.y < y) and ( (_pos.y + self.h) > y):
#             return True
#         return False
#
# class HitMark:
#     """Класс цели, включающий параметр стоимости"""
#     def __init__(self, cost) -> None:
#         self.setCost(cost)
#         self.setState(HitMark.State_Normal)
#
#     def setCost(self, cost):
#         self.cost = cost
#
#     def getCost(self):
#         return self.cost
#
# class SquareHitMark(Square, HitMark):
#     """Класс прямоугольной цели, наследуемый от класса прямоугольника и класса цели, который включает как форму, так и стоимость"""
#     def __init__(self, pos, w, h, cost) -> None:
#         super().__init__(pos, w, h)
#         HitMark.setCost(self, cost)
#
# class GameEvent:
#     """Класс внутриигрового обмена сообщениями, который служит коробочкой, в которую передаются сообщения между графикой и логикой"""
#     Event_None = 0 # пустое сообщение
#     Event_Tick = 1 # событие таймера
#     Event_Hit = 2 # событие выстрела по цели
#
#     def __init__(self, type, data) -> None:
#         self.type = type
#         self.data = data
#
#     def getType(self):
#         return self.type
#
#     def getData(self):
#         return self.data
#
# class GameLogic:
#     """Класс игровой логики, включающий всю внутриигровую логику, состояющую из двух дейсвтий:
#     1) нахождение пересечения клика пользователя с фигурой
#     2) подсчёт очков"""
#     def __init__(self, w, h) -> None:
#         self.gameboard_width = w # ширина игрового поля
#         self.gameboard_height = h # высота игрового поля
#         self.marks = [] # активные цели на доске
#         self.hitMarks = [] # поражённые цели
#         self.score = 0 # полученные очки
#
#     def processEvent(self, event):
#         """Метод обработки сообщений, которые приходят к игровой логике"""
#         if event.type == GameEvent.Event_Tick: # если событие таймер, то добавляем ещё одну цель к списке активных целей
#             markRandPos = Pos(rnd.randint(20, self.gameboard_width - 20), rnd.randint(20, self.gameboard_height - 20))
#             # случайного размера от 10 до 20
#             markSize = rnd.randint(10, 20)
#             # стоимость цели обратно пропорциональна размеру
#             markCost = 30 - markSize
#             # случайный цвет цели в формате RGB
#             markColor = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
#             mark = SquareHitMark(markRandPos, markSize, markSize, markCost)
#             mark.setColor(markColor)
#             # добавляем цель на доску
#             self.addHitMark(mark)
#             # если сообщение “выстрел в цель”, то обрабатываем эту ситуацию
#             # используя позицию pos, переданную от интерфейса
#         if event.type == GameEvent.Event_Hit:
#             self.hit(event.data)
#
#         # метод добавить цель на “логическую” доску
#
#     def addHitMark(self, mark):
#         self.marks.append(mark)
#
#         # метод поразить цель на “логической” доске
#
#     def hit(self, pos):
#         # перебираем все цели, и если метод isIn возвращает True
#         # добавляем стоимость цели к счету и перемещаем ее из списка активных целей в пораженные
#         for markIndex in range(len(self.marks)):
#             mark = self.marks[markIndex]
#             if mark.isIn(pos.x, pos.y):
#                 self.score += mark.getCost()
#                 self.marks.pop(markIndex)
#                 self.hitMarks.append(mark)
#                 break
#         # метод возвращает все активные цели на доске
#
#     def getBoard(self):
#         return self.marks
#         # метод возвращает текущий счёт
#
#     def getScore(self):
#         return self.score
#
# class PyGameGui:
#     """Класс, реализующий графическую подсистему игры"""
#     def __init__(self, w, h, logic) -> None:
#         self.main_w = w # ширина окна
#         self.main_h = h # высота окна
#         self.screen = pygame.display.set_mode([self.main_w, self.main_h]) # окно pygame
#         self.logic = logic # логика игры в виде внутреннего объекта
#         self.font = pygame.font.SysFont('Consolas', 30)
#
#     def run(self):
#         """Метод, который запускает игру"""
#         running = True
#         pygame.time.set_timer(pygame.USEREVENT + GameEvent.Event_Tick, 1000) # устанавливаем таймер pygame на 1 сек.
#         while running:
#             """Создаём бесконечный цикл обработки сообщений от пользователя.
#             Если пользователь закрыл окно, то завершаем обработку событий и заканчиваем игру,
#             Иначе обрабатываем сообщение"""
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 else:
#                     self.processEvent(event)
#             self.draw() # выполняем отрисовку
#
#     def processEvent(self, event):
#         """Метод обработки сообщений от интерфейса"""
#         if (event.type >= pygame.USEREVENT) and (event.type < pygame.NUMEVENTS):
#             myevent = GameEvent(event.type - pygame.USEREVENT, None)
#             self.logic.processEvent(myevent)
#
#         if event.type == pygame.MOUSEBUTTONDOWN:  # если событие клик мышкой, то передаём позицию клика в сообщении Hit
#             pypos = event.pos
#             myevent = GameEvent(GameEvent.Event_Hit, Pos(pypos[0], pypos[1]))
#             self.logic.processEvent(myevent)
#
#     def draw(self):
#         """Метод отрисовки доски"""
#         self.screen.fill((255, 255, 255))  # заполняем фон
#         marks = self.logic.getBoard()  # получаем все активные цели на доске и отрисовываем из в виде прямоугольников соответствующего цвета
#         for mark in marks:
#             pygame.draw.rect(self.screen, mark.getColor(), pygame.Rect(mark.getPos().x, mark.getPos().y, mark.getWidth(), mark.getHeight()))
#
#         score = self.logic.getScore()  # получаем текущие очки
#         self.screen.blit(self.font.render(f"score:{score}", True, (0, 0, 0)), (32, 48))  # отображаем счёт на окне
#         pygame.display.flip()
#
#
# if __name__ == "__main__":
#     """Соединяем все части вместе и запускаем игру"""
#     pygame.init()
#     width = 800
#     height = 600
#     gui = PyGameGui(width, height, GameLogic(width, height))
#     gui.run()
#     pygame.quit()



"""Морской бой"""
# from random import randint
# def greet():
#     print(f"""{'~' * 20}
# Добро пожаловать
# в игру
# морской бой
# {'~' * 20}
# формат ввода: x y
# x - номер строки
# y - номер столбца""")
#
# class BoardException(Exception):
#     """Общий класс, содержащий в себе все остальные классы исключений.
#     Если мы хотим отловить несколько исключений, то их не нужно прописывать по отдельности"""
#     pass
#
# class BoardOutException(BoardException):
#     """Если пользователь выстрелит за пределы доски, сработает это исключение. Пользовательский класс исключений"""
#     def __str__(self):
#         return "Вы пытаетесь выстрелить за пределы доски!"
#
# class BoardUsedException(BoardException):
#     """Если пользователь выстрелит в уже задействованную клетку, сработает это исключение. Пользовательский класс исключений."""
#     def __str__(self):
#         return "Вы уже стреляли в эту клетку!"
#
# class BoardWrongShipException(BoardException):
#     """Исключение для беспрепятственного размещения кораблей. Пользователю данное исключение не отображается."""
#     pass
#
# # ----------------------------------------------------------------------------------------------------------------------
#
# class Dot:
#     """Класс, содержащий все точки корабля на поле"""
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         """Сравнение точек"""
#         return self.x == other.x and self.y == other.y
#
#     def __repr__(self):
#         """Вывод точек в консоль"""
#         return f"Dot({self.x}, {self.y})"
#
# # ----------------------------------------------------------------------------------------------------------------------
# class Ship:
#     """Класс Корабль"""
#     def __init__(self, bow, l, o):
#         self.bow = bow # нос корабля
#         self.l = l # длина корабля
#         self.o = o # ориентация корабля (0 - вертикальный, 1 - горизонтальный)
#         self.lives = l
#
#     @property # декоратор @property позволяет организовать класс так, чтобы скрыть внутреннюю структуру класса, оставив видимым только нужный API.
#     def dots(self):
#         ship_dots = [] # список с точками всего корабля
#         for i in range(self.l): # проходимся в цикле по значениям от 0 до (длинны корабля - 1)
#             cur_x = self.bow.x # текущая точка корабля
#             cur_y = self.bow.y # текущая точка корабля
#
#             if self.o == 0: # шаг на одну клетку относительно ориентации корабля
#                 cur_x += i
#
#             elif self.o == 1: # шаг на одну клетку относительно ориентации корабля
#                 cur_y += i
#
#             ship_dots.append(Dot(cur_x, cur_y)) # добавляем значение в список
#
#         return ship_dots
#
#     def shooten(self, shot):
#         """Проверка на попадание"""
#         return shot in self.dots
#
#
# # s = Ship(Dot(1, 2), 4, 0) # передаём координаты корабля в экземпляре
#
# # ----------------------------------------------------------------------------------------------------------------------
#
# class Board:
#     """Игровое поле"""
#     def __init__(self, hid=False, size=6):
#         self.hid = hid  # hid - нужно ли скрывать поле?
#         self.size = size # размер поля
#
#         self.count = 0 # количество поражённых кораблей
#
#         self.field = [["0"] * size for _ in range(size)] # сетка, в которой храним состояние клеток
#
#         self.busy = [] # занятые точки (либо кораблём, либо выстрелом)
#         self.ships = [] # список кораблей доски
#
#     def __str__(self):
#         """Вывод корабля на доску"""
#         res = ""
#         res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
#         for i, row in enumerate(self.field): # в цикле проходимся по строкам доски, берём индекс и...
#             res += f"\n{i + 1} | " + " | ".join(row) + " |" # ... выводим: номер строки | клетки строки
#
#         if self.hid:
#             res = res.replace("■", "0") # если True, заменяем все симолы корабля на пустые символы
#         return res
#
#     def out(self, d):
#         """Проверяем нахождение точки за пределами доски"""
#         return not ((0 <= d.x < self.size) and (0 <= d.y < self.size)) # условие нахождение точки в пределах доски - её нахождение в диапазоне от 0 до size
#
#     def contour(self, ship, verb=False): # verb указывает на необходимость ставить точки (.) вокруг кораблей
#         """Контур корабля"""
#         near = [
#             (-1, -1), (-1, 0), (-1, 1),
#             (0, -1), (0, 0), (0, 1),
#             (1, -1), (1, 0), (1, 1)
#         ] # все точки вокруг текущей (сдвиги по диагонали и вертикали)
#         for d in ship.dots: # берём каждую точку корабля...
#             for dx, dy in near: # ...проходимся в цикле по списку near...
#                 cur = Dot(d.x + dx, d.y + dy) # ...сдвигаем исходную точку на dx и dy
#                 # self.field[cur.x][cur.y] = "+" # вывод плюса для точек. Это поможет для определения клеток, на которые корабли ставить нельзя.
#                 if not(self.out(cur)) and cur not in self.busy: # если точка не выходит за пределы доски и точка не занята...
#                     if verb: #
#                         self.field[cur.x][cur.y] = "." # ставим в ячейке символ точки (.)
#                     self.busy.append(cur) # добавляем точку в список занятых
#
#     def add_ship(self, ship):
#         for d in ship.dots: # проверка каждой точки корабля...
#             if self.out(d) or d in self.busy: # ... что она не выходит за границу и не занята.
#                 raise BoardWrongShipException() # вызов исключения в случае успешной проверки условия
#         for d in ship.dots: # проверка каждой точки...
#             self.field[d.x][d.y] = "■" # ... поставим в каждой точке квадрат...
#             self.busy.append(d) # ... запишем точку в список занятых (точки расположения корабля или соседние)
#
#         self.ships.append(ship) # добавляем список собственных кораблей
#         self.contour(ship) # обводим список собственных кораблей по контуру
#
#     def shot(self, d):
#         """Выстрел"""
#         if self.out(d): # выходит ли точка за границу?...
#             raise BoardOutException() # ... если да, вызываем исключение
#
#         if d in self.busy: # занята ли точка?...
#             raise BoardUsedException() # ... если да, вызываем исключение о занятости точки
#
#         self.busy.append(d) # точка занята (если не была занята)
#
#         for ship in self.ships:
#             """Проходимся в цикле по кораблям и проверяем, принадлежит ли точка какому-либо кораблю или нет"""
#             if ship.shooten(d): # если корабль был подстрелен...
#                 ship.lives -= 1 # уменьшаем количество жизней корабля
#                 self.field[d.x][d.y] = "X" # ставим в эту точку икс
#                 if ship.lives == 0: # если у корабля кончились жизни, то...
#                     self.count += 1 # прибавляем к счётчику уничтоженных кораблей единицу
#                     self.contour(ship, verb=True) # обводим корабль, чтобы контур обозначился точками
#                     print("Корабль уничтожен")
#                     return False
#                 else:
#                     print("Корабль ранен!")
#                     return True
#
#         self.field[d.x][d.y] = "." # если никакой корабль не поражён, срабатывает этот код
#         print("Мимо!")
#         return False
#
#     def begin(self):
#         self.busy = [] # обнуление списка вначале игры (храним точки выстрела игрока).
#
#     def defeat(self):
#         """Поражение"""
#         return self.count == len(self.ships)
#
# # ----------------------------------------------------------------------------------------------------------------------
# class Player:
#     """Игрок"""
#     def __init__(self, board, enemy):
#         self.board = board
#         self.enemy = enemy
#
#     def ask(self):
#         raise NotImplementedError() # при попытке вызвать метод будет вызываться исключение (метод должен быть у потомков класса)
#
#     def move(self):
#         """В бесконечном цикле пытаемся сделать выстрел"""
#         while True:
#             try:
#                 target = self.ask() # просим компьютера или пользователя дать координаты выстрела
#                 repeat = self.enemy.shot(target) # выполняем выстрел
#                 return repeat # если выстрел успешен, возвращаем запрос на повторение хода
#             except BoardException as e: # если выстрел не удался, печатаем исключение
#                 print(e)
#
# # ----------------------------------------------------------------------------------------------------------------------
# class AI(Player):
#     """Класс игрок-компьютер"""
#     def ask(self):
#         d = Dot(randint(0, 5), randint(0, 5)) # генерируем две случайные точки от 0 до 5
#         print(f"Ход компьютера: {d.x+1} {d.y+1}")
#         return d
#
# class User(Player):
#     def ask(self):
#         while True:
#             cords = input("Ваш ход: ").split() # запрос координат
#
#             if len(cords) != 2: # проверка, что введены две координаты
#                 print("Введите 2 координаты! ")
#                 continue
#
#             x, y = cords
#
#             if not (x.isdigit()) or not (y.isdigit()): # проверяем, что введённое значение - число
#                 print(" Введите числа! ")
#                 continue
#
#             x, y = int(x), int(y)
#
#             return Dot(x - 1, y - 1) # возвращаем нашу точку, не забыв вычесть единицу
#
# class Game:
#     """Игра"""
#     def __init__(self, size=6):
#         self.size = size
#         pl = self.random_board() # генерируем случайную доску для игрока
#         co = self.random_board() # генерируем случайную доску для компьютера
#         co.hid = True # скрываем доску компьютера
#
#         self.ai = AI(co, pl) # создание игрока AI
#         self.us = User(pl, co) # создание игрока User
#     def try_board(self):
#         """Пытаемся создать доску и расставить на неё каждый корабль"""
#         lens = [3, 2, 2, 1, 1, 1, 1] # длины кораблей
#         board = Board(size=self.size) # создание доски
#         attempts = 0 # количество попыток
#         for l in lens: # для каждой длины корабля будем пытаться его поставить
#             while True:
#                 attempts += 1
#                 if attempts > 2000:
#                     return None
#                 ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
#                 try:
#                     board.add_ship(ship) # попытка добавить корабль
#                     break
#                 except BoardWrongShipException:
#                     pass
#
#         board.begin()
#         return board
#
#     def random_board(self):
#         """Генерация случайной доски"""
#         board = None # пуская доска
#         while board is None: # создание доски в бесконечном цикле при условии, что доска пустая
#             board = self.try_board()
#             return board # возвращаем непустую доску
#
#     def loop(self):
#         """Создаём игровой цикл"""
#         num = 0 # номер хода
#         while True:
#             print(f"""{'~' * 20}
# Доска пользователя:
# {self.us.board}
# {'~' * 20}
# Доска компьютера:
# {self.ai.board}
# {'~' * 20}""")
#             if num % 2 == 0: # если номер хода чётный, ходит пользователь
#                 print("Ходит пользователь!")
#                 repeat = self.us.move() # записываем результат
#             else: # если номер хода нечётный, ходит компьютер
#                 print("Ходит компьютер!")
#                 repeat = self.ai.move()
#             if repeat: # ход остаётся у того же игрока, если попал
#                 num -= 1
#
#             if self.ai.board.defeat(): # проверка на количество поражённых кораблей, равных количеству кораблей на доске
#                 print("~" * 20)
#                 print("Пользователь выиграл!")
#                 break
#
#             if self.us.board.defeat():  # проверка на количество поражённых кораблей, равных количеству кораблей на доске
#                 print("~" * 20)
#                 print("Компьютер выиграл!")
#                 break
#             num += 1
#     def start(self):
#         greet()
#         self.loop()
#
# g = Game()
# g.start()


