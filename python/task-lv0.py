# """Поиск факториала (декларативный способ)"""
# f = int(input(': '))
# p = 1
#
# if 1 > f > 100:
#     print('Ввели неверное число')
# else:
#     for i in range(1, f+1):
#         p *= i
#
# print(f'Факториал числа {f}! = {p}')

"""Есть два списка разной длины. В первом содержатся ключи, а во втором — значения.
Напишите функцию make_dict, которая создаёт из этих ключей и значений словарь."""
# def make_dict(keys, values):
#     result = {}
#
#     for i in range(len(keys)):
#         if i < len(values):
#             result[keys[i]] = values[i]
#         else:
#             result[keys[i]] = None
#
#     return result
#
# keys = [1, 2, 3]
# values = ['a', 'b']
# result = make_dict(keys, values)
#
# print(result)

"""Напишите простой калькулятор. У вас должна быть функция calculate, которая принимает три аргумента: 
первые два — числа, третий — операция, которая должна быть произведена над ними"""
def calculate(num1, num2, operation):
    if operation == 'сложение':
        return num1 + num2
    elif operation == 'вычитание':
        return num1 - num2
    elif operation == 'умножение':
        return num1 * num2
    elif operation == 'деление':
        if num2 != 0:  # Проверка на деление на ноль
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"

# Примеры использования
print(calculate(10, 5, 'сложение'))
print(calculate(10, 5, 'вычитание'))
print(calculate(10, 5, 'умножение'))
print(calculate(10, 5, 'деление'))
print(calculate(10, 0, 'деление'))        # Вывод: Ошибка: деление на ноль
print(calculate(10, 5, 'возведение'))     # Вывод: Неизвестная операция