"""Паттерны проектирования"""
# # ПП - обобщающее решение часто встречающихся проблем в разработке ПО.
# # ПП - проверенные временем подходы к проектированию, позволяющие создавать гибкие, поддерживающие и масштабируемые системы.
# # ПП - способы построения программ, которые считаются хорошим тоном для разработчиков.
# # Паттерн - типовое решение часто встречающейся задачи на построение.
# # Статья: https://blog.skillfactory.ru/glossary/pattern/

# # 1. Порождающие паттерны (Creational Patterns) - касаются процесса создания объектов. Они помогают сделать систему
# # более независимой от способа создания, компоновки и представления объектов.

"""Паттерны создания (singleton, factory, abstract factory, builder, builder). 
Эти паттерны касаются процесса создания объектов. 
Они помогают сделать систему независимой от способа создания, компоновки и представления объектов."""

"""Singleton"""
# > Singleton (одиночка) - подразумевает наличие одного большого объекта, имеющего глобальный доступ ко всему.
# Гарантирует, что класс имеет только один экземпляр и предоставляет глобальную точку доступа к нему.
# Ситуация: нужно создать класс, который будет управлять конфигурацией приложения, и мы хотим, чтобы у него был только
# # один экземпляр

# class Configuration:
#     _instance = None # Хранит единственный экземпляр класса
#
#     def __new__(cls):
#         """Создаём новый экземпляр (если ещё не создан)"""
#         if cls._instance is None:
#             cls._instance = super(Configuration, cls).__new__(cls)
#             cls._instance.settings = {} # Инициализируем настройки
#         return cls._instance # Возвращаем единственный экземпляр
#
#     def set_setting(self, key, value):
#         self.settings[key] = value # Устанавливаем значение настройки
#
#     def get_setting(self, key):
#         return self.settings.get(key) # Получаем значение настройки по ключу
#
# # Использование
# config1 = Configuration() # Создаём первый экземпляр
# config1.set_setting('theme', 'dark') # Устанавливаем настройку
#
# config2 = Configuration() # Попытка создать второй экземпляр
# print(config2.get_setting('theme'))  # Вывод: dark (настройка доступна)
# print(config1 is config2)  # Вывод: True (оба экземпляра ссылаются на один и тот же объект)


"""Lazi Initialization"""
# # > Lazy Initialization - техника, при которой объект создаётся только в тот момент, когда он действительно необходим,
# # а не в момент инициализации программы. Это полезно для экономии ресурсов, особенно если создание объекта является дорогостоящей операцией.
# # Ситуация: создадим класс `DatabaseConnection`, который будет использовать Lazy Initialization для создания единственного
# # экземпляра соединения с базой данных.

# # Реализация Lazy Initialization на примере Singleton:

# class DatabaseConnection:
#     _instance = None # Хранит единственный экземпляр класса
#
#     def __new__(cls):
#         """Создаём новый экземпляр (если ещё не создан)"""
#         if cls._instance is None:
#             cls._instance = super(DatabaseConnection, cls).__new__(cls) # Создаём новый экземпляр
#             cls._instance.initialize() # Инициализируем экземпляр (+ установление соединения с БД)
#         return cls._instance # Возвращаем единственный экземпляр
#
#     def initialize(self):
#         """Здесь можно выполнить дорогостоящие операции, например, установить соединение с БД"""
#         self.connection_string = 'Database connection established.'
#         print(self.connection_string) # Выводим сообщение об установлении соединения
#
#
# # Использование
# db1 = DatabaseConnection() # Создаём первый экземпляр
# db2 = DatabaseConnection() # Пытаемся создать второй экземпляр
#
# print(db1 is db2) # Вывод: True (оба экземпляра ссылаются на один и тот же объект)


"""Factory"""
# > Factory (фабрика) - для создания новых объектов придумывают отдельный класс. Он создаёт объекты как копии некоего эталона.
# Это когда создают отдельный класс для создания новых объектов.
# Ситуация: есть несколько типов уведомлений (Email, SMS), мы хотим создать их без жёсткой привязкии к конкретным классам.

