# import telebot
#
# TOKEN = "7011613703:AAHBD39eBizDTeajFbvdKYzDufZSTzx1SfM"
#
# bot = telebot.TeleBot(TOKEN) # бот - экземпляр класса телебот [?]
#
# bot.polling(none_stop=True) # запускаем бота с помощью метода polling, none_stop=True - параметр, который говорит боту не прекращать работу в случае возникношения ошибок.
#
# @bot.message_handler(content_types=['voice'])# filters - фильтры, определяющие, следует ли вызывать декор.ф. для соотв. сообщ. или нет
# def f_handler(message):
#     bot.reply_to(message, "This is a message handler") # ответ бота


"""Напишите обработчик, который на сообщения с фотографией будет отвечать сообщением «Nice meme XDD».
Бот должен отвечать не отдельным сообщение, а с привязкой к картинке."""

# @bot.message_handler(content_types=['photo'])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')
#
# bot.polling(none_stop=True)

"""Задание:Допишите обработчик так, чтобы он из сообщения брал username и выдавал приветственное сообщение с привязкой к пользователю"""
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")
#
# bot.polling(none_stop=True) # запуск бота

"""Ответ бота на отправленное голосовое сообщение"""
# @bot.message_handler(content_types=['voice'])
# def repeat(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'У тебя красивый голос!') # ответ на голосовое сообщение, отправленное пользователем.
#
# bot.polling(none_stop=True) # запуск бота

"""Примеры обработки команд и контента"""
# # Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     pass
#
# # Обрабатывается все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

"""Парсер"""
# import requests # отправление запросов на сервер и получение ответа
# import lxml.html # обработка данных HTML и XML
# from lxml import etree # модуль etree позволяет создавать элементы XML/HTML и их подэлементы (полезно, если пытаемся написать XML/HTML-файлы или манипулировать ими)
#
# html = requests.get('https://www.python.org/').content # получаем html главной страницы официального сайта python, content используется для получения содержимого страницы (он позволяет получить информацию в виде байтов, то есть в итоге у нас будет вся информация, не только строковая).
#
# tree = lxml.html.document_fromstring(html) # анализирует документ по заданной строке. При этом всегда создаётся правильный html-документ, что означает, что родительским узлом ялвяется <html>, а также есть тело и, возможно, заголовок.
# title = tree.xpath('/html/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]/a/text()')
#
# # title = tree.xpath('/html/head/title/text()') # забираем текст тега <title> из тега <head>, который лежит в свою очередь внутри тега <html>
#
# print(title)

