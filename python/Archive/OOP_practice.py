import requests
import json


"""Напишите программу, которая отправляет запрос на генерацию случайных текстов, выведите первый их них.
Сервис: https://baconipsum.com/api/"""
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# r = json.loads(r.content)
# print(r[0])


"""Отправляем POST-запрос в нужном(?) формате"""
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(data)) # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)


"""Отправляем POST-запрос"""
# r = requests.post('https://httpbin.org/post', data =
# {'key': 'value'}) # отправляем post-запрос
# print(r.content) # содержимое ответа и его обработка происходит так же, как и с ГЕТ-запросами, разницы нет никакой.


"""Перевод полученной информации в словарь"""
# r = requests.get('https://api.github.com')
# d = json.loads(r.content) # делаем из полученных байтов Python-объект для удобной работы
#
# print(type(d))
# print(d['following_url']) # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений.

"""Пример GET-зароса"""
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler') # делаем запрос на сервер по переданному адресу
# print(r.content)
# texts = json.loads(r.content) # делаем из полученных байтов Python-объект для удобной работы
# print(type(texts))
#
# for text in texts: # выводим полученный текст, но только первые 50 символов, чтобы он влез в консоль
#     print(text[:50], '\n')