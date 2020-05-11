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

    if 'привет' in message.text.lower():
        bot.send_message(message.from_user.id, "Привет, напиши ХОЧУ НОВОСТЬ и я тебе выберу 1 новость наугад, если захочешь прочитать ее до конца, напиши ПРОДОЛЖЕНИЕ")

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
        	bot.send_message(message.from_user.id, title2)
    elif 'продолжение' in message.text.lower():
    	if len(spis2) > 0:
    		a = 'https://www.vesti.ru/'
    		b = str(spis2[-1])
    		c = a + b
    		new = requests.get(c)
    		html = bs(new.content, 'html.parser')
    		for i in html.select('.js-mediator-article'):
        		title = i.select('p')
    		result_list = []
    		spisok = []
    		delete_flag = False
    		for char in title:
        		if char == "<":
        			delete_flag = True
        		if char == ">":
        			delete_flag = False
        		if not delete_flag and char != ">":
        			result_list.append(str(char))

    		result = "".join(result_list)
    		print(str(result))
    		new = str(result)
    		sps = []
    		for i in range(len(new)):
    			sps.append(new[i])
    		for i in sps:
    			if i not in '><brpahefitqwertyuiopasdfghjklzxcvbnm/=':
    				spisok.append(str(i))

    		res = ''.join(spisok)
 
        	
    		bot.send_message(message.from_user.id, res)
    		print(title)
    	else:
    		bot.send_message(message.from_user.id, 'сначала нужно подобрать новость, напиши ХОЧУ НОВОСТЬ')
bot.polling(none_stop=True, interval=0)