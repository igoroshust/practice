# XSS, CSRF, JWT
# Парсинг,
# Асимптотическая сложность
# Алгоритмы
# Структуры данных, типы данных
# ООП
# Паттерны проектирования
# Парадигмы программирования

# Docker, Compose, Redis
# SQL, Postgres

# Функции высшего порядка
# Асинхронное программирование
# Замыкание функции
# Рекурсия
# Побочные эффекты
# Односвязный список
# Брокер сообщений


"""Паттерны проектирования"""
# Паттерные проектирования - это проверенные решения распространённых проблем, возникающих при работке ПО.
# Они помогают разработчикам создавать более гибкие, поддерживаемые и масштабируемые приложения.

# 1. Sigleton - одиночка. Гарантирует, что у класса есть только 1 экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.
# подразумевает наличие одного большого объекта, имеющего глобальный доступ ко всему.
# Гарантирует, что класс имеет только один экземпляр и предоставляет глобальную точку доступа к нему.
# Ситуация: нужно создать класс, который будет управлять конфигурацией приложения, и мы хотим, чтобы у него был только один экземпляр

# 2. Lazy Initialization - техника, при которой объект создаётся только в тот момент, когда он действительно необходим,
# # а не в момент инициализации программы. Это полезно для экономии ресурсов, особенно если создание объекта является дорогостоящей операцией.
# # Ситуация: создадим класс `DatabaseConnection`, который будет использовать Lazy Initialization для создания единственного экземпляра соединения с базой данных.

# 3. Factory (Фабрика) - для создания новых объектов придумывают отдельный класс. Он создаёт объекты как копии некоего эталона.
# Это когда создают отдельный класс для создания новых объектов.
# Ситуация: есть несколько типов уведомлений (Email, SMS), мы хотим создать их без жёсткой привязкии к конкретным классам.

# 4. Abstract Factory - предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.
# # Ситуация: вы разрабатываете кросс-платформенное приложение и вам нужно создать интерфейсы для различных платформ (Windows, Mac).

# # 5. Builder - разделяет конструирование сложного объекта и его представление, так что один и тот же процесс строительства
# # может создавать разные представления. Похож на фабрику, но новые объекты можно модифицировать. Они создаются по сложной логике, а не клонируют эталонный.
# # Ситуация: вы хотите создать сложный объект, например, дом, который может иметь различные компоненты (крыша, стены, окна и т.д.).

# # 6. Prototype - Создает новые объекты путём копирования существующих. Объект сам создаёт свои копии.
# # Ситуация: есть объект, который вы хотите клонировать, чтобы создать новые экземпляры с теми же свойствами.


# 7. Observer - наблюдатель. Определяет зависимость "один ко многим" между объектами. При изменении состояния одного объекта все его зависимые объекты уведомляются и обновляются автоматически.
# 8. State - состояние. Позволяет объекту изменять своё поведение в зависимости от его состояния (игра: жив, здоров, ранен).

# 9. Декоратор - позволяет динамически добавлять новые функциональные возможности объектам, оборачивая их в другие объекты.

# 10. Strategy - стратегия. Позволяет изменять поведение программы в зависимости от ситуации, не изменяя сам класс.
# 11. Адаптер - позволяет объектам с несовместимыми интерфейсами работать вместе.
# 12. Команда - инкапсулирует запрос как объект, позволяя параметризировать клиентов с различными запросами, ставить запросы в очередь или логировать их, а также поддерживать отмену операций.








"""ООП"""
# 1. Инкапсуляция - принцип, позволяющий скрыть внутренние детеали реализации объекта и предоставить доступ к ним только через определённые методы.
# Это помогает защитить данные данные и уменьшить зависимость между компонентами.
# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balance = balance # Приватное свойство
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f'Deposited: {amount}')
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew: {amount}")
#         else:
#             print("Insufficient funds")
#
#         def get_balance(self):
#             return self.__balance  # Метод для доступа к приватному свойству
#
# # Пример использования
# account = BankAccount()
# account.deposit(100)
# account.withdraw(50)
# print("Current balance:", account.get_balance())  # Вывод: Current balance: 50

# 2. Наследование. Механизм, позволяющий создавать новый класс на основе существующего. Новый класс (наследник) наследует свойства и методы родительского класса.
# class Animal:
#     def speak(self):
#         return 'Animal speaks'
#
# class Dog(Animal):
#     def speak(self):
#         return 'Woof!'
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
# dog = Dog()
# cat = Cat()
#
# print(
#     dog.speak(),
#     cat.speak(),
#     sep='\n'
# )

