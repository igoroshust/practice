"""Пример бинарного поиска через рекурсию"""
# def binary_search_recursive(array: list, element: int, start: int, end: int) -> int:
#     mid: int = (start + end) // 2 # делим список пополам (длину списка делим пополам, получаем 3)
#     if element == array[mid]: # являелся ли элемент id 3 (равен ли шестёрке)
#         return mid # возвращаем значение
#     elif element < array[mid]: # если не равняется, то проверяем, меньше ли он 6
#         return binary_search_recursive(array, element, start, mid-1) # возвр. с концом end-1 (2), рекурся на строку mid: (start + end) // 2 и новая итерация
#     else:
#         return binary_search_recursive(array, element, mid+1, end) # прибавляем к старту
#
# print(binary_search_recursive([1, 2, 4, 6, 7, 8], 4, 0, 5))

"""Пример бинарного поиска"""
# def bi_search(a: int, array: list) -> int: # а - искомое число, array - список, в котором проводится поиск числа. Возвращается индекс числа (тип int).
#     left, right = 0, len(array) # left - левый край списка, right - правый край списка
#     while left < right: # пока левый край меньше правого, мы ищем нужное число
#         middle = (left + right) // 2 # находим середину данного списка
#         if array[middle] < a: # если искомое число меньше
#             left = middle + 1 # в качестве левой границы берём центр + 1
#         else:
#             right = middle # в другом случае, правая граница равна middle
#     return left
#
# print(bi_search(6, [1,3,5,6,8,12,15]))

"""Пример Евклидового алгоритма"""
# def e_alg(a: int, b: int) -> int:
#     while a != 0 and b != 0:
#         if a < b:
#             b %= a
#         else:
#             a %= b
#     return a + b
# print(e_alg(30, 45))


"""Задача. В классе N учеников. Учитель опрашивает сначала всех учащихся с несётными номерами (1,3...),
затем - всех с чётными номерами (2,4...). Вася, имеющий номер К по журналу, хочет узнать, какой по порядку
вопрос достанется ему. Напишите программу, вычисляющую номер вопроса по введённым N и K."""
# N = int(input("Введите количество учеников в классе: "))
# K = int(input("Введите позицию Васи: "))
#
# if K % 2 == 1:
#     print(int(K/2+1))
# else:
#     print(int(N/2 + N%2 + K/2))


"""Пример наивной сортировки (не рекомендуется)"""
# import random  # модуль, с помощью которого перемешиваем массив
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счетчику
#     random.shuffle(array)  # перемешиваем массив
#     # проверяем отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698

"""Сортировка выбором по неубыванию (поиск минимального элемента и его добавление в начало)"""
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(len(array)): # проходим по всему массиву
#
#         idx_min = i # сохраняем индекс предположительно минимального элемента
#         for j in range(i+1, len(array)):
#                 if array[j] < array[idx_min]:
#                         idx_min = j
#         if i != idx_min: # если индекс не совпадает с минимальным, меняем
#                 array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)

"""Сортировка выбором по убыва (поиск минимального элемента и его добавление в начало)"""
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(len(array)): # проходим по всему массиву
#
#         idx_max = i # сохраняем индекс предположительно минимального элемента
#         for j in range(i, len(array)):
#                 if array[j] > array[idx_max]:
#                         idx_max = j
#         if i != idx_max: # если индекс не совпадает с минимальным, меняем
#                 array[i], array[idx_max] = array[idx_max], array[i]
#
# print(array)

"""Сортировка пузырьком"""
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)

"""Сортировка вставками"""
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# print(array)

"""Алгоритм сортировки слиянием"""
# def merge_sort(L):  # «разделяй»
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
# def merge(left, right):  # «властвуй»
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result

"""Быстрая сортировка"""
# import random
#
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#             random.choice(array[idx_left: idx_right])
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)


"""Реализация бинарного дерева"""
# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#         print(self.value)  # процедура обработки
#
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.pre_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.pre_order()  # рекурсивно вызываем функцию
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
# a_node = BinaryTree('A').insert_left('B').insert_right('C')
# # print(a_node)
#
# # Реализация дерева(бинарного)
# # создаем корень и его потомки /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
#
# # node_root.post_order()
# # node_root.pre_order()

"""Алгоритм Дейкстры (поиск кротчайшего пути между вершинами)"""
# G = {
#     "Адмиралтейская": {
#         "Садовая": 4},
#     "Садовая": {
#         "Сенная площадь": 4,
#         "Спасская": 3,
#         "Адмиралтейская": 4,
#         "Звенигородская": 5},
#     "Сенная площадь": {
#         "Садовая": 4,
#         "Спасская": 4},
#     "Спасская": {
#         "Садовая": 3,
#         "Сенная площадь": 4,
#         "Достоевская": 6},
#     "Звенигородская": {
#         "Пушкинская": 3,
#         "Садовая": 5},
#     "Пушкинская": {
#         "Звенигородская": 3,
#         "Владимирская": 4},
#     "Владимирская": {
#         "Достоевская": 3,
#         "Пушкинская": 4},
#     "Достоевская": {
#         "Владимирская": 3,
#         "Спасская": 6}
# }
#
# D = {k : 100 for k in G.keys()}  # расстояния
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()}  # флаги просмотра вершин
# P = {k : None for k in G.keys()}  # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]:  # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v]  # то фиксируем его
#             P[v] = min_k  # и записываем как предок
#     U[min_k] = True  # просмотренную вершину помечаемp
#
# pointer = "Владимирская" # куда должны прийти
# path = [] # список с вершинами пути
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#    path.append(pointer)
#    pointer = P[pointer]
#
# path.reverse() # разворачиваем путь
# for v in path:
#     print(v)
