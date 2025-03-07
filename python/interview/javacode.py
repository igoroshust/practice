




# Библиотеки, модули, пакеты, фреймворк
# Алгоритмы, LIFO/FIFO, Структуры данных, Паттерны проектирования
# Как итерироваться по двум спискам и создать из i[0] - ключ, а из k[0] - значение?
# lambda
# Redis
# Swagger, SwaggerUI
# API, DRF, WebSocket, grpc, OSI простыми словами.
# Как браузер обрабатывает веб-страницу
# Примеры HTTP-Запросов. Как выглядит запрос на получение.
# Статус коды HTTP
# Токен


"""Разобрать Unit-тесты, DOCKER, COMPOSE, SQL"""
# Unit-тесты - метод тестирования ПО, при котором отдельные модули (или юниты) кода проверяются на корректность работы.
# Основная цель unit-тестирования - убедиться, что каждый компонент программы работает так, как задумано, и что изменения
# в коде не приводят к появлению новых ошибок.

# Основные принципы unit-тестирования:
# 1. Изолированность. Каждый тест должен проверять только одну функциональность. Это позволяет легче выявлять и исправлять ошибки.
# 2. Автоматизация. Unit-тесты должны быть автоматизированы, чтобы их можно было запускать регулярно, например, при каждом изменении кода.
# 3. Повторяемость. Тесты должны давать одинаковые результаты при каждом запуске, если код не изменился.
# 4. Документирование. Тесты могут служить документацией к коду, показывая, как он должен работать.

# unittest - встроенный модуль для тестирования
# Пример юнит-тестов (файл calculator.py, затем нужно перейти в файл _test.py)
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b

# Библиотеки для тестирования: pytest, doctest, nise2

# # ---------------------- Unit-тестирование на примере pytest ------------------------
# 1. pip install pytest
# 2. Создадим функции:
# javacode.py
# javacode.py
# def name(s):
#     valid_names = ['igor', 'alice']
#     if s in valid_names:
#         return s
#     else:
#         raise ValueError("Неправильное имя")
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# # Основная функция, которую можно вызывать с заранее известными значениями
# def main():
#     test_name = 'Николай'  # Заранее известная строка
#     try:
#         print(name(test_name))
#     except ValueError as e:
#         print(e)
#
# if __name__ == "__main__":
#     main()

# 3. Называем файл `test_calculator` или `_test.py` (pytest автоматически найдёт все файлы с началом test_ или заканчивающиеся на _test.py`.
# 4. Описываем логику проверки в файле (сейчас это _test.py)
# 5. Запускаем файл pytest или pytest %filename%

# --------------- Преимущества pytest -----------
# 1. Простота. Синтаксис pytest проще и более читаем, чем unittest. Не нужно создавать классы для тестов, если это не требуется.
# 2. Поддержка параметрезации. Вы можете легко параметризовать тесты, что позволяет запускать один и тот же тест с разными входными данными.
# 3. Расширяемость. `pytest` поддерживает плагины, которые могут добавлять новые функции или улучшать функциональность.
# 4. Отчётность. `pytest` предоставляет более подробные и понятные отчёты о тестах, что упрощает отладку.

# ----------------- Параметризация тестов (pytest) ---------------
# В файле _test.py


"""GIT"""
# GiT - распределённая система управления версиями, которая позволяет разработчикам отслеживать изменения в коде, сотрудничать с другими
# разработчиками и управлять проектами.

# Характеристики Git:
# 1. Распределённая система. Гит позволяет каждому разработчику иметь полную копию репозитория на своём локальном компьютере.
# То есть, разработчики могут работать офлайн и выполнять операции без необходимости подключения к центральному серверу.
# 2. Отслеживание изменений. Git позволяет отслеживать изменения в файлах и каталогах, сохраняя историю изменений.
# Это позволяет разработчикам видеть, кто и когда вносил изменения, а также возвращаться к предыдущим версиям кода.
# 3. Ветвление и слияние. Git поддерживает создание веток, что позволяет разработчикам работать над новыми функциями или исправлениями ошибок в изоляции от основной кодовой базы.
# 4. Эффективность. Git оптимизирован для работы с большими проектами и большими файлами. Он использует алгоритмы сжатия и хранения данных, которые делают его быстрым и эффективным.
# 5. Поддержка совместной работы. Git упрощает совместную работу между разработчиками.

# Команды Git:
# git: init, clone, add, commit -m, status, push, pull (получение изменений из удалённого репозитория и их интеграция в локальный),
# branch (просмотр существующих веток и создание новых), checkout (переключение на другую ветку), git merge <branch> - слияние указанной ветки с текущей.



"""REST"""
# REST (Representational State Transfer) - это архитектурный стиль для разработки веб-сервисов, который использует стандарнтые HTTP-методы
# для взаимодействия между клиентом и сервером.

# Основные принципы:
# Клиент-серверная архитектура. Клиент и сервер разделены, что позволяет им развиваться независимо друг от друга.
# Клиент - пользовательский интерфейс и взаимодействие с ним, сервер - обработка запросов и управление данными.
# Пример: клиент отправляет HTTP-запросы к серверу, который обрабатывает их и возвращает данные.

