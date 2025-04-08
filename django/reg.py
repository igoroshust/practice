"""Реализация регистрации"""
# 1. python manage.py startapp accounts

# 2. accounts/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
#
#
# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label="Email")
#     first_name = forms.CharField(label="Имя")
#     last_name = forms.CharField(label="Фамилия")
#
#     class Meta:
#         model = User
#         fields = (
#             "username",
#             "first_name",
#             "last_name",
#             "email",
#             "password1",
#             "password2",
#         )

# 3. accounts/views.py
# from django.contrib.auth.models import User
# from django.views.generic.edit import CreateView
# from .forms import SignUpForm
#
#
# class SignUp(CreateView):
#     model = User
#     form_class = SignUpForm
#     success_url = '/accounts/login'
#     template_name = 'registration/signup.html'


# 4. templates/registration/signup.html
# {% extends "flatpages/default.html" %}
#
# {% block content %}
#
# <form method="post">
# {% csrf_token %}
#     {{ form.as_p }}
#     <input type="submit" value="Sing up">
# </form>
#
# {% endblock %}


# 5. accounts/urls.py
# from django.urls import path
# from .views import SignUp
#
# urlpatterns = [
#     path('signup/', SignUp.as_view(), name='signup'),
# ]

# 6. project/urls.py
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("accounts/", include("django.contrib.auth.urls")),
#     path("accounts/", include("accounts.urls")),  # Добавили эту строчку
#     path("products/", include("simpleapp.urls")),
# ]