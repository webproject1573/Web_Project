import discord 
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
hello_words = ['hi', 'hello', 'привет', 'здравствуйте', 'ky', 'ку']
answer_questions = ['узнать информацию о сервере', 'какая информация вас интересует', 'команды', 'команды сервера', 'что здесь делать']
flag_hello = True
flag_questions = True


@client.event
async def on_ready():
    print('BOT connected')


@client.event
async def on_message(message):
    global flag_hello, flag_questions
    msg = message.content.lower()
    for i in hello_words:
        if (i in msg) and flag_hello:
            await message.channel.send('Привет, мой повелитель!')
            flag_hello = False
        

    for i in answer_questions:
        if i in msg:
            await message.channel.send('Для выполнения данной комнды надо прописать в чат команду .help')
            flag_questions = False
        

client.run(TOKEN)
