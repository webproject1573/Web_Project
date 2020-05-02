import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
hello_words = ['hi', 'hello', 'привет', 'здравствуйте', 'ky', 'ку']
answer_questions = ['узнать информацию о сервере',
                    'какая информация вас интересует',
                    'команды', 'команды сервера',
                    'что здесь делать']
sign = "'!@#№$;:/|}{][><*&^%?'"


@client.event
async def on_ready():
    print('BOT connected')


@client.event
async def on_message(message):
    msg = message.content.lower().split(' ')
    msg_ = message.content.lower()
    for i in msg:
        if i[-1] in sign:
            await message.channel.send('Бот не может рабоать со знаками препинаия на конце слова')
        if i in hello_words:
            await message.channel.send('Привет, мой повелитель!')
    if msg_ in answer_questions:
        await message.channel.send('Чтобы узнать данную информацию пропишите .help')


client.run(TOKEN)
