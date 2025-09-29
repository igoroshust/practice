import re
from typing import Dict, Any

class UserValidator:
    """Тестируемая функция"""
    def __init__(self):
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    def validate_user(self, user_data: Dict[str, Any]) -> Dict[str, str]:
        errors = {}
        email = user_data.get('email', '')
        age = user_data.get('age', 0)

        if not self.email_pattern.match(email):
            errors['email'] = 'Invalid email format'
        if not isinstance(age, int) or age < 18 or age > 100:
            errors['age'] = 'Age must be between 18 and 100'

        return errors # Пустой dict - OK