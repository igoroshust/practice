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

# from allauth.account.forms import SignupForm
# from django.core.mail import send_mail
#
# class CustomSignupForm(SignupForm):
#     def save(self, request):
#         user = super().save(request)
#
#         # send_mail - отправка письма указанному получателю в recipient_list
#         send_mail(
#             subject='Добро пожаловать на сайт!', # тема письма
#             message=f'{user.username}, вы успешно зарегистрировались!', # текстовое сообщение
#             from_email = None, # будет использовано значение DEFAULT_FROM_EMAIL
#             recipient_list=[user.email] # список получателей.
#         )
#         return user


"""HTML-письма"""
# Чтобы отправить HTML по почте, нужно воспользоваться EmailMultiAlternatives.
# Он позволяет одновременно отправить текстовое сообщение и приложить к нему версию c HTML-разметкой.
# Так, почтовые клиенты способные отображать HTML, будут его показывать, а для остальных будет в приоритете текстовая версия.

# EmailMultiAlternatives - класс из модуля 'django.core.mail', который позволяет отправлять электронные письма с несколькими альтернативными
# форматами содержимого, такими как текст и HTML. Это полезно, когда мы хотим по-разному отображать оформление письма в зависимостей от возможностей почтового клиента получателя.

# # accounts/forms
# from allauth.account.forms import SignupForm
# from django.core.mail import EmailMultiAlternatives

# class CustomSignupForm(SignupForm):
#     def save(self, request):
#         user = super().save(request)
#
#         subject = 'Добро пожаловать на наш сайт!'
#         text = f'{user.username}, вы успешно зарегистрировались на сайте!'
#         html = (
#             f'<b>{user.username}</b>, вы успешно зарегистрировались на сайте '
#             f'<a href="http://127.0.0.1:8000/main">сайте</a>!'
#         )
#         msg = EmailMultiAlternatives(
#             subject=subject, body=text, from_email=None, to=[user.email]
#         )
#         # метод для добавления альтернативного формата содержимого к письму
#         # attach_alternative(html-код, "text/html")
#         msg.attach_alternative(html, "text/html")
#         msg.send()
#
#         return user

"""Рассылка менеджерам и администраторам"""
# Django предоставляет специальные функции для отправки сообщения набору администраторов и менеджеров.
# Для этого в настройках проекта нужно создать и описать группу администраторов и менеджеров, после чего вызвать функцию
# mail_admins или mail_managers. Они отвечают за отправку писем.

# Шаг 1.
# Добавим переменную SERVER_EMAIL, где будет содержаться адрес почты, от имени которой будет отправляться письмо при вызове mail_admin и mail_manager.
# Переменная MANAGERS хранит список имён менеджеров и адресов их почтовых ящиков.
# в файле projects/settings.py
# SERVER_EMAIL = 'example@yandex.ru'
# MANAGERS = (
#     ('Ivan', 'ivan@xx.xx'),
#     ('Igor', 'igor@xx.xx'),
# )

# Шаг 2. Формируем отправку сообщения в файле accounts/forms.py
# from django.core.mail import mail_managers (добавлено)
# # Добавляем в CustomSignupForm
# mail_managers(
#     subject='Новый пользователь',
#     message=f'Пользователь {user.username} зарегистрировался на сайте'
# )



















