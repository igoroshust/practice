def largest_power_of_two(n):
    """Наибольшее число со степенью 2 меньше n"""
    if n < 1:
        return 0
    power = 1  # Начинаем с 2^0 = 1
    while power * 2 <= n:  # Пока удвоение не превысит n
        power *= 2  # Удваиваем (делим пространство поиска пополам)
    return power


# Тестирование
print(
    largest_power_of_two(10),  # Вывод: 8 (2^3 = 8 <= 10)
    largest_power_of_two(1),  # Вывод: 1 (2^0 = 1)
    largest_power_of_two(100),  # Вывод: 64 (2^6 = 64 <= 100)
)

# Для большого n (n=1_000_000)
large_n = 1_000_000
result = largest_power_of_two(large_n)
print(f'Для n = {large_n}: {result}')  # Вывод: 524288 (2^19)