# class Notification:
#     def notify(self):
#         raise NotImplementedError("Subclass should implement this!")
#
# class EmailNotification(Notification):
#     def notify(self):
#         return "Sending an email notification." # Реализация для Email
#
# class SMSNotification(Notification):
#     def notify(self):
#         return "Sending an SMS notification." # Реализация для SMS
#
# class NotificationFactory:
#     @staticmethod
#     def create_notification(type):
#         """Создаём уведомление в зависимости от типа"""
#         if type == "email":
#             return EmailNotification() # Возвращаем email-уведомление
#         elif type == "sms":
#             return SMSNotification() # Возвращаем SMS-уведомление
#         else:
#             raise ValueError("Unknown notification type.") # Обработка неизвестного типа
#
# # Использование
# notification = NotificationFactory.create_notification("email") # Создаём Email-уведомление
# print(notification.notify()) # Вывод: Sending an email notification.

"""Abstract Factory"""
# # > Abstract Factory - предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.
# # Ситуация: вы разрабатываете кросс-платформенное приложение и вам нужно создать интерфейсы для различных платформ (Windows, Mac).

# class Button:
#     def paint(self):
#         raise NotImplementedError('Subclasses should implement this.')
#
# class WindowsButton(Button):
#     def paint(self):
#         return "Windows button"
#
# class MacButton(Button):
#     def paint(self):
#         return "Mac button"
#
# class GUIFactory:
#     def create_button(self):
#         raise NotImplementedError('Subclasses should implement this.')
#
# class WindowsFactory(GUIFactory):
#     def create_button(self):
#         return WindowsButton() # Создаём Windows-кнопку
#
# class MacFactory(GUIFactory):
#     def create_button(self):
#         return MacButton() # Создаём Mac-кнопку
#
# # Использование
# def client_code(factory: GUIFactory):
#     button = factory.create_button() # Создаём кнопку через фабрику
#     print(button.paint()) # Выводим результат рендеринга кнопки
#
# # Выбор фабрики в зависимости от платформы
# platform = 'Windows'
#
# if platform == 'Windows':
#     factory = WindowsFactory()
# else:
#     factory = MacFactory()
#
# client_code(factory) # Вывод: Rendering a button in Windows style.

"""Builder"""
# # > Builder - разделяет конструирование сложного объекта и его представление, так что один и тот же процесс строительства
# # может создавать разные представления. Похож на фабрику, но новые объекты можно модифицировать. Они создаются по сложной логике,
# # а не клонируют эталонный.
# # Ситуация: вы хотите создать сложный объект, например, дом, который может иметь различные компоненты (крыша, стены, окна и т.д.).

# class House:
#     def __init__(self):
#         self.roof = None # Инициализация крыши
#         self.walls = None
#         self.windows = None
#
#     def __str__(self):
#         """Строковое представление дома с его компонентами"""
#         return f"House with {self.roof}, {self.walls}, and {self.windows}"
#
# class HouseBuilder:
#     def __init__(self):
#         self.house = House() # Создаём новый объект House
#
#     def build_roof(self, roof_type):
#         self.house.roof = roof_type # Устанавливаем тип крыши
#         return self # Возвращаем текущий объект для цепочки вызовов
#
#     def build_walls(self, wall_type):
#         self.house.walls = wall_type # Устанавливаем тип стен
#         return self
#
#     def build_windows(self, window_type):
#         self.house.windows = window_type # Устанавливаем тип окон
#         return self
#
#     def build(self):
#         return self.house # Возвращаем готовый объект House
#
# # Использование
# builder = HouseBuilder() # Создаём строителя
# house = (builder
#          .build_roof('Gable Roof') # Устанавливаем крышу
#          .build_walls('Brick Walls') # Устанавливаем стены
#          .build_windows('Double Glazed Windows') # Устанавливаем окна
#          .build()) # Завершаем строительство и получаем объект House
#
# print(house)

"""Prototype"""
# # > Prototype - Создает новые объекты путём копирования существующих. Объект сам создаёт свои копии.
# # Ситуация: есть объект, который вы хотите клонировать, чтобы создать новые экземпляры с теми же свойствами.