# Без состояния (stateless). Сервер не хранит состояние клиента между запросами.
# Каждый запрос от клиента к серверу должен содержать всю необходимую информацию для его обработки. Это упрощает масштабирование и делает систему более надёжной.
# Если клиент отправляет запрос на получение информации о пользователе, он должен включать все необходимые данные (н-р, токен аутентификации) в заголовок запроса.
# Сервер не будет хранить информацию о предыдущих запросах клиента.
# GET /users/123 HTTP/1.1
# Host: api.example.com
# Authorization: Bearer <token>

# Кэширование. Ответы могут быть кэшированы для повышения производительности. Может происходит на стороне клиента, прокси-сервера или самого сервера.
# Например, если клиент запрашивает список товаров, сервер может указать, что ответ можно кэшировать на 60 секунд.
# В этом случае, если клиент повторно запрашивает тот же список в течении этого времени, он может получить ответ из кэша, а не отправлять новый запрос на сервер.
# HTTP/1.1 200 OK
# Cache-Control: max-age=60
# Content-Type: application/json
#
# [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}

# Единообразный интерфейс. REST использует стандартные HTTP-методы (GET, POST, PUT, DELETE) для выполнения операций над ресурсами.
# GET: Получение ресурса, POST: Создание ресурса, PUT: Обновление существующего ресурса, DELETE: Удаление ресурса.
# API для управления пользователями:
# GET/users, GET/users/123, PUT/users/123, POST/users, DELETE/users/123

# Иерархическая структура ресурсов. Ресурсы идентифицируются с помощью URL, и их представления могут быть в различных форматах (JSON, XML, etc).
# Каждый ресурс может иметь свои подресурсы, что позволяет создавать иерархическую структуру.
# Пример API для управление библиотекой.
# /books - коллекция всех книг
# /books/1 - конкретная книга с ID 1
# /books/1/authors - авторы книги с ID 1
# /authors - коллекция всех авторов
# /authors/2/books - книги автора с ID 2

# Итог
# Принципы REST обеспечивают гибкость, масштабируемость и простоту в разработке веб-сервисов. Следуя этим принципам,
# разработчики могут создавать эффективные и надежные API, которые легко интегрируются с различными клиентскими приложениями.


"""RESTful"""
# RESTful - термин, описывающий веб-сервисы, которые следуют принципам REST.
# Rf-сервисы используют стандартные HTTP-методы и обеспечивают взаимодействие с ресурсами через чётко определённые URL.

# Характеристики RESTful-приложений:
# 1. Использование стандартных HTTP-методов: GET, POST, PUT, DELETE
# 2. Идентификация ресурсов. Ресурсы в RESTful-приложения идентифицируются с помощью уникальных URL. Каждый ресурс (пользователь, товар) имеет свой собственный адрес.
# 3. Форматы представления данных. Rf-приложения могут возвращать данные в различных форматах, таких как JSON, XML, HTML, JSON. JSON - самый популярый из-за лёгкости и удобочитаемости.
# 4. Статус-коды HTTP: 200 (OK) - запрос успешно выполнен, 201 (created) - ресурс успешно создан,
# 204 (No content) - запрос выполнен, нет данных для возврата. 400 (Bad Request) - ошибка в запросе клиента. 404 (Not Found) - запрашиваемый ресурс не найден. 500 - ошибка сервера.
# 5. Без состояния (stateless). Каждый запрос от клиента к серверу должен содержать всю необходимую информацию для его обработки. Сервер не хранит состояние клиента.
# 6. Кэширование. Ответы от сервера могут быть кэшированы, что позволяет уменьшить нагрузку на сервер и ускорить время отклика.


"""REST(ful) API"""
# REST(ful) API - интерфейс программирования приложений, который использует принципы REST для взаимодействия между клиентом и сервером.
# REST API позволяет разработчикам создавать, читать, обновлять и удалять ресурсы через HTTP-запросы.
# REST API часто используется для создания веб-приложений и мобильных приложений, обеспечивая взаимодействие с сервером и доступ к данным.

# RESTApi позволяет клиентам выполнять операции с ресурсами на сервере, используя чётко определённые URL и HTTP-методы.
# RESTAPI - это конкретная реализации REST, которая предоставляет интерфейс для взаимодействия с ресурсами через HTTP.
# RESTApi следует принципам REST и использует их для создания API, который может быть использован клиентами.

# Применение:
# RESTApi - Это конкретный интерфейс, который реализует принципы REST для взаимодействия с ресурсами. REST API используется для создания веб-сервисов, которые могут быть вызваны клиентами.
# Примеры REST API включают API для социальных сетей (Twitter API), API для работы с данными (GitHub API) и API для управления ресурсами (API на вашем сайте по URL)

# Итог:
# RESTApi - конкретная реализация принципов REST в виде интерфейса для взаимодейтсвия с ресурсами через HTTP. Предоставляет клиентам возможность выполнять операции с ресурсами на сервере.
# RESTApi - спосбо, с помощью которого программы могут общаться друг с другом, запрашивая и отправляя данные через интернет, используя стандартные правила и адреса.
# Это конкретная реализации принципов REST в виде интерфейса, который позволяет клиентам взаимодействовать с ресурсами на сервере через HTTP-запросы.


