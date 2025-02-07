# # Методы создания объектов
create(**kwargs) # Создание объекта
Book.objects.create(title='New Book', author='Author Name', published_date='2023-01-01')

bulk_create(objs, batch_size=None) # Создание множества объектов в БД за один SQL-запрос
Book.objects.bulk_create([Book(title='Book 1'), Book(title='Book 2')])

get_or_create(defaults=None, **kwargs) # Получает объект, если он существует, или создаёт его, если нет
book, created = Book.objects.get_or_create(title='New Book', defaults={'author': 'Author Name'})

update_or_create(defaults=None, **kwargs) # Обновляет объект, если он существует, или добавляет его в случае отсутствия
book, created = Book.objects.update_or_create(title='New Book', defaults={'author': 'Author Name'})

# # Методы чтения объектов
all() # Возвращает все объекты модели
book = Book.objects.all()

filter(**kwargs) # Возвращает объекты, соответствующие заданным условиям
book = Book.objects.filter(author='Author Name')

exclude(**kwargs) # Возвращает объекты, не соответствующие заданным условиям
book = Book.objects.exclude(author='Author Name')

get(**kwargs) # Возвращает единственный объект, соответствующий заданным условиям (вызывает искл. DoesNotExist и MultipleObjectsReturned)
book = Book.objects.get(author='Author Name')

first() # Возвращает первый объект из QuerySet или None, если QuerySet пуст
book = Book.objects.filter(author='Author Name').first()

last() # Возвращает последний элемент из QuerySet или None, если QuerySet пуст
book = Book.objects.filter(author='Author Name').last()

count() # Возвращает количество объектов в QuerySet
book = Book.objects.filter(author='Author Name').count()

exists() # Проверяет, существуют ли объекты QuerySet
book = Book.objects.filter(author='Author Name').exists()

# # Методы CRUD
update(**kwargs) # Обновляет поля объектов в QuerySet
book = Book.objects.filter(author='Old Author').update(author='New Author')

delete() # Удаляет объекты в QS
book = Book.objects.filter(author='Old Author').delete()

# # Методы для работы с QS
order_by() # Упорядочивает объекты по указанным полям
books = Book.objects.all().order_by('published_date')

distinct() # Возвращает уникальные объекты
book = Book.objects.values('author').distinct()

values(*fields) # Возвращает QS, содержащий словари с указанными полями
books = Book.objects.values('title', 'author')

values_list(*fields, flat=False) # Возвращает QS, содержащий кортежи с указанными полями. flat=True вернёт плоский список
books = Book.objects.values_list('title', flat=True)

annotate(*args, **kwargs) # Добавляет аннотации к объектам в QuerySet
from django.db.models import Count
authors_with_book_count = Author.objects.annotate(book_count=Count('book'))

aggregate(*args, **kwargs) # Выполняет агрегацию на уровне QS и возвращает словарь с результатами
from django.db.models import Count, Avg
stats = Book.objects.aggregate(total_books=Count('id'), average_price=Avg('price'))

prefetch_related(*lookups) # Оптимизирует запросы, загружая связанные объекты в одном запросе для избежания проблемы "N+1 запросов"
books = Book.objects.prefetch_related('authors').all()

select_related(*fields) # Используется для оптимизации запросов, загружая связанные объекты с помощью SQL JOIN (полезно с ForeignKey и OneToOne полями)
books = Book.objects.select_related('author').all()

iterator(chunk_size=None) # Позволяет итерироваться по QS, загружая данные порционно (полезно для работы с большими наборами данных)
for book in Book.objects.all().iterator(chunk_size=100):
    print(book.title)

# # Метод для работы с транзакциями
transaction.atomic() # Контекстный менеджер, позволяющий выполнять операции в рамках одной транзакции (если что-то не так, все изменения отменятся)

from django.db import transaction
with transaction.atomic():
    # Ваши операции с БД
    Book.objects.create(title='New Book', author='Author Name')