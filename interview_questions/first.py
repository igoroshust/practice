# Пользовательские классы
# функция help


"""Какие типы данных есть в Python?"""
# Числа: int, float, complex
# Строки: str
# Списки: list
# Кортежи: tuple
# Словари: dict
# Множества: set
# Булевы значения: bool

# Эти типы данных можно объединить в такие группы:
# Числовые типы данных: int, float, complex
# Строковые типы данных: str
# Коллекции: list, tuple, dict, и set.
# Булевы типы данных: bool.

# Иерархия типов данных: https://skrinshoter.ru/sUuEz2a6r3M
# None (class NoneType)
# Numbers: Intergral: Integer (class int), Booleans (class bool); Real (class float); Complex (class complex)
# Sequences: Immutable: Strings (class str), Tuples (class tuple), Bytes (class bytes); Mytable: Lists (class list), Byte Arrays (class bytearray);
# Set Types: Sets (class set), Frozen sets (class frozenset)
# Mappings: Dictionaries (class dict)
# Callable: <Functions, Methods, Classes>
# Modules

"""Что такое лямбда-функиця? Какое у неё назначение?"""
# Лямбда-фукнция (она же анонимная функция) - это функция, которая определяется в одной строке кода без использования ключевого слова `def`.
# Она может быть использована вместо обычной функции, когда требует быстрое определение небольшой функции.
# Как правило, лямбда-функции - одноразовые.

# Лямбда-функция определяется с помощью ключевого слова lambda, за которым следует список аргументов через запятую, затем символ `:`, после - тело.
# double = lambda x: x*2
# Лямбда используются к качестве аргументов функций высшего порядка, которые принимают другие функции в качестве аргументов.
# Также они могут использоваться для создания более читаемого и компактного кода.

# Пример использования для преобразования списка
# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x**2, numbers))
# even_numbers = list(filter(lambda x: x%2 == 0, numbers))

# Передаём lambda в качестве аргумента key для сортировки
# mylist = ['111', '22', '3']
# mylist = sorted(mylist, key=lambda x: len(x))
# print(mylist)

"""Что такое docsting?"""
# Docstring - это строка документации, описывающая, что делает функция, метод, модуль или класс Python.
# Данная строка располагается в начале определения объекта и используется для генерации документации автоматически.
# Docstring используется для создания описания API и содержит информацию о том, как использовать функцию или метод,
# какие аргументы они принимают и какие значения возвращают.

# def add_numbers(a, b):
#     """
#     This function takes in two numbers and returns their sum
#     """
#     return a + b
#
# print(add_numbers.__doc__)
# help(add_numbers)

"""Что такое дандер методы?"""
# Дандер методы (или магические методы) в Python - это специальные методы, которые начинаются и заканчиваются двумя подчёркиваниями
# Например: `__init__`, `__new__`, `__add__`.
# Они позволяют определять поведение объектов пользовательских классов в различных ситуациях, таких как создание, представление,
# сравнение и арифметические операции.

# Зачем они нужны?
# 1. Переопределение поведения: дандер методы позволяют переобпределять стандартное поведение операторов и встроенных функций.
# Например, с помощью метода `__add__` можно определить, как будет работать оператор `+` для объектов вашего класса.

# 2. Интерфейс. Они обеспечивают интерфейс для взаимодействия с объектами.
# Например, метод `__str__` позволяет задать, как объект будет представлен в виде строки, когда мы вызываем `print()`.

# 3. Инкапсуляция логики: дандер методы помогают инкапсулировать логику, связанную с определёнными действиями, в самих классах,
# что делает код более чистым и понятным.

# Чем отличаются от других функций и методов?
# 1. Специальное назначение. Дандер методы имеют специальное назначение и вызываются автоматически в определённых ситуациях.
# Н-р, `__init__` вызывается при создании объекта, а `__add__` - при использовании оператора `+`.

# 2. Именование. Они имеют строгое именование, которое начинается и заканчивается двумя подчёркиваниями.

# 3. Автоматический вызов. Дандер методы не вызываются напрямую, как обычные методы.
# Они вызываются автоматически интерпретатором Python в ответ на определённые действия (создание объекта, выполнение арифметических операций)

# Примеры dander methods:
# 1. `__init__`: Конструктор класса, вызывается при создании нового объекта
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# # 2. `__str__`: Определяет строковое представление объекта
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

# # 3. `__add__`: позволяет переопределить оператор сложения.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

# Итог: дандер методы являются мощным инструментом для создания гибких и интуитивно понятных классов в Python, позволяя разработчикам
# определять, как их объекты должны вести себя в различных контекстах.

