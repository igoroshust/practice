from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")  # Цена с 2 знаками после запятой
    #  DecimalField для чисел с плавающей точкой (цена), max_digits - общее количество цифр (включая цифры до и после точки), decimal_places - количество цифр после точки
    #  DecimalField рекомендуется для денежных значений, где важна точность (FloatField - где погрешность допустима)
    #  (max_digits=5, decimal_places=2) может хранить значения от -999.99 до 999.99
    category = models.CharField(max_length=100, verbose_name="Категория")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"