# 3. Полиморфизм - это возможность использовать один интерфейс для работы с разными типами объектов.
# Это позволяет использовать методы, которые могут иметь разные реализации в разных классах.
# class Bird:
#     def fly(self):
#         return "Flies in the sky"
#
# class Airplane:
#     def fly(self):
#         return "Soars through the clouds"
#
# def let_it_fly(flyable):
#     print(flyable.fly())
#
# bird = Bird()
# airplane = Airplane()
# let_it_fly(bird)
# let_it_fly(airplane)


# Полиморфизм ещё.
# Полиморфизм - способность объектов разных классов реагировать на одно и тоже событие (метод) по-разному.
# Получается, можно использовать один и тот же метод для разных объектов, и каждый объект будет выполнять свою собственную реализацию этого метода.



# class Vehicle:
#     def start_engine(self):
#         pass # Абстрактный метод
#
# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine started"
#
# class Motocycle(Vehicle):
#     def start_engine(self):
#         return "Motocycyle engine started"
#
# def start_vehicle(vehicle: Vehicle):
#     print(vehicle.start_engine()) # Вызываем метод start_engine
#
# car = Car()
# motocycle = Motocycle()
# start_vehicle(car)
# start_vehicle(motocycle)




# class Adder:
#     def add_sum(self, a, b):
#         return a + b
#
# class Concat(Adder):
#     pass
#
# class Summer(Adder):
#     pass
#
# concat = Concat()
# summer = Summer()
# print(
#     concat.add_sum('Igor', 'Alice'),
#     summer.add_sum(3, 4),
#     sep='\n'
# )


# 4. Абстракция - принцип, позволяющий скрыть сложные детали реализации и показывать только необходимые характеристики объкта.
# В Python абстракция достигается с помощтю абстрактных классов и интерфейсов.
# from abc import ABC, abstractmethod
#
# class Shape(ABC): # абстрактный класс
#     @abstractmethod
#     def area(self):
#         pass # Метод без реализации
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height # Реализация метода area
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2 # Реализация метода area
#
# shapes = [Rectangle(3, 4), Circle(5)]
# for shape in shapes:
#     print("Area: ", shape.area())


# Различие между Инкапсуляцией и Абстракцией:
# Инпуксуляция:
# 1. Защита данных и контроль над их изменением;
# 2. Скрывает внутренние данные и реализацию методов;
# 3. Защита данных и управления доступа к ним;

# Абстракиция:
# 1. Сокрытие сложности и упрощение взаимодействия с объектами;
# 2. Скрывает сложные детали реализации, предоставляя только интерфейс;
# 3. Используется для создания общих интерфейсов и определения, какие методы должны быть реализованы в подклассах;



"""КЭШ"""
# Временное хранилище данных, которое используется для ускорения доступа к часто запрашиваемым данным.
# Кэш может находится в оперативной памяти, на дисках или в других местах.


"""Docker"""
# Docker - это платформа для автоматизации развёртывания, масштабирования и управления приложениями в контейнерах. Контейнера позволяют упаковывать
# приложение и все его зависимости в единый образ, который можно запускать на любой системе, поддерживающей Docker. Это упрощает процесс развёртывания.

# Особенности Docker:
# 1. Изоляция. Каждое приложение работает в своём собственном контейнере, что предотвращает конфликты между зависимостями.
# 2. Портативность. Контейнеры могут быть запущены на любой системе, где установлен Docker, независимо от операционной системы.
# 3. Упрощение CI/CD. Docker облегчает интеграцию и развёртывание приложений, что делаего его популярным в DevOps-практиках.

# ------------- Docker Compose -----------
# Docker Compose - инструмент для определения и запуска многоконтейнерных Docker-приложений.
# С помощью файла конфигурации (docker-compose.yml) можно описать, какие контейнеры вам нужны, как они взаимодействуют друг с другом, какие конфиги должны быть установлены.
# Основные особенности Docker Compose: упрощение конфигурации, управление многими контейнерами, сетевые настройки.


