# Протокол SMTP
# POP3

"""Реализация отправки сообщений"""
# Шаг 1. Настроить отправителя сообщений и указать данные почты, с которой будут отправляться письма.
# Отправителем в Django выступает один из специальных Python-классов.
# По аналогии с обычным использованием почты можно считать, что данный класс играет роль почтовой программы.
# Подобно mail.yandex.ru, mail.google.com, mozilla thunderbird, он умеет отправять сообщения на другие почтовые ящики, но получать входящие нельзя (только отправка).
# Для настройки класса используется переменная EMAIL_BACKEND в settings.py, по умолчанию 'django.core.mail.backends.smtp.EmailBackend'.
# Это класс, который использует стандартную библиотеку Python для работы с SMTP - протоколом отправки сообщений.


# Параметры для работы с почтовыми сервисами
# Yandex: https://yandex.ru/support/yandex-360/customers/mail/ru/mail-clients/others.html#smtpsetting
# + Yandex разрашение работы с помощью пароля приложений: https://mail.yandex.ru/?uid=1567990805#setup/client
# GMAIL: https://support.google.com/mail/answer/7126229?hl=ru#zippy=%2C%D1%88%D0%B0%D0%B3-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D0%B5-smtp-%D0%B8-%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B2-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D0%B5


# Шаг 2. Настраиваем в проекте доступ к нашей почте, от чьего имени будут отправляться письма.
# Настраиваем логин, пароль и параметры для работы для работы с почтовым сервисом по протоколу SMTP (адрес почтового сервера, порт, необходимость использования SSL)

# Шаг 3. Настраиваем в проекте данные по работе с почтовым сервером:
# EMAIL_BACKEND - класс отправителя сообщений | django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST - хост почтового сервера | smtp.yandex.ru
# EMAIL_PORT - порт, на который почтовый сервер принимает письма | 465
# EMAIL_HOST_USER - логин пользователя почтового сервера | example@xx.xx
# EMAIL_HOST_PASSWORD - пароль пользователя почтового сервера; | xxxxxx
# EMAIL_USE_TLS - необходимость использования TLS (в зависимости от почтового сервера) | False
# EMAIL_USE_SSL - необходимость использования SSL (зависит от почтового сервера) | True
# DEFAULT_FROM_EMAIL - почтовый адрес отправителя по умолчанию | example@xx.xx

# Шаг 4. Отпределиться, где и какой код написать для отправки письма новому пользователю.
# Переходим в приложение (accounts), создаём файл forms.py

from allauth.account.forms import SignupForm
from django.core.mail import send_mail

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        # send_mail - отправка письма указанному получателю в recipient_list
        send_mail(
            subject='Добро пожаловать на сайт!', # тема письма
            message=f'{user.username}, вы успешно зарегистрировались!', # текстовое сообщение
            from_email = None, # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email] # список получателей.
        )
        return user

