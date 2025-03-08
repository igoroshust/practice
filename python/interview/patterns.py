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