"""Redis"""
# Redis (REmote Dictionary Server) - высокопроизводительная система управления базами данных в памяти, поддерживающая структуры данных, такие как строки
# хэши, списки, множества и упорядоченные множества. Redis часто используется как кэш, брокер сообщений или БД для приложений, требующих высокой скорости обработки данных.
# Особенности: высокая производительность, поддержка различных структур данных, персистентность (сохраняет данные на диск), поддержка репликации и кластеризации.




"""Структура данных"""
# Это программная единица, позволяющая хранить и обрабатывать множество логически связанных объектов.

# Виды структур данных: Массивы (статические и динамические) и хэш-таблицы.

# Массив - упорядоченный набор данных. Упорядоченный - хранение этой структуры в памяти каким-то образом организовано.
# Массив - фиксированный набор элементов одного типа, хранящихся в последовательных ячейках памяти. Размер массива задаётся при его создании и не может быть изменён.
# Массивы бывают одномерные, двумерные, трёхмерные и т.д. Их отличительной особенностью является хранение элементов в последовательных ячейках памяти/
# И это становится одним из ограничений массива: при его создании мы всегда должны указывать, какое количество физической памяти нужно для него "забронировать"
# СТАТИЧЕСКИЙ МАССИВ - тот, для которого заранее резервируется определённая область в памяти.
# ДИНАМИЧЕСКИЙ МАССИВ - изменяют свой размер с помощью буферного механизма.

# Важно различать:
# Логический размер массива (logical size) - фактическая заполненность массива;
# Зарезервированный размер памяти (capacity) - фактическая заполненность массива;
# Наиболее выгодное использование массивов возникает в ситуациях частого обращения к элементам массива по индексам, и в
# меньшей степени возникает необходимость добавлять и удалять элементы на произвольное место.
# Пример: Забег легкоатлетов, победители - индекс. Но если кого-то исключили, нужно всех сдвигать.

# Хэш-таблицы - это структуры данных, которые обеспечивают эффективное хранение и поиск данных. Они используют хэш-функцию для преобразования ключей
# в индексы массива, что позволяет быстро находить значения по заданным ключам. Предназначены для хранения данных в паре "ключ-значение". Ключ уникален.
# Словарный тип данных реализует принцип структурирования данных, называющийся хэш-таблицей. Каждое значение обладает ключом доступа к нему.
# Все значения хранятся в обычном массиве (скрытом от нас), а в качестве индекса используется результат хэширования ключа.
# Хэширование (в данном случае) - преобразование объекта, выступающего ключом, в целое число - индекс, используемый для доступа к значению. Ключ должен быть уникальным и не изменяемым.

# Односвязный список. Если в памяти хранится указатель только на следующий элемент, то список называется односвязным. Если указатель и на предыдущий и на следующий - двусвязный список.
# Список - упорядоченный набор элементов. Может быть хаотично распределён в памяти (порядок задаётся наличием указателей на следующий/предыдущий элемент в списке).
# Плюсы cписочного способа хранения:
# 1. Вставка элемента в КОЕНЦ списка (происходит за константное время), если в первой ячейке хранится указатель на последний элемент.
# 2. Вставка элемента в НАЧАЛО списка (происходит за константное время), если в первой ячейке хранится указатель на последний элемент.
# 3. Удаление элемента из НАЧАЛА списка (происходит за константное время).

# Минусы:
# 1. Вставка элемента НА ПРОИЗВОЛЬНОЕ МЕСТО.
# 2. Удаление элемента НА ПРОИЗВОЛЬНОЕ МЕСТО.


# Стек - структура данных, реализующая LIFO. (Стопка тарелок)
# Операции: append (добавить элемент на верх стека), pop (удалить элемент с верха стека), peek (посмотреть на верхний элемент стека без его удаления)
# stack = []
# stack.append(1) # push
# stack.append(2) # push
# print(stack.pop())


# Очередь - структура данных, которая работает по принципу FIFO. То есть, первый добавленный элемент будет удалён. (Очередь к врачу)
# Операции: enqueue (добавить элемент в конец очереди), dequeue (удалить элемент из начала очереди), front (посмотреть на первый элемент очереди без его удаления).
# queue1 = []
# queue1.append(1)
# queue1.append(2)
# print(queue1.pop(0))


# Дерево (Tree) - иерархическая структура данных, состоящая из узлов, где каждый узел может иметь несколько дочерних узлов.
# Удобен для представления иерархий (в виде файловой системы)

# Граф (Graph) - набор узлов и рёбер, соединяющих пары узлов.
# Моделирует сложные взаимосвязи (например, социальные сети).