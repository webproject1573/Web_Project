import telebot
import sys
import random
from telebot import types
import sqlite3

print('������� �����:')
tok = '1138291378:AAFCUM3jniDEyta3_ZeIqlLCGsvhdI9T-bs'
bot = telebot.TeleBot(tok)

telegram_bots = {'�������-������ ���. ���� ��� ������ ���������� � ������ ����������, �������� c kanobu (������ ������ ���� #3340)': 'https://yadi.sk/d/-5gIoeh2vsuJ4w?qq=1',
'PSP - ���. ��� ���� ���������� �� ����� �� PSP.(������ ������ ���� - #3341)': 'https://yadi.sk/d/4dttKWB8Q28TKw?qq=1', '���������-������ ���. ��� ����� ������� ���������� � ��������. (������ ������ ���� #3342)': 'https://yadi.sk/d/VvPV2N7LzjIToA?qq=1',
'���-���������� ��� ����������. ��������� ����� �����. (������ ������ ���� - #3343)': 'https://yadi.sk/d/VvPV2N7LzjIToA?qq=1'}

vk_bots = {'PSP - ���. ��� ���� ���������� �� ����� �� ������ ������ � ������������ ��� psp (������ ������ ���� #3350)': 'https://yadi.sk/d/V5OnW90HyZpxAw?qq=1'}

discord_bots = {'��� ����������. ��� ����� ������� ���������� �������� �������, ������ ��� ��������� ��������': 'https://yadi.sk/d/h6ZWwL7u2iqONg?qq=1', '���������. ��� �������� ������ ���� ����������, ����������� � ����������. ������ ����� �������� ����, ������� �������': 'https://yadi.sk/d/REU1OU3ImT04Vw?qq=1'}

insta_bots = {"� ��� ��� ���� ��� ����� ��� ���������, �� � ������ ������� ��������, �� �� ������ �������� � ��� ��������� ����": ''}

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
    if '������' in message.text.lower():
        bot.send_message(message.from_user.id, '������, � ��� ��� ����� botworld.ru. � ������ ���� ������� ������ ���� ��� ������ ���. �����. �� ������ ���� ��������������� �� ����� ����� botworld.ru, ���� �� �� ���������������, ������ ���, ������ ������ ������! ������ ��� ���� �����, ����� � ��������, ��� �� ��� ���������������!')
    elif '@' in message.text.lower():
        if check(message.text.lower()) == True:
            bot.send_message(message.from_user.id, '����� ����������')
            keyboard = types.InlineKeyboardMarkup()
	
            key_telegram = types.InlineKeyboardButton(text='�������� ����', callback_data='order')
            keyboard.add(key_telegram)
	    
            key_telegram = types.InlineKeyboardButton(text='Telegram', callback_data='tele')
            keyboard.add(key_telegram)
	
            key_vk = types.InlineKeyboardButton(text='��', callback_data='vk')
            keyboard.add(key_vk)
	    
            key_instagram = types.InlineKeyboardButton(text='Instagram', callback_data='insta')
            keyboard.add(key_instagram)
	
            key_discord = types.InlineKeyboardButton(text='Discord', callback_data='dis')
            keyboard.add(key_discord)
	
            bot.send_message(message.from_user.id, text='������ ���������� ����', reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, '� �� ����� ���� ����� � ����� ���� ������, ������� ������� ������������ ��������� ����� ��� ���������������!(botworld.ru)')

	
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

    elif message.text.lower() == '#000':
        bot.send_message(message.from_user.id, '�������� #000, �������, ���, ����� � ���������� � ����.')

    elif '#000' in message.text.lower():
        f = open('orders.txt', 'a')
        f.write(message.text)
        f.write('\n')
        bot.send_message(message.from_user.id, "���� ������ ������� ����������, �����, � ��������� ����� � ���� �������� ���� ������������")
    else:
        bot.send_message(message.from_user.id, "� ���� �� �������. ������ ������.")


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
        bot.send_message(call.message.chat.id, "��� ����, ����� �������� ����, �������� ������ (#000), ����� �������, ��� � �����. ����� ���� ������� ������ ���������� � ���� � ����, �� ������� �� ������������� (� ����������� �� ��������� ����), ����� ���� ������������ �������� � ����")
    else:     # ���������
        msg = 'insta test'


bot.polling(none_stop=True, interval=0)