"""Как получить докумнетацию по атрибутам объекта?"""
# Кратко: с помощью .__doc__ (или help)

# class MyClass:
#     """This is the docstring for MyClass."""
#     attribute_name = "value"
#
# print(MyClass.attribute_name.__doc__) # None

# class MyClass:
#
#     def __init__(self, attr1: int, attr2: str):
#         self.attr1 = attr1  # Значение атрибута attr1
#         self.attr2 = attr2  # Значение атрибута attr2
#
# # Создание экземпляра класса
# my_instance = MyClass(10, "Hello")
#
# # Получение доступа к документации класса
# print(MyClass.__doc__)
#
# # Получение доступа к документации атрибутов экземпляра
# # Обратите внимание, что у атрибутов экземпляра нет docstring
# # Но вы можете получить доступ к их значениям
# print(my_instance.attr1)  # 10
# print(my_instance.attr2)  # Hello


"""В чём разница между типами list и tuple?"""
# 1. Они являются различными типами данных, которые предоставляют набор элементов в определённом порядке.
# 2. Список может быть изменён, кортеж - нет.
# 3. Кортежи более эффективным по памяти и даёт гарантию того, что их содержимое не будет изменено случайно в коде.
# 4. Котрежи обрабатываются быстрее, чем списки.
# 5. Синтаксис разный: круглые скобки против квадратных.


"""Что значит конструкция pass?"""
# pass является пустым оператором. Он используется там, где синтаксически требуется оператор, но никаких действий выполнять не нужно.


"""Чем отличается многопоточное и прогопроцессорное приложение"""
# Многопоточное и многопроцессорное приложения отличаются друг от друга в том, как они используют ресурсы компьютера.
# В многопроцессорных приложениях каждый процесс имеет свой собственный набор ресурсов, включая память, открытые файлы, сетевые соединения и другие системные ресурсы.
# Многопроцессорность в Python может быть достигнута с помощью библиотек multiporcessing и concurrent.futures.

# В многопоточных приложениях несколько потоков выполняются в рамках одного процесса, используя общие ресурсы. Это означает, что все потоки имеют доступ к общим данным.
# Реализация многопоточности в Python выполняется за счёт стандартной библиотеки threading.

# При правильном использовании оба подхода могут ускорить выполнение программы и улучшить управляемость ею, однако многопоточное приложение может иметь проблемы с блокироваками
# и условиями гонки при доступе к общим ресурсам. В многопроцессорных приложениях каждый процесс защищён от других процессов и обеспечивает более высокую степень изоляциии.

# Многопоточность и многопроцессность - это два подхода к параллельному выполнению задач в программировании. Оба метода позволяют улучшить производительность приложений,
# особенно на многоядерных процессорах, но они имеют свои особенности и области применения.

# Многопоточность - подразумевает использование нескольких потоков (threads) в рамках одного процесса. Потоки разделяюет память и ресурсы процесса, что позволяем им легко обмениваться данными.
# Однако это также может привести к проблемам с синхронизацией и состоянием гонки (race conditions).
# В Python для работы с потоками используется threading

import threading
import time

def worker(thread_number):
    print(f"Поток {thread_number} начал работу")
    time.sleep(2)
    print(f"Поток {thread_number} завершил работу")


threads = []
for i in range(5):
    thread = threaing.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() # Ожидание завершения всех потоков

print("Все потоки завершены")

# Многопроцессность - подразумевает использование нескольких процессов, каждый из которых имеет свою собственную память и ресурсы. Это позволяет избежать проблем с синхронизацией, но обмен данными между процессами
# может быть более сложным и медленнным. Работает с модулем multiprocessing

import multiprocessing
import time

def worker(process_number):
    print(f'Процесс {process_number} начал работу')
    time.sleep(2)
    print(f'Процесс {process_number} завершил работу')

if __name__ == "__main__":
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=worker, args=(i, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

print('Все процессы завершены')

# Сравнение
# 1. Память. Потоки разделяют память, процессы имеют отдельные области памяти.
# 2. Скорость. Потоки могут быть быстрее в обмене данными, но требуют синхронизации. Процессы медленнее в обмене данными, но проще в плане управления состоянием.
# 3. Использование CPU: многопроцессность может лучше использовать многоядерные процессоры, так как каждый процесс может выполняться на отдельном ядре.
# В Python, из-за GIL, многопоточность может не дать ожидаемого прироста производительности для CPU-bound задач.

# Заключение
# Выбор между многопоточностью и многопроцессностью зависит от конкретной задачи. Если задача требует интенсивных вычислений, лучше использовать многопроцессность.
# Если работаем с I/O-bound задачами (например, сетевые запросы), многопоточность может быть подходящим вариантом.
