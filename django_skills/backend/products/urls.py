from django.urls import path
from products import views

urlpatterns = [
    path('search/', views.product_search, name='product_search'),
]