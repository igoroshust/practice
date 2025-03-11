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
class Pizza:
    def __init__(self):
        self.size = None
        self.dough = None
        self.toppings = []

    def __str__(self):
        return f"Pizza(size={self.size}, dough={self.dough}, toppings={self.toppings})"

# Интерфейс строителя
class PizzaBuilder:
    def set_size(self, size):
        raise NotImplementedError

    def set_dough(self, dough):
        raise NotImplementedError

    def add_topping(self, topping):
        raise NotImplementedError

    def build(self):
        raise NotImplementedError

# Конкретный строитель
class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size

    def set_dough(self, dough):
        self.pizza.dough = dough

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)

    def build(self):
        return self.pizza


# Директор
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_margherita(self):
        self.builder.set_size("Medium")
        self.builder.set_dough("Thin")
        self.builder.add_topping("Tomato")
        self.builder.add_topping("Mozzarella")
        self.builder.add_topping("Basil")

    def make_pepperoni(self):
        self.builder.set_size("Large")
        self.builder.set_dough("Thick")
        self.builder.add_topping("Tomato")
        self.builder.add_topping("Mozzarella")
        self.builder.add_topping("Pepperoni")

# Использование
builder = ConcretePizzaBuilder()
director = PizzaDirector(builder)

# Создаём пиццу Маргарита
director.make_margherita()
pizza1 = builder.build()
print(pizza1)

# Создаём пиццу Пепперони
builder = ConcretePizzaBuilder() # Сбрасываем строителя
director = PizzaDirector(builder)
director.make_pepperoni()
pizza2 = builder.build()
print(pizza2)