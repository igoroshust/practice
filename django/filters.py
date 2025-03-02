"""Использование django-filter"""
# django-filter - сторонняя библиотека, упрощающая процесс фильтрации данных в Django.
# Она позволяет создавать фильтра для ваших моделей и использовать их в представлениях.

# 1. pip install django-filter

# # 2. Создаём фильтр (app/filters.py)
# from django_filters import rest_framework as filters
# from myapp.models import Product
#
# class ProductFilter(filters.FilterSet):
#     class Meta:
#         model = Product
#         fields = {
#             'category': ['exact', 'icontains'],
#             'price': ['lt', 'gt'],
#         }

# # 3. Используем фильтр в представлении
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = (DjangoFilterBackend)
#     filterset_class = ProductFilter


# # 3. Можно использовать фильтр в представлении через Views
# class ProductsList(ListView):
#    model = Product
#    ordering = 'name'
#    template_name = 'products.html'
#    context_object_name = 'products'
#    paginate_by = 2
#
#    def get_queryset(self):
#        # Получаем обычный запрос
#     queryset = super().get_queryset()
#        # self.request.GET содержит QueryDict
#     self.filterset = ProductFilter(self.request.GET, queryset)
#        # Возвращаем из функции отфильтрованный список товаров
#     return self.filterset.qs
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        # Добавляем в контекст объект фильтрации
#        context['filterset'] = self.filterset
#        return context


# # Фильтрация и сортировка в представлении
# def product_list(request):
#     products = Product.objects.all()
#
#     # Фильтрация по категориям
#     category = request.GET.get('category')
#     if category:
#         products = products.filter(category=category)
#
#     # Сортировка по цене
#     sort = request.GET.get('sort')
#     if sort == 'price':
#         products = products.order_by('price')
#     elif sort == '-price':
#         products = products.order_by('-price')
#
#     return render(request, 'product_list.html', {'products': products})

# # Использование Django Admin
# Django admin автоматически предоставляет интерфейс для фильтрации и сортировки данных. Можно настроить фильтры и сортировку
# в админке, добавляя соответствующие параметры в класс админки.
# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ('category', 'price')
#     ordering = ('price',)
#
# admin.site.register(Product, ProductAdmin)


"""Создание формы"""
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'

"""CreateView"""
# class ProductCreate(CreateView):
#     form_class = ProductForm
#     model = Product
#     template_name = 'product_edit.html'

