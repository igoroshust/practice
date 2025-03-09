from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, mail_managers, EmailMultiAlternatives
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

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            subject = 'Добро пожаловать...'
            text = 'Вы успешно зарегистрировались!'
            html = (
                f'<b>{user.username}</b>, Вы успешно зарегистрировались на '
                f'<a href="http://127.0.0.1:8000/main">сайте</a>'
            )

            msg = EmailMultiAlternatives(
                subject=subject, body=text, from_email='igoroshust@yandex.ru', to=[user.email]
            )

            msg.attach_alternative(html, "text/html")
            msg.send()

            # mail_managers(
            #     subject='Новый пользователь!',
            #     message=f'Пользователь {user.username} зарегистрировался на сайте',
            #     fail_silently=False,
            # )

        return user

    # def save(self, commit=True): # если commit=True, мы отправляем письмо на адрес ЭП пользователя с помощью функции send_mail
    #     user = super().save(commit=commit) # commit позволяет контролировать, сохраняется ли пользователь в БД сразу или мы можем сделать это позже.
    #     if commit:
    #         # Отправка письма о регистрации
    #         send_mail(
    #             subject='Добро пожаловать',
    #             message='Вы успешно зарегистрировались',
    #             from_email='igoroshust@yandex.ru',
    #             recipient_list=[user.email],
    #         )
    #     return user

    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     if commit:
    #
    #         subject = 'Добро пожаловать на наш сайт!'
    #         text = f'{user.username}, вы успешно зарегистрировались на сайте!'
    #         html = (
    #             f'<b>{user.username}</b>, вы успешно зарегистрировались на сайте '
    #             f'<a href="http://127.0.0.1:8000/main">сайте</a>!'
    #         )
    #         msg = EmailMultiAlternatives(
    #             subject=subject, body=text, from_email='igoroshust@yandex.ru', to=[user.email]
    #         )
    #         # метод для добавления альтернативного формата содержимого к письму
    #         # attach_alternative(html-код, "text/html")
    #         msg.attach_alternative(html, "text/html")
    #         msg.send()
    #
    #     return user


























