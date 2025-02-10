"""Паттерны проектирования"""
# # ПП - обобщающее решение часто встречающихся проблем в разработке ПО.
# # ПП - проверенные временем подходы к проектированию, позволяющие создавать гибкие, поддерживающие и масштабируемые системы.
# # ПП - способы построения программ, которые считаются хорошим тоном для разработчиков.
# # Паттерн - типовое решение часто встречающейся задачи на построение.
# # Статья: https://blog.skillfactory.ru/glossary/pattern/

# # 1. Порождающие паттерны (Creational Patterns) - касаются процесса создания объектов. Они помогают сделать систему
# # более независимой от способа создания, компоновки и представления объектов.

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


# # Abstract Factory - предоставляет интерфейс для создания семейств связанных или зависимых объектов без указания их конкретных классов.
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


# # Builder - разделяет конструирование сложного объекта и его представление, так что один и тот же процесс строительства
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


















