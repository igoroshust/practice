import time
class HeavyResource:
    def __init__(self):
        print('Загружаем данные тяжёлого ресурса...')
        time.sleep(2)
        self.data = 'Данные большого ресурса'

    def get_data(self):
        return self.data


class LazyLoader:
    def __init__(self):
        self._heavy_recource = None

    @property
    def heavy_resource(self):
        if self._heavy_recource is None:
            print('Поступил запрос на создание ресурса')
            time.sleep(2)
            print('Создаём тяжёлый ресурс...')
            time.sleep(2)
            self._heavy_recource = HeavyResource()
        return self._heavy_recource

if __name__ == "__main__":
    loader = LazyLoader()

    print('Ресурс ещё не создан...')
    time.sleep(2)
    resource = loader.heavy_resource
    print(resource.get_data())



"""Вывести сумму чисел введённого числа"""
# # Решение ИИ
# def print_digit_sum(num: int) -> None: # None указывает, что функция ничего не возвращает.
#     # Вычисляем сумму цифр с помощью генератора
#     digit_sum = sum(int(i) for i in str(num))
#     print(digit_sum)
#
# # Запрос ввода от пользователя
# num = int(input('Введите число: '))
# print_digit_sum(num)


# # Моё решение
# def print_digit_sum(num):
#     lst = []
#     for i in str(num):
#         lst.append(int(i))
#     print(sum(lst))
#
# print_digit_sum(7)


"""Вывести ФИО"""
# def print_fio(name: str, surname: str, patronymic: str) -> str:
#     print(
#         surname[0].upper(), name[0].upper(), patronymic[0].upper(),
#         sep=''
#     )
#
# print_fio('игорь', 'ошуст', 'неизвестно')



"""Реализуйте звёздный треугольник"""
# def draw_triangle(fill, base):
#     # Вывод верхней части треугольника
#     for i in range(1, base // 2 + 2): # (base // 2) - целочисленное деление основания на 2. Получаем целое число, равное половине основания.
#         # Добавляем 2, чтобы включить в диапазон не только половину, но и самую верхнюю строку, содержащую `5` символов (в случае с 9)
#         # Получается диапазон от 1 до 5 (включительно).
#         print(fill * i)
#
#     # Вывод нижней части треугольника
#     for i in range(base // 2, 0, -1): # (base // 2) - начинаем с половины основания, что соотстветвует количеству символовв первый строке нижней части треугольника.
#         # 0 - продолжаем цикл до 1 включительно, поэтому указываем 0, которое не включается в диапазон.
#         # -1 - уменьшаем i на 1 при каждой итерации
#         print(fill * i)
#
# # Пример вызова функции
# draw_triangle('*', 9)


"""Вывести лесенку звёздочек от 1 до 10"""
# # Моё решение
# def draw_triangle(ast, count):
#     while count <= 10:
#         print(ast * count)
#         count += 1
#
# draw_triangle('*', 1)

# # Решение ИИ
# def draw_triangle(symbol, height):
#     """Рисуем треугольник"""
#     for count in range(1, height + 1):
#         print(symbol * count)
#
# # Вызов функции с высотой 10
# draw_triangle('*', 10)


"""Сделать прямоугольник с вырезом"""
# def draw_box(width, height):
#     # Печатаем верхнюю границу
#     print('*' * width)
#
#     # Печатаем боковые границы
#     for _ in range(height - 2):
#         print(f'*{(width - 2) * ' '}*')
#         # print('*' + ' ' * (width - 2) + '*')
#
#     # Печатаем нижнюю границу
#     print('*' * width)
#
# # Вызов функции
# draw_box(10, 14)



"""Поисковый запрос"""
# n = int(input())
# lines = []
#
# # Считываем строки
# for _ in range(n):
#     line = input()
#     lines.append(line)
#
# # Считываем поисковый запрос
# query = input().lower()
#
# # Ищем строки запроса
# results = []
# for line in lines:
#     if query in line.lower():
#         results.append(line)
#
# print('\n'.join(results))



"""Вывести только уникальные числа из списка"""
# n = int(input())
# numbers = []
#
# for i in range(n):
#     x = input()
#     if x not in numbers:
#         numbers.append(x)
#
# print('\n'.join(numbers))



"""Вывести числа по формуле"""
# n = int(input("Введите количество чисел: "))
# results = []
# xs = []
#
# for _ in range(n):
#     x = int(input("Введите число: "))
#     f = x**2 + 2 * x + 1
#     xs.append(x)
#     results.append(f)
#
# print("Введенные числа:")
# print('\n'.join(map(str, xs)))
# print("\nРезультаты:")
# print('\n'.join(map(str, results)))