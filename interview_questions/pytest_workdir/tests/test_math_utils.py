# from interview_questions.pytest_workdir.math_utils import add, divide
import pytest
import requests

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError('Division by zero!')
    return a / b

"""Мокирование"""
def fetch_user(id):
    response = requests.get(f'https://api.example.com/user/{id}')
    return response.json()

def test_fetch_user(mocker): # mocker - fixture из pytest-mock
    # Mock: подменяем requests.get
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'id': 1, 'name': 'Test'}
    mocker.patch('requests.get', return_value=mock_response)

    result = fetch_user(1)
    assert result['name'] == 'Test'
    mock_response.json.assert_called_once() # Проверили вызов


"""Параметризация"""
# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 5),
#     (-1, -1, -2),
#     (0, 5, 5),
#     pytest.param(1, 'a', None, marks=pytest.mark.xfail) # Ожидаемый fail
#     # param - специальный объект для создания строк данных с доп.опциями (marks)
# ])
#
# def test_add_parametrized(a, b, expected):
#     if expected is None:
#         with pytest.raises(TypeError):
#             add(a, b)
#     else:
#         assert add(a, b) == expected
#
# @pytest.mark.slow
# def test_long_running():
#     assert True # Имитация
#
# @pytest.mark.smoke # Быстрые smoke-тесты
# def test_basic():
#     assert 1 == 1

"""Фикстуры"""
# @pytest.fixture
# def sample_data():
#     # Подготовка: возвращаем данные
#     return [2, 3, -1] # Список для тестов
#
# @pytest.fixture(autouse=True) # Автоматически для всех тестов
# def setup_logging():
#     print('Начало тестирования') # Вызывается перед каждым тестом
#     yield # Точка выполнения теста
#     print('Конец тестирования') # Очистка после
#
# def test_add_with_fixture(sample_data):
#     # sample-data - автоматически подставляется
#     result = add(sample_data[0], sample_data[1])
#     assert result == 5
#
# def test_negative_with_fixture(sample_data):
#     result = add(sample_data[2], sample_data[2])
#     assert result == -2
#
# """Первое знакомство"""
# def test_add_positive():
#     assert add(2, 3) == 5 # Просто assert
#
# def test_add_negative():
#     assert add(-1, -1) == -2
#
# def test_add_zero():
#     assert add(0, 5) == 5
#
# def test_divide_normal():
#     assert divide(10, 2) == 5.0
#
# def test_divide_zero():
#     # Проверка исключения
#     with pytest.raises(ValueError, match="Divisin by zero"):
#         divide(10, 0)