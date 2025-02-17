def is_leap_year(param):
    """Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным. Год будет високосным, если он делится без остатка на 400, или он одновременно делится без остатка на 4 и не делится на 100:"""
    return (param % 400 == 0) or (param % 4 == 0 and param % 100 > 0)
print(is_leap_year(2003))
