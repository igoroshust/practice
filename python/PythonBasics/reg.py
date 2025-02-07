"""Опишите, как будет работать приложение, в котором надо реализовать:

Регистрация пользователей
Зарегистрированные пользователи могут создавать посты
Незарегистрированные пользователи могут читать посты """


Создание приложения на Django с функциональностью регистрации пользователей, создания постов зарегистрированными пользователями и чтения постов незарегистрированными пользователями — это классическая задача, которая хорошо иллюстрирует основные возможности Django. Давайте рассмотрим, как будет работать такое приложение, шаг за шагом.

1. Структура приложения
Приложение будет состоять из следующих основных компонентов:

Модели: Определяют структуру данных (например, пользователей и посты).
Представления (Views): Обрабатывают запросы и возвращают ответы.
Шаблоны (Templates): Отображают данные пользователю.
URL-адреса (URLs): Определяют маршруты для доступа к различным частям приложения.

2. Модели
Вам понадобятся две основные модели: User  (пользователь) и Post (пост). Django предоставляет встроенную модель пользователя, поэтому мы можем использовать её.

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
3. Регистрация пользователей
Для регистрации пользователей можно создать форму и представление. Используем встроенные механизмы Django для работы с пользователями.

Форма регистрации

from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

Представление для регистрации

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Автоматически авторизуем пользователя
            return redirect('post_list')  # Перенаправление на список постов
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

4. Создание постов
Зарегистрированные пользователи смогут создавать посты. Для этого создадим форму и представление.

Форма создания поста

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


Представление для создания поста

from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')  # Перенаправление на список постов
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
5. Чтение постов
Незарегистрированные пользователи смогут читать посты. Создадим представление для отображения списка постов.

Представление для списка постов

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

6. URL-адреса
Теперь нужно настроить маршруты для доступа к различным частям приложения.

from django.urls import path
from .views import register, create_post, post_list

urlpatterns = [
    path('register/', register, name='register'),
    path('create_post/', create_post, name='create_post'),
    path('', post_list, name='post_list'),  # Главная страница со списком постов
]


7. Шаблоны (продолжение)
Пример шаблона для регистрации (registration/register.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Регистрация</title>
</head>
<body>
    <h1>Регистрация</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Зарегистрироваться</button>
    </form>
    <p>Уже есть аккаунт? <a href="{% url 'login' %}">Войти</a></p>
</body>
</html>

Пример шаблона для создания поста (posts/create_post.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Создать пост</title>
</head>
<body>
    <h1>Создать пост</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Создать</button>
    </form>
    <p><a href="{% url 'post_list' %}">Назад к списку постов</a></p>
</body>
</html>

Пример шаблона для списка постов (posts/post_list.html)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список постов</title>
</head>
<body>
    <h1>Список постов</h1>
    <ul>
        {% for post in posts %}
            <li>
                <h2>{{ post.title }}</h2>
                <p>{{ post.content }}</p>
                <p><em>Автор: {{ post.author.username }} | Дата: {{ post.created_at }}</em></p>
            </li>
        {% empty %}
            <li>Нет постов для отображения.</li>
        {% endfor %}
    </ul>
    <p><a href="{% url 'create_post' %}">Создать новый пост</a></p>
    <p><a href="{% url 'register' %}">Зарегистрироваться</a></p>
</body>
</html>

8. Настройка аутентификации
Чтобы пользователи могли входить в систему, вам нужно настроить аутентификацию. Django предоставляет встроенные представления для входа и выхода.

URL-адреса для аутентификации
Добавьте следующие URL-адреса в ваш файл urls.py:

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('create_post/', create_post, name='create_post'),
    path('', post_list, name='post_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

Шаблон для входа (registration/login.html)
Создайте шаблон для входа, если вы хотите настроить его:


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Вход</title>
</head>
<body>
    <h1>Вход</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Войти</button>
    </form>
    <p>Нет аккаунта? <a href="{% url 'register' %}">Зарегистрироваться</a></p>
</body>
</html>

9. Защита представлений
Чтобы защитить представление для создания постов, вы уже использовали декоратор @login_required. Это гарантирует, что только авторизованные пользователи могут получить доступ к этому представлению.

10. Запуск приложения
Теперь, когда все компоненты настроены, вы можете запустить сервер разработки Django и протестировать приложение:

python manage.py runserver
Перейдите по адресу `http://127.0.0.1:800
