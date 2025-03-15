"""Singleton"""
# Паттерн гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру.
# Подразумевает наличие одного большого объекта, имеющего глобальный доступ ко всему.
# Ситуация: мы хотим создать класс, который будет управлять конфигурацией приложения, и мы хотим, чтобы у него был только 1 экземпляр.

# class Configuration:
#     _instance = None # Хранит единственный экземпляр класса
#
#     def __new__(cls):
#         """Создаём экземпляр (если его ещё нет)
#         new - метод, отвечающий за создание нового экземпляра класса. Вызывается перед init и используется для выделения
#         памяти для нового объекта."""
#         if cls._instance is None:
#             cls._instance = super(Configuration, cls).__new__(cls)
#             cls.set_setting = {} # Инициализируем настройки
#         return cls._instance # Возвращаем единственный экземпляр
#
#     def set_settings(self, key, value):
#         """Устанавливаем значение настройки"""
#         self.set_setting[key] = value
#
#     def get_settings(self, key):
#         """Получаем значение настройки"""
#         return self.set_setting.get(key)
#
#     def __setitem__(self, key, value):
#         """Установление через квадратные скобки"""
#         self.set_settings(key, value)
#
#     def __getitem__(self, key):
#         """Получение через квадратные скобки"""
#         return self.set_setting[key]
#
#
# config1 = Configuration()
# config1['theme'] = 'White'
#
# config2 = Configuration()
# config3 = Configuration()
#
# print(
#     config1['theme'],
#     config2['theme'],
#     config3['theme'],
#     config1 is config2,
#     sep='\n'
# )

"""Lazy Initialization"""
# Lazy Initialization - это подход, при котором объект или ресурс создаётся только в момент, когда он действиетельно необходим, а не заранее.
# Это может помочь сэкономить ресурсы, такие как память и время, особенно если создание объекта является дорогостоящей операцией.

# Преимущества Ленивой Инициализации:
# 1. Экономия ресурсов. Объекты создаются только по мере необходимости;
# 2. Улучшение производительности. Если объект не будет использован, его создание инициализация не пройдёт.
# 3. Упрощение управления зависимостями. Объекты могут быть созданы только тогда, когда они действительно нужны.

# Пример (создание "тяжёлого объекта", например, изображения)

# import time  # Импортируем модуль time для использования функции sleep
#
# class HeavyResource:
#     def __init__(self):
#         # Конструктор класса HeavyResource
#         print('Загружаем данные тяжёлого ресурса...')
#         time.sleep(2)  # Имитация длительной загрузки данных (2 секунды)
#         self.data = 'Данные большого ресурса'  # Инициализация атрибута с данными
#
#     def get_data(self):
#         # Метод для получения данных тяжелого ресурса
#         return self.data  # Возвращаем данные
#
#
# class LazyLoader:
#     def __init__(self):
#         # Конструктор класса LazyLoader
#         self._heavy_recource = None  # Инициализируем приватную переменную для хранения HeavyResource
#
#     @property
#     def heavy_resource(self):
#         # Свойство для доступа к HeavyResource
#         if self._heavy_recource is None:  # Проверяем, был ли уже создан ресурс
#             print('Поступил запрос на создание ресурса')  # Сообщаем о запросе на создание
#             time.sleep(2)  # Имитация задержки перед созданием ресурса (2 секунды)
#             print('Создаём тяжёлый ресурс...')  # Сообщаем о начале создания ресурса
#             time.sleep(2)  # Имитация длительного процесса создания ресурса (2 секунды)
#             self._heavy_recource = HeavyResource()  # Создаем объект HeavyResource и сохраняем его
#         return self._heavy_recource  # Возвращаем созданный или уже существующий ресурс
#
# if __name__ == "__main__":
#     # Основной блок программы
#     loader = LazyLoader()  # Создаем экземпляр LazyLoader
#
#     print('Ресурс ещё не создан...')  # Сообщаем, что ресурс еще не инициализирован
#     time.sleep(2)  # Имитация задержки (2 секунды)
#     resource = loader.heavy_resource  # Запрашиваем heavy_resource, что приведет к его созданию
#     print(resource.get_data())  # Получаем и выводим данные из HeavyResource

