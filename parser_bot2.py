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
        new = requests.get('https://kanobu.ru/games/pc/popular/')
        html = bs(new.content, 'html.parser')

        for i in html.select('.c-game'):
            title = i.select('.game-release-date > b')
            title2 = i.select('.h2 > a')
            bot.send_message(message.from_user.id, 'Игра {}.{}'.format(title2[0].text, title[0].text))

    elif 'stopgame' in message.text.lower():
        new = requests.get('https://stopgame.ru/review/new/stopchoice')
        html = bs(new.content, 'html.parser')
        for i in html.select('.lent-block'):
            title = i.select('.lent-title > a')
            title_2 = i.select('.brief')
            bot.send_message(message.from_user.id, '{} - {}'.format(title[0].text, title_2[0].text))

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Привет.")

bot.polling(none_stop=True, interval=0)