"""Про API"""
# Интерфейс программирования приложений, позволяющий различным программным системам взаимодействовать друг с другом.
# API определяет набор правил и протоколов, позволяющих одной программе запрашивать и использовать функции или данные другой программы.
# API служит "мостом" между различными программами, позволяя им обмениваться данными и функциональностью.
# Определяет, как одна программа может взаимодейтсвовать с другой, какие запросы можно отправлять и какие ответы можно ожидать.

# WebAPI - API, доступные через интернет, которые используют протоколы HTTP/HTTPS. Примеры включают REST API и SOAP API.
# API работает по принципу "запрос-ответ". Клиент (приложение) отправляет запрос к API, а API обрабатывает этот запрос и возвращает ответ.
# Форматы данных: API может использовать различные форматы для передачи данных, наиболее распространёнными из которых являются JSON и XML.

# Пример использования API (приложение о погоде).
# 1. Запрос. Наше приложение отправляет HTTP-запрос к API погодного сервиса, например:
# GET https://api.weather.com/v1/current?location=NewYork
# 2. Ответ. Api обрабатывает запрос и возвращает данные о погоде в формате JSON:
# {
#     "location": "New York",
#     "temperature": "-22",
#     "condition": "Sunny"
# }

# API - мощный инструмент, позволяющий разработчикам интегрировать различные системы и использовать функциональность других приложений.
# Он упрощает процесс разработки, позволяя сосредоточиться на создании новых функций, вместо того чтобы изобретать велосипед, повторно реализуя уже существующие решения.



"""SOAP"""
# Simple Object Access Protocol - ПРОТОКОЛ ОБМЕНА СООБЩЕНИЯ (в отличае от REST - архитектурного стиля), который используется для передачи структурированных данных между компьютерами в сети.
# Он основан на XML и обычно используется для реализации веб-сервисов. SOAP определяет строгие правила для формата сообщений, что делает его более формальным и безопасным по сравнению с другими подходами.
# Основные характеристики SOAP: Протокол, XML, Стандарты (WS-Security), Операции (WSDL - язык описания веб-сервисов)

# SOAP API - это API, который использует протокол SOAP для обмена данными. Он позволяет клиентам взаимодействовать с веб-сервисами, отправляя SOAP-сообщения и получая ответы в формате XML.
# SOAP API часто используется в корпоративных приложениях, где важны безопасность и надёжность.

# Пример SOAP-запроса
# POST /service HTTP/1.1
# Host: www.example.com
# Content-Type: text/xml; charset=utf-8
#
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <GetWeather xmlns="http://www.example.com/weather">
#       <City>New York</City>
#     </GetWeather>
#   </soap:Body>
# </soap:Envelope>


"""gRPC (Remote Procedure Calls)"""
# Это современный фреймворк для удалённых вызовов процедур (RPC), разработанный Google. Он позволяет клиентам и серверам взаимодействовать друг с другом,
# вызывая функции на удалённых машинах, как если бы они были локальными. gRPC использует HTTP/2 для передачи данных, что обеспечивает высокую производительность и поддерку потоковой передачи данных.


"""Swagger"""
# Swagger - набор инструментов и спецификаций, который используется для документирования и тестирования RESTful API.
# Он позволяет разработчикам описывать API в удобочитаемом для людей и машин формате. Swagger помогает упростить процесс разработки,
# тестирования и интеграции API, предоставляя чёткую и понятную документацию.

# Основные компоненты:
# 1. Swagger Specification (OpenAPI spec). Стандартный формат (формат JSON, YAML), описывающий структуру API, включая доступные эндпоинты, методы, параметры, типы данных и ответы.
# 2. Swagger UI. Инструмент, предоставляющий интерактивный интерфейс для документации API. Позволяет тестировать API прямо из браузера.
# Преимущества: документация, интерактивность, наглядность, автоматизация, стандартизация.


"""CI/CD"""
# CI (Continuous Integration)- Это практика разработки программного обеспечения, при которой разработчики регулярно интегрируют свои изменения в общий репозиторий.
# Каждый раз, когда изменения вносятся, автоматически запускаются тесты, чтобы убедиться, что новый код не нарушает существующий функционал.

# CD (Continuous Delivery/Deployment). Delivery означает, что код всегда готов к развёртыванию в производственной среде, но развёртывание может быть выполнено вручную.
# Deployment означает автоматическое развёртывание кода в производственной среде после успешного прохождения всех тестов.

# CI/CD помогает ускорить процесс разработки, улучшить качество кода и снизить риски, связанные с развёртыванием.

"""Фреймворк"""
# Фреймворк - это набор инструментов, библиотек и правил, который предоставляет структуру для разработки приложений.
# Он упрощает процесс разработки, предоставляя разработчикам готовые решения для распространённых задач.
# Фреймворки могут быть специфичными для определённых языков программирования или типов приложений.
# Примеры: Django, Flask, React (?), Angular.