"""Builder"""
# Builder (строитель) - паттерн проектирования, использующийся для создания сложных объектов пошагово.
# Он позволяет разделить процесс создания объекта от его представлния, что делает код более гибким и удобным для изменения.
# Паттерн особенно полезен, когда обьект имеет много параметров или когда его создание требует сложной логики.

# Основные компоненты паттерна Builder:
# 1. Builder: Интерфейс или абстрактный класс, который определяет методы для создания частей объекта.
# 2. ConcreteBuilder: Конкретная реализации интерфейса Builder, которая создаёт и собирает части объекта.
# 3. Director. Класс, который управляет процессом создания объекта, используя объект Builder.
# 4. Product. Конечный объект, который создаётся.

# На примере создания объекта Pizza с различными параметрами (размер, тип теста, начинка)

# Продукт
# class Pizza:
#     def __init__(self):
#         self.size = None
#         self.dough = None
#         self.toppings = []
#
#     def __str__(self):
#         return f"Pizza(size={self.size}, dough={self.dough}, toppings={self.toppings})"
#
# # Интерфейс строителя
# class PizzaBuilder:
#     def set_size(self, size):
#         raise NotImplementedError
#
#     def set_dough(self, dough):
#         raise NotImplementedError
#
#     def add_topping(self, topping):
#         raise NotImplementedError
#
#     def build(self):
#         raise NotImplementedError
#
# # Конкретный строитель
# class ConcretePizzaBuilder(PizzaBuilder):
#     def __init__(self):
#         self.pizza = Pizza()
#
#     def set_size(self, size):
#         self.pizza.size = size
#
#     def set_dough(self, dough):
#         self.pizza.dough = dough
#
#     def add_topping(self, topping):
#         self.pizza.toppings.append(topping)
#
#     def build(self):
#         return self.pizza
#
#
# # Директор
# class PizzaDirector:
#     def __init__(self, builder):
#         self.builder = builder
#
#     def make_margherita(self):
#         self.builder.set_size("Medium")
#         self.builder.set_dough("Thin")
#         self.builder.add_topping("Tomato")
#         self.builder.add_topping("Mozzarella")
#         self.builder.add_topping("Basil")
#
#     def make_pepperoni(self):
#         self.builder.set_size("Large")
#         self.builder.set_dough("Thick")
#         self.builder.add_topping("Tomato")
#         self.builder.add_topping("Mozzarella")
#         self.builder.add_topping("Pepperoni")
#
# # Использование
# builder = ConcretePizzaBuilder()
# director = PizzaDirector(builder)
#
# # Создаём пиццу Маргарита
# director.make_margherita()
# pizza1 = builder.build()
# print(pizza1)
#
# # Создаём пиццу Пепперони
# builder = ConcretePizzaBuilder() # Сбрасываем строителя
# director = PizzaDirector(builder)
# director.make_pepperoni()
# pizza2 = builder.build()
# print(pizza2)


"""Фабрика"""
# Паттерн проектирования Фабрика относится к категории порождающих паттернов.
# Он используется для создания объектов, не указывая конкретный класс создаваемого объекта.
# Это позволяет делегировать создание объектов подклассам, что упрощает код и делает его более гибким и расширяемым.

# Существует несколько разновидностей паттерна Фабрика, включая:
# Фабричный метод (Factory Method): определяет интерфейс для создания объекта, но позволяет подклассам изменять тип создаваемого объекта.
# Абстрактная фабрика (Abstract Factory): предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.

# Какие проблемы решаются благодаря Фабрике:

# 1. Сокрытие сложности создания объектов.
# Фабрика позволяет скрыть детали создания объектов от клиента. Вместо того чтобы создавать экземпляры классов напрямую, клентский код взаимодействует с фабрикой,
# которая берёт на себя ответственность за создание объектов. Это упрощает клиентский код и делает его более понятным.

