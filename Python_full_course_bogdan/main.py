import copy
lst1 = [1, 2, 3, 4]  # Создаётся mutable объект list
lst2 = copy.copy(lst1)  # Поверхностная копия
lst1.append(5)

print(lst1, lst2)  # [1, 2, 3, 4, 5] [1, 2, 3, 4]
print(id(lst1), id(lst2))  # id(lst1) != id(lst2)