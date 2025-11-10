from django.shortcuts import render
from django.db.models import Q  # Для сложных запросов
from django.db.models.functions import Lower  # Преобразование строкового поля в нижний регистр в SQL-запросе.
from products.models import Product
import re

def product_search(request):
    """Поиск с icontains и Lower для регистронезависимости"""

    # TODO: как обойти поиск по `е` и `ё` и другие схожие кейсы
    # TODO: Прочитать стандартные кейсы для работы поиска

    query = request.GET.get('q', '').strip()  # Убираем лишние пробелы
    products = Product.objects.all() 

    if query:
        # Преобразуем запрос к нижнему регистру
        query_lower = query.lower()
        
        # Аннотируем поля нижним регистром и фильтруем
        products = products.annotate(
            name_lower=Lower('name'),  # Преобразуем поля и запрос к нижнему регистру перед сравнением
            description_lower=Lower('description')
        ).filter(
            Q(name_lower__icontains=query_lower) |
            Q(description_lower__icontains=query_lower)
        )

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'products/search.html', context=context)

    #  Комментарии:
    #  + нужно добавть db_index=True для полей name и description


# def product_search(request):
#     """Поиск с регулярными выражениями"""
#     query = request.GET.get('q', '')
#     products = Product.objects.all()

#     if query:
#         # Экранируем специальные символы regex
#         safe_query = re.escape(query)  # Добавляет обратные слэши перед спец.символами, чтобы они не экранировались, как операторы.
#         regex_pattern = f'(?i){safe_query}'  # Паттерн регистронезависимого поиска

#         products = products.filter(
#             Q(name__iregex=regex_pattern) |  # iregex - lookup в Django ORM для поиска по регулярному выражению
#             Q(description__iregex=regex_pattern)
#         )

#     context = {
#         'products': products,
#         'query': query,
#     }

#     return render(request, 'products/search.html', context=context)



"""Документация к файлу views.py
from django.db.models.functions - применение функций (Lower, Upper, Concat) к полям в запросах без сырого SQL.

Lower - функция для преобразования строкового поля в нижний регистр в SQL-запросе. `Lower('name')` генерирует `LOWER(name)`в SQL. 
Используется для регистронезависимых операций.

annotate - метод QuerySet для добавления вычисляемых полей к объектам. `queryset.annotate(name_lower=Lower('name'))` добавляет поле `name_lower` с нижним регистром.
Не изменяет БД, только результат запроса.

Группировка данных (annotate + values). `annotate` добавляет агрегированные поля (н-р, Count, Sum). Для группировки используется `values()` + annotate.
Пример: Product.objects.values('category').annotate(count=Count('id')) группирует по категории и считает товары. filter применяется после группировки для фильтрации групп.

Q - класс для сложных условий в фильтрах. Позволяет комбинировать запросы с `&` (AND), `|` (OR), `~` (NOT).
Q(name__icontains='test') | Q(description__icontains='test')

db_index - атрибут поля модели (`db_index=True`) для создания индекса в БД. Ускоряет поиск, но замедляет вставку/обновление. После добавления нужны миграции.

Проверить в консоле, что поле проиндексировано
python manage.py shell
>>> from products.models import Product 
>>> print(Product._meta.get_field('name').db_index)

_meta - защищённый атрибут каждого класса модели Django, предоставляющий программный доступ к метаданным модели: информации о её структуре, полях, настройках, связях.
fields = Product._meta.get_fields()
fields1 = Product._meta.get_field('name').db_index
Пример:
class Meta:
        db_table = 'my_products'
        ordering = ['-price']
# Получение информации через _meta
print(Product._meta.db_table)  # 'my_products'
print(Product._meta.ordering)  # ['-price']

Просмотр проиндексированных полей в SQLite
PRAGMA index_list('products_product');
PRAGMA index_info('products_product_name_fa23bcd2'); (значение вставлено из index_list)
"""


"""Пример работы annotate
`annotate` добавляет вычисляемые поля к объектам QuerySet без изменения БД. Используется для агрегации, вычислений или группировки.

Пример-1 (добавление вычисляемого поля - длина имени)
from django.db.models.functions import Length
from products.models import Product

# Добавляем поле 'name_length' с длиной имени
products = Product.objects.annotate(name_length=Length('name'))

for product in products:
    print(f"{product.name}: {product.name_length}")  # Вывод: "Кот: 3"


Пример-2 (агрегация - количество товаров в категории)
from django.db.models import Count
from products.models import Product

# Группируем по категории и считаем товары
categories = Product.objects.values('category').annotate(product_count=Count('id'))  # values группирует, annotate добавляет счётчик product_count
for cat in categories:
    print(f"{cat['category']}: {cat['product_count']} товаров")  # Вывод: "Электроника: 5"


Пример-3 (Фильтрация + регистронезависимый поиск)
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product

query = 'кот'
products = Product.objects.annotate(
    name_lower=Lower('name'),
    description_lower=Lower('description'),
).filter(
    Q(name_lower__icontains=query.lower()) | 
    Q(description_lower__icontains=query.lower())
)

for product in products:
    print(product.name)
"""