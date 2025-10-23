# Задача-2 (альтернативный вариант)
seq = [1, 2, 3, True, 'string']
def filter_list(sequence, type_of_sequence):
    return list(filter(lambda elem: type(elem) == type_of_sequence, sequence))
print(filter_list(seq, int))
