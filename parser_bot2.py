import telebot
import random
import requests
from bs4 import BeautifulSoup as bs

print('Введите токен')
tok = input()
bot = telebot.TeleBot(tok)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я могу пропарсить сайт stopgame и kanobu, чтоб показать, какие сейчас самые популярные игры. Напиши слово stopgame или kanobu")

    elif 'kanobu' in message.text.lower():
        new = requests.get('https://kanobu.ru/games/pc/popular/')  #обращаемся через request к сайту
        html = bs(new.content, 'html.parser')    

        for i in html.select('.c-game'):    # начинаем парсинг по тегу c-game
            title = i.select('.game-release-date > b')  # определяем еще два тега, в которых и лежит нужная нам инфорамция
            title2 = i.select('.h2 > a')
            bot.send_message(message.from_user.id, 'Игра {}.{}'.format(title2[0].text, title[0].text))   # выводим пользователю в красивом формате

    elif 'stopgame' in message.text.lower():
        new = requests.get('https://stopgame.ru/review/new/stopchoice')
        html = bs(new.content, 'html.parser')    #повторяем все то же самое с другим сайтом
        for i in html.select('.lent-block'):
            title = i.select('.lent-title > a')
            title_2 = i.select('.brief')
            bot.send_message(message.from_user.id, '{} - {}'.format(title[0].text, title_2[0].text))

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Привет.")    # это то, что будет выведено пользователю, в случае неизвестной команды для бота

bot.polling(none_stop=True, interval=0)