# import copy
#
# class Prototype:
#     def clone(self):
#         return copy.deepcopy(self) # Глубокая копия текущего объекта
#
# class ConcretePrototype(Prototype):
#     def __init__(self, name):
#         self.name = name # Инициализируем имя объекта
#
#     def __str__(self):
#         return f'Prototype with name: {self.name}' # Возвращаем строковое представление
#
# # Использование
# original = ConcretePrototype("Original") # Создаём оригинальный объект
# print(original) # Вывод: Prototype with name: Original
#
# cloned = original.clone() # Клонируем оригинальный объект
# cloned.name = "Cloned"
#
# print(cloned)  # Вывод: Prototype with name: Cloned
# print(original)  # Вывод: Prototype with name: Original (оригинал не изменился)


"""Структурные паттерны (Structural Patterns). 
Эти паттерны касаются компоновки классов и объектов, чтобы образовывать более крупные структуры
(Adapter, Decorator, Facade, Composite, Proxy)"""

"""Adapter"""
# Паттерн Adapter (Адаптер) используется для обеспечения совместимости между двумя несовместимыми интерфейсами.
# Он позволяет объектам с разными интерфейсами работать вместе, действуя как промежуточное звено,
# которое преобразует интерфейс одного объекта в интерфейс, ожидаемый другим объектом.

# # Основные характеристики паттерна Адаптер
# 1. Совместимость. Позволяет взаимодействовать классам, которые не могут работать вместе из-за несовместимости интерфейсов.
# 2. Инкапсуляция. Адаптер инкапсулирует логику преобразования, что позволяет клиентскому коду оставаться чистым и простым.
# 3. Гибкость. Позволяет легко добавлять новые классы, не изменяя существующий код.

# # Примущества паттерна Adapter:
# 1. Позволяет интегрировать устаревшие системы с новыми без изменения их кода.
# 2. Упрощает работу с различными интерфейсами, предоставляя единый интерфейс для клиента.
# 3. Увеличивает гибкость и расширяемость системы, позволяя легко добавлять новые классы и адаптировать их к существующим интерфейсам.

# Паттерн "Adapter" широко используется в различным приложениях, особенно в тех случаях, когда необходимо интегрировать сторонние библиотеки или устаревшие системы.

# # Пример. Создадим два класса `OldSystem`, который имеет устаревший интерфейс, и `NewSystem`, который имеет современный интерфейс.
# Создадим `Adapter`, который позволит `OldSystem` работать с `NewSystem`.

# Устаревшая система с несовместимым интерфейсом
# class OldSystem:
#     def specific_request(self):
#         return 'Данные из устаревшей системы'
#
# # Новый интерфейс, который мы хотим использовать
# class NewSystem:
#     def request(self):
#         return 'Данные из новой системы'
#
# # Адаптер, который позволяет OldSystem работать с NewSystem
# class Adapter:
#     def __init__(self, old_system):
#         self.old_system = old_system
#
#     def request(self):
#         # Преобразуем вызов из нового интерфейса в старый
#         return self.old_system.specific_request()
#
#
# # Пример использования
# if __name__ == "__main__":
#     # Создаём экземпляр устаревшей системы
#     old_system = OldSystem()
#
#     # Создаём адаптер для устаревшей системы
#     adapter = Adapter(old_system)
#
#     # Теперь мы можем использовать адаптер как новый интерфейс
#     print("Используем адаптер для получения данных:")
#     print(adapter.request())
#
#     # Пример использования нового интерфейса
#     new_system = NewSystem()
#     print("Используем новую систему напрямую:")
#     print(new_system.request())


"""Декоратор"""
# Паттерн проектирования Decorator (Декоратор) - это структурный паттерн, который позволяет динамически добавлять объектам новые обязанности, оборачивая их в другие объекты.
# Этот паттерн предоставляет гибкий способ расширения функциональности объектов, не изменяя их исходный код.
# Паттерн Декоратор позволяет гибко добавлять новые возможности к объектам, не изменяя их исходный код.

