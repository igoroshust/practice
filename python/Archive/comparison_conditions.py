def is_good_apartment(area, street):
    """Теперь представим, что мы хотим купить квартиру, которая удовлетворяет таким условиям: площадь от 100 квадратных метров и больше на любой улице ИЛИ площадь от 80 квадратных метров и больше, но на центральной улице Main Street."""
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartment(90, 'Main Street'))