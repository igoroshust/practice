from django.db import models

### Ограничение должностей
director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик'),
]

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)

class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    labor_contract = models.IntegerField()

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True) - значение автоматически устанавливалось на текущую дату и время при поступлении заказа в БД
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) - один ко многим.
    products = models.ManyToManyField(Product, through='ProductOrder')

class ProductOrder(models.Model):
    amount = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)