# Зачем нужен паттерн:
# 1. Расширяемость. Позволяет добавлять новые функциональные возможности к объектам без изменения их структуры.
# 2. Композиция. Позволяет комбинировать различные декораторы для создания сложных объектов с множеством обязанностей.
# 3. Избежание наследования. Уменьшает необходимость создания большого количества подклассов для добавления функциональности.

## Пример. У нас есть базовый класс `Coffee`, и мы хотим добавить различные добавки (молоко, сахар), используя паттерн Декоратор.

# class Coffee:
#     def cost(self):
#         return 5 # базовая цена кофе
#
# class MilkDecorator:
#     def __init__(self, coffee):
#         self._coffee = coffee
#
#     def cost(self):
#         return self._coffee.cost() + 1 # добавляем стоимость молока
#
# class SugarDecorator:
#     def __init__(self, coffee):
#         self._coffee = coffee
#
#     def cost(self):
#         return self._coffee.cost() + 0.5 # добавляем стоимость сахара
#
# # Использование
#
# if __name__ == "__main__":
#     # Заказ обычного кофе
#     my_coffee = Coffee()
#     print('Стоимость обычного кофе:', my_coffee.cost())
#
#     # Заказ кофе с молоком
#     my_coffee_with_milk = MilkDecorator(my_coffee)
#     print('Стоимость кофе с молоком:', my_coffee_with_milk.cost())
#
#     # Заказ кофе с сахаром
#     my_coffee_with_sugar = SugarDecorator(my_coffee_with_milk)
#     print('Стоимость кофе с сахаром:', my_coffee_with_sugar.cost())

"""Facade"""
# Паттерн проектирования Facade (фасад) - это структурный паттерн, который предоставляет упрощённый интерфейс к сложной системе классов, библиотек
# или фреймворков. Он служит для скрытия сложности системы и упрощения взаимодействия с ней.

# Основные цели и преимущества использования паттерна Facade:
# 1. Упрощение интерфейса. Facade предоставляет более простой и понятный интерфейс для работы с сложной системой, что делает её использование более удобным.
# 2. Скрытие сложности. Паттерн позволяет скрыть детали реализации и внутренние взаимодействия между компонентами системы, что делает код более чистым и понятным.
# 3. Снижение зависимости. Использование фасада помогает уменьшить количество зависимостей между клиентским кодом и сложной системой, что улучшает тестирование и модификацию кода.
# 4. Улучшение читаемости. Код становится более читаемым и поддерживаемым, так как разработчики могут работать с выокоуровневым интерфейсом, не углубляясь в детали реализации.

# Пример использования.
# Допустим, у нас есть сложная система для обработки заказов, которая включает в себя классы для управления пользователями, продуктами, платежами и доставкой.
# Вместо того чтобы взаимодействовать с каждым из этих классов напрямую, вы можете создать фасад, который будет предоставлять методы для выполнения общих операций,
# таких как создание заказа, обработка платежа и организация доставки.

# class User:
#     def login(self, username, password):
#         pass
#
# class Product:
#     def __init__(self):
#         # Пример базы данных продуктов
#         self.products = {
#             123: 'Product A',
#             456: 'Product B',
#         }
#
#     def get_product_details(self, product_id):
#         return self.products.get(product_id, None)
#
# class Payment:
#     def process_payment(self, amount):
#         pass
#
# class Delivery:
#     def schedule_delivery(self, address):
#         pass
#
# class OrderFacade:
#     def __init__(self):
#         self.user = User()
#         self.product = Product()
#         self.payment = Payment()
#         self.delivery = Delivery()
#
#     def create_order(self, username, password, product_id, amount, address):
#         self.user.login(username, password)
#         product_details = self.product.get_product_details(product_id)
#         self.payment.process_payment(amount)
#         self.delivery.schedule_delivery(address)
#         return f"Order for {product_details} has been created and will be delivered to {address}."
#
# # Использование фасада
# order_facade = OrderFacade()
# result = order_facade.create_order("user1", "password", 123, 100, "123 Main St")
# print(result)