# 2. Упрощение кода. Когда создание объектов сосредоточено в одном месте (фабрике), это упрощает управление зависимостями и уменьшает количество повторяющегося кода.
# Если в будущем потребуется изменить способ создания объектов, это можно сделать в одном месте, не затрагивая остальной код.

# 3. Гибкость и расширяемость. Фабрика позволяет добавлять новые типы объектов без изменения существующего кода.
# Например, Если мы хотим добавить новый тип автомобиля, нам нужно только создать новый класс и соответствующую фабрику, не изменяя код, который использует фабрики.

# 4. Инкапсуляция логики создания объектов. Фабрика может содержать логику, необходимую для создания объектов, н-р, выбор конкретного класса на основе параметров или конфигурации.
# Это позволяет более гибко управлять процессом создания объектов.

# 5. Поддержка принципа открытости/закрытости. Поддерживает принцип (Open/Closed Principle), гласящий, что классы должны быть открыты для расширения, но закрыты для модификации.
# Мы можем добавлять новые классы и фабрики, не изменяя существующий код.

# 6. Упрощение тестирования. Поскольку можно легко подменять реальные фабрики на моки или стабы. Это позволяет изолировать тестируемый код и контролировать, какие объекты создаются.

# Пример применения: приложение работает с различными типами платежей (кредитные карты, PayPal, криптовалюты и т.д.). Вместо того чтобы создавать объекты платежей напрямую в коде, можно использовать фабрику,
# которая будет создавать нужный тип платежа в зависимости от условий (например, тип платежа, выбранного пользователем). Это делает код более чистым и лёгким для изменения.


# На примере создания фабрики для различных типов автомобилей

# from abc import ABC, abstractmethod
#
# # Интерфейс продукта
# class Car(ABC):
#     @abstractmethod
#     def drive(self):
#         """Метод для вождения автомобиля (должен быть реализован в подклассах)"""
#         pass
#
# # Конкретные продукты
# class Sedan(Car):
#     def drive(self):
#         """Реализация метода для седана"""
#         return "Driving a sedan."
#
# class SUV(Car):
#     def drive(self):
#         """Реализация метода для внедорожника"""
#         return "Driving an SUV."
#
# # Фабрика - определяет интерфейс для создания объектов типа `Car`
# class CarFactory(ABC):
#     @abstractmethod
#     def create_car(self) -> Car:
#         """Метод для создания автомобиля (должен быть реализован в подклассах)"""
#         pass
#
# # Конкретные фабрики - реализуют метод `create_car`, создавая конкретные типы автомобилей.
# class SedanFactory(CarFactory):
#     def create_car(self) -> Car:
#         """Создаёт и возвращает объект типа Sedan."""
#         return Sedan()
#
# class SUVFactory(CarFactory):
#     def create_car(self) -> Car:
#         """Создаём и возвращает объект типа SUV"""
#         return SUV()
#
# # Клиентский код
# def client_code(factory: CarFactory):
#     """Функция, использующая фабрика для создания автомобиля и его вождения"""
#     car = factory.create_car() # Создаём автомобиль через фабрику
#     print(car.drive())
#
# # Использование
# if __name__ == "__main__":
#     # Создаём фабрику для седанов
#     sedan_factory = SedanFactory()
#     client_code(sedan_factory) # Вывод: Driving a sedan.
#
#     # Создаём фабрику для внедорожников
#     suv_factory = SUVFactory()
#     client_code(suv_factory) # Вывод: Driving an SUV.



from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        return "Driving a Sedan."

class SUV(Car):
    def drive(self):
        return "Driving a SUV."

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()

def client_code(factory: CarFactory):
    car = factory.create_car()
    print(car.drive())


if __name__ == "__main__":
    # Создать экземпляр седана
    sedan_factory = SedanFactory()
    client_code(sedan_factory)

    # Создать экземпляр внедорожника
    suv_factory = SUVFactory()
    client_code(suv_factory)

















