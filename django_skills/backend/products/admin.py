from django.contrib import admin
from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')  # Какие поля показывать в списке
    search_fields = ('name', 'description', 'category')  # По каким полям можно искать в админке
