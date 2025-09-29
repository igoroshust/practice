list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = dict(zip(list1, list2))
print(zipped)

it = iter(list1)
print(next(it))
print(next(it))