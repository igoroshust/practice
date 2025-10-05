class Person:
    def __init__(self, age):
        self.age = age  # Публичная
        self._age = age  # Защищённая
        self.__age = age  # Приватная

# Доступ к переменным
person = Person(25)
print(
    person.age,  # 25
    person._age,  # 25
    # person.__age,  # AttributeError
    person._Person__age,  # 25
    sep='\n'
)