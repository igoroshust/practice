import unittest
from unittest.mock import patch
import pytest
from javacode import add, name, subtract

@pytest.mark.parametrize("input_value, expected", [
    ('igor', 'igor'),  # Входное и ожидаемое значение
    ('alice', 'alice'),
])
def test_name_valid(input_value, expected):
    result = name(input_value)  # Прямой вызов функции
    assert result == expected

@pytest.mark.parametrize("input_value", [
    ('Андрей'),
    ('Николай'),
])
def test_name_invalid(input_value):
    with pytest.raises(ValueError, match="Неправильное имя"):
        name(input_value)  # Прямой вызов функции

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (1, 3, 4),
    (1, 5, 6),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (2, 1, 1),
    (2, 3, -1),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected









"""Параметризация тестов (pytest)"""
# @pytest.mark.parametrize("a, b, expected", [
#     (1, 2, 3),
#     (-1, 1, 0),
#     (-1, -1, -2),
# ])
#
# def test_add(a, b, expected):
#     assert add(a, b) == expected
#
# @pytest.mark.parametrize("a, b, expected", [
#     (2, 1, 1),
#     (2, 2, 0),
#     (2, 3, -1),
# ])
#
# def test_subtract(a, b, expected):
#     assert subtract(a, b) == expected



"""Пример использования для pytest"""
# def test_add():
#     assert add(1, 2) == 3
#     assert add(-1, 1) == 0
#     assert add(-1, -1) == -2
#
# def test_subtract():
#     assert subtract(2, 1) == 1
#     assert subtract(2, 2) == 0
#     assert subtract(2, 3) == -1
#
# # запуск по команде pytest



"""Пример использования для unittest"""
# class TestCalculator(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(1, 2), 3)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(-1, -1), -2)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(2, 1), 1)
#         self.assertEqual(subtract(2, 2), 0)
#         self.assertEqual(subtract(2, 3), -1)
#
# if __name__ == "__main__":
#     unittest.main()

# # Запуск тестов производится командой: python -m unittest %filename.py%