my_dict = {
    'brand': 'Ducati',
    'price': 390_000_00,
    'vol': 1.2,
}

print(
    my_dict.setdefault('test', 'asd'),  # asd
    my_dict,  # {'brand': 'Ducati', 'price': 39000000, 'vol': 1.2, 'test': 'asd'} (добавляет 'test': 'asd')
    sep='\n'
)
