import telebot
from pytube import YouTube
import sys
import random
from telebot import types
import sqlite3

print('Введите токен:')
tok = '1253588512:AAEfDNBJC0a0ToG8P2DfzDk_gp3U94zXvxU'
bot = telebot.TeleBot(tok)

telegram_bots = {'Игровой-парсер бот. Этот бот парсит информацию с разных источников, например c kanobu (индекс бота #3340)': 'https://yadi.sk/d/-5gIoeh2vsuJ4w?qq=1', 
'PSP - бот. Бот дает информацию об играх на PSP.(индекс бота - #3341)': 'https://yadi.sk/d/4dttKWB8Q28TKw?qq=1', 'Новостной-парсер бот. Бот может парсить информацию о новостях. (индекс бота #3342)': 'https://yadi.sk/d/VvPV2N7LzjIToA?qq=1', 
'Бот-переводчик для телеграмма. Переводит любой текст. (индекс бота - #3343': 'https://yadi.sk/d/VvPV2N7LzjIToA?qq=1'}

vk_bots = {'PSP - бот. Бот дает информацию об играх по разным жанрам и направлениям для psp (индекс бота #3350)': 'https://yadi.sk/d/V5OnW90HyZpxAw?qq=1'}

discord_bots = {'Бот сообщества. Бот имеет большое количество полезных функций, нужных для сообществ дискорда (индекс бота - #3360)': 'https://yadi.sk/d/h6ZWwL7u2iqONg?qq=1', 'Ролеватор. Бот способен давать роли участникам, находящихся в сообществе. Каждый может получить роль, которую захочет(индекс бота - #3361)': 'https://yadi.sk/d/REU1OU3ImT04Vw?qq=1'}

insta_bots = {}

def check(text_mes):
	con = sqlite3.connect('base.db')
	cur = con.cursor()
	try:
		result = cur.execute(
			"""SELECT id FROM users
			WHERE email = ?""", (text_mes,)).fetchall()
		if result == []:
			return False
		else:
			return True
	except:
		return False

 


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    bot.send_message(message.from_user.id, 'Привет, я бот для сайта botworld.ru. Я помогу тебе скачать любого бота для разных соц. сетей. Напиши мне одно из названий: telegram, vk, instagram, discord. Ты должен быть зарегистрирован на нашем сайте botworld.ru, если ты не зарегистрирован, сделай это, займен меньше минуты! Напиши мне свою почту, чтобы я убедился, что ты уже зарегестрирован!')
    if '@' in message.text.lower():
    	if check(message.text.lower()) == True:
    		bot.send_message(message.from_user.id, 'Добро пожаловать')
    	else:
    		bot.send_message(message.from_user.id, 'пшел вон')

    if 'привет' in message.text.lower():
        bot.send_message(message.from_user.id, "Привет, я бот для сайта botworld.ru. Я помогу тебе скачать любого бота для разных соц. сетей. Напиши мне одно из названий: telegram, vk, instagram, discord")


        keyboard = types.InlineKeyboardMarkup()

        key_telegram = types.InlineKeyboardButton(text='Заказать бота', callback_data='order')
        keyboard.add(key_telegram)

        key_telegram = types.InlineKeyboardButton(text='Telegram', callback_data='tele')
        keyboard.add(key_telegram)

        key_vk = types.InlineKeyboardButton(text='ВК', callback_data='vk')
        keyboard.add(key_vk)

        key_instagram = types.InlineKeyboardButton(text='Instagram', callback_data='insta')
        keyboard.add(key_instagram)

        key_discord = types.InlineKeyboardButton(text='Discord', callback_data='dis')
        keyboard.add(key_discord)


        bot.send_message(message.from_user.id, text='Выбери социальную сеть', reply_markup=keyboard)

    elif '#3340' in message.text.lower():
    	for key, val in telegram_bots.items():
    		if '3340' in key:
    			bot.send_message(message.from_user.id, text=val)
    elif '#3341' in message.text.lower():
    	for key, val in telegram_bots.items():
    		if '3341' in key:
    			bot.send_message(message.from_user.id, text=val)
    elif '#3342' in message.text.lower():
    	for key, val in telegram_bots.items():
    		if '3342' in key:
    			bot.send_message(message.from_user.id, text=val)
    elif '#3343' in message.text.lower():
    	for key, val in telegram_bots.items():
    		if '3343' in key:
    			bot.send_message(message.from_user.id, text=val)

    elif '#3350' in message.text.lower():
    	for key, val in vk_bots.items():
    		if '3350' in key:
    			bot.send_message(message.from_user.id, text=val)

    elif '#3360' in message.text.lower():
    	for key, val in discord_bots.items():
    		if '3360' in key:
    			bot.send_message(message.from_user.id, text=val)

    elif '#3361' in message.text.lower():
    	for key, val in discord_bots.items():
    		if '3361' in key:
    			bot.send_message(message.from_user.id, text=val)

    elif '#000' in message.text.lower():
    	f = open('orders.txt', 'w')
    	f.write(message.text)


    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши Привет.")

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    if call.data == "tele": 
        for key, val in telegram_bots.items():
        	bot.send_message(call.message.chat.id, key)
    elif call.data == 'vk':
    	for key, val in vk_bots.items():
        	bot.send_message(call.message.chat.id, key)
    elif call.data == 'dis':
    	for key, val in discord_bots.items():
        	bot.send_message(call.message.chat.id, key)
    elif call.data == 'order':
    	bot.send_message(call.message.chat.id, "Для того, чтобы заказать бота, напишите индекс (#000), затем фамилию, имя и почту. После чего опишите полное требование к боту и цену, на которую вы рассчитываете (в зависимости от сложности бота), далее наши программисты свяжутся с вами")
    else:     # инстаграм
    	msg = 'insta test'
       

bot.polling(none_stop=True, interval=0)