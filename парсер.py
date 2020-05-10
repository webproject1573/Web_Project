import telebot
import random
import requests
from bs4 import BeautifulSoup as bs


spis = []
spis2 = []
print('Введите токен')
tok = '1253588512:AAEfDNBJC0a0ToG8P2DfzDk_gp3U94zXvxU'
bot = telebot.TeleBot(tok)

new = requests.get('https://www.vesti.ru/news')
html = bs(new.content, 'html.parser')
for link in html.find_all('a'):
    a = link.get('href')
    if 'doc' in a:
    	spis.append(a)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, напиши ХОЧУ НОВОСТЬ")

    elif 'хочу новость' in message.text.lower():
        linf = random.choice(spis)
        spis2.append(linf)
        a = 'https://www.vesti.ru/'
        b = str(linf)
        c = a + b
        new = requests.get(c)
        html = bs(new.content, 'html.parser')
        for i in html.select('.article'):
        	title2 = i.select('.article__title')
        	print(title2)
    elif 'продолжение' in message.text.lower():
    	a = 'https://www.vesti.ru/'
    	b = str(spis2[-1])
    	c = a + b
    	new = requests.get(c)
    	html = bs(new.content, 'html.parser')
    	for i in html.select('.js-mediator-article'):
        	title = i.select('p')
        	print(title)
bot.polling(none_stop=True, interval=0)






