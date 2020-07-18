import telebot
import random
import requests
from bs4 import BeautifulSoup as bs


spis = []
spis2 = []
   # введите свой токен

tok = input('введите токен:')   # просим ввести токен, узнать его можно, зайдя в диалог с BotFather
bot = telebot.TeleBot(tok)

new = requests.get('https://www.vesti.ru/news')   #этот код нужен,чтобы собрать список все заголовков 
html = bs(new.content, 'html.parser')  
for link in html.find_all('a'):   # прасим по тегам a -> href
    a = link.get('href')
    if 'article' in a:    # здесь мы собираем все ссылки на полную статью, они являются продолжением одной большой ссылки, поэтому начинаются на doc 
        spis.append(a)
        print(spis, 111111)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if 'привет' in message.text.lower():
        bot.send_message(message.from_user.id, "Привет, напиши ХОЧУ НОВОСТЬ и я тебе выберу 1 новость наугад, если захочешь прочитать ее до конца, напиши ПРОДОЛЖЕНИЕ")

    elif 'хочу новость' in message.text.lower():   # пользователю нужно просто показать заголовок
        print(spis)
        linf = random.choice(spis)    # на рандом берем одну статью
        spis2.append(linf)
        a = 'https://www.vesti.ru/'   # вофрмируем
        b = str(linf)                 # полную
        c = a + b                     # ссылку
        new = requests.get(c)     # делаем по ссылке запрос

        html = bs(new.content, 'html.parser')    # начинаем парсить
        for i in html.select('.article'):
            title2 = i.select('.article__title')
            bot.send_message(message.from_user.id, title2)   # выводится только заголовок

    elif 'продолжение' in message.text.lower():    # если пользователю понравился заголовок, выводим полную статью
        if len(spis2) > 0:    # условие, чтобы избежать случая, что заголовок еще не предложен пользователю, а он уже просит продолжение
            
            a = 'https://www.vesti.ru/'    # формируем полную ссылку
            b = str(spis2[-1])
            c = a + b
            new = requests.get(c)

            html = bs(new.content, 'html.parser')   # парсим потегу js-mediator-article и выбираем все теги с подписью P(их там 4, так как текст разбит на 4 части)
            for i in html.select('.js-mediator-article'):
                title = i.select('p')
            print(title)
            result_list = []   # в текст попадает и html код, поэтому фильтруем его
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
                if i not in '><brpahefitqwertyuiopasdfghjklzxcvbnmWERTYUIOPASDFGHJKLZXCVBNM/=':
                    spisok.append(str(i))

            res = ''.join(spisok)    # в результате получаем собранный текст и выводим его пользователю

            bot.send_message(message.from_user.id, res)
        else:
            bot.send_message(message.from_user.id, 'сначала нужно подобрать новость, напиши ХОЧУ НОВОСТЬ')
bot.polling(none_stop=True, interval=0)