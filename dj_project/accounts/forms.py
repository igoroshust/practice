from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True): # если commit=True, мы отправляем письмо на адрес ЭП пользователя с помощью функции send_mail
        user = super().save(commit=commit) # commit позволяет контролировать, сохраняется ли пользователь в БД сразу или мы можем сделать это позже.
        if commit:
            # Отправка письма о регистрации
            send_mail(
                subject='Добро пожаловать',
                message='Вы успешно зарегистрировались',
                from_email='igoroshust@yandex.ru',
                recipient_list=[user.email],
            )
        return user
