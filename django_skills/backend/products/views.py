from django.shortcuts import render
from django.db.models import Q  # Для сложных запросов
from products.models import Product

def product_search(request):
    query = request.GET.get('q', '')  # Получаем поисковый запрос из GET-параметра 'q'
    products = Product.objects.all()  # Начинаем со всех товаров

    if query:
        products = products.filter(
            Q(name__icontains=query) |  # Ищем в названии (регистронезависимо)
            Q(description__icontains=query)  # Ищем в описании
        )

    #  Словарь данных для шаблона
    context = {
        'products': products,  # Передаём отфильтрованные товары
        'query': query,  # Передаём запрос для отображения в шаблоне
    }

    return render(request, 'products/search.html', context=context)