import unittest
from interview_questions.UserValidatorExample.user_validator import UserValidator

class TestUserValidatorReal(unittest.TestCase):
    def setUp(self):
        self.validator = UserValidator() # Создаём экземпляр

    def tearDown(self):
        pass

    def test_valid_user(self):
        # Нормальный кейс: валидные данные
        # data - данные на вход функции validate_user (UserValidation)
        data = {'email': 'user@example.com', 'age': 25}
        errors = self.validator.validate_user(data)
        self.assertEqual(errors, {}) # Нет ошибок

    def test_invalid_email(self):
        # Edge-кейс: неверный email
        data = {'email': 'invalid-email', 'age': 30}
        errors = self.validator.validate_user(data)
        self.assertIn('email', errors)
        self.assertEqual(errors['email'], 'Invalid email format')

    def test_invalid_age(self):
        # Edge-кейс: возраст вне диапазона
        data = {'email': 'test@example.com', 'age': 15}
        errors = self.validator.validate_user(data)
        self.assertIn('age', errors)
        self.assertEqual(errors['age'], 'Age must be between 18 and 100')

    def test_missing_fields(self):
        # Реальный кейс: неполные данные (get() возвращает default)
        data = {'email': 'ok@example.ru'} # Нет age
        errors = self.validator.validate_user(data)
        self.assertIn('age', errors) # age=0 < 18

    def test_non_int_age(self):
        # Edge-кейс: неверный тип
        data = {'email': 'ok@example.com', 'age': 'twenty'}
        errors = self.validator.validate_user(data)
        self.assertIn('age', errors) # Не int

if __name__ == '__main__':
    unittest.main(verbosity=2)