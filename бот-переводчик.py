# бот - переводчик
import telebot
import random
import requests
from langdetect import detect


bot = telebot.TeleBot('1123646527:AAGfUxduzp-kFliZbKGH1syRo45Yu6jtZjs')


def get_translation(text, lang):
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
    KEY = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
    TEXT = text
    LANG = lang
    r = requests.post(URL, data={'key': KEY, 'text': TEXT, 'lang': LANG})
    return eval(r.text)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    lan = detect(message.text)
    if 'ы' in message.text or 'у' in message.text or 'к' in message.text or 'е' in message.text or 'н' in message.text or 'г' in message.text or 'я' in message.text or 'в' in message.text or 'а' in message.text or 'р' in message.text or 'и' in message.text or 'о' in message.text or 'ю' in message.text or lan == 'mk' or lan == 'ru':
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
        KEY = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
        TEXT = message.text
        LANG = 'en'
        r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate?', data={'key': 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97', 'text': message.text, 'lang': 'en'})        
        bot.send_message(message.from_user.id, eval(r.text)['text'])
    
    if 'q' in message.text or 'w' in message.text or 'e' in message.text or 'r' in message.text or 't' in message.text or 'y' in message.text or 'u' in message.text or 'i' in message.text or 'o' in message.text or 'p' in message.text or 'a' in message.text or 's' in message.text or 'd' in message.text or 'f' in message.text or 'g' in message.text or 'h' in message.text or 'j' in message.text or 'k' in message.text or 'l' in message.text or 'z' in message.text or 'x' in message.text or 'c' in message.text or 'v' in message.text or 'b' in message.text or 'n' in message.text or 'm' in message.text:
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
        KEY = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97' 
        TEXT = message.text
        ri = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate?', data={'key': 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97', 'text': message.text, 'lang': 'ru'})        
        bot.send_message(message.from_user.id, eval(ri.text)['text'])
    
    

bot.polling(none_stop=True, interval=0)

