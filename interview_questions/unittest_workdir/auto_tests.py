import unittest

def add(a, b):
    """Тестируемая функция"""
    return a + b

def divide(a, b):
    return a / b


# class TestAddFunction(unittest.TestCase):
#     """Автотест для функции add"""
#     # def setUp(self):
#     #     # Метод выполнится до тестов (подготовка данных, создание объектов)
#     #     self.value = 10 # self.assertEqual(self.value + 5, 15)
#
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(2, 3), 5)
#
#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -1), -2)
#
#     def test_add_zero(self):
#         self.assertEqual(add(1, 0), 1)
#
#     def test_not(self):
#         # Проверка неравенства
#         self.assertNotEqual(add(3, 8), 4) # 11 != 4 - ОК
#
#     def test_true(self):
#         # Проверка истинности
#         self.assertTrue(add(4, 4) > 4) # 8 > 4 - True, OK
#
#     def test_false(self):
#         self.assertFalse(add(0, 5) == 1)
#
#     def test_iden(self):
#         # Проверка идентичности (тот же объект в памяти)
#         result = add(1, 4)
#         self.assertIs(type(result), int)
#
#     def test_none(self):
#         # Проверяет, что значение None
#         self.assertIsNone(add(0, 0) if False else None)
#
#     def test_in(self):
#         self.assertIn(6, [add(3, 3), 12]) # 6 в списке - ОК
#
#     # Проверяет, что код вызывает исключение
#     with self.assertRaises(TypeError): # Ожидаем TypeError
#         multiply("a", 3)

    # def tearDown(self):
    #     # Метод сработает после отработки тестов (закрыть соединение с БД, удалить лишние файлы, чистить кэщ)
    #     self.value = ''


if __name__ == "__main__":
    unittest.main(verbosity=2)


# class TestDivision(unittest.TestCase):
#     def test_divistion_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             divide(2, 0)