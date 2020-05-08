import discord
import datetime
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

client = commands.Bot(command_prefix='.')
client.remove_command('help')
bad_words = ['fuck', 'bitch', 'in your mother', 'fuck you']
# данный массив был написан с целью не 
# оскорбить кого-либо, а избавить сервер от плохих слов

TOKEN = 'NzA2ODgyMDc0OTM3Nzg2NDA4.XrAukw.BzGFlu2wFklfZDELDmAseBzOP10'


# указываем ТОКЕН для точто чтобы подключится к серверу


@client.event
async def on_ready():
    print("Logged in as: " + client.user.name + "\n")
    # сообщаем о подключении Бота к северу
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('.help'))


# удаляем команду .help для дальнейшей работы


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author.name}, '
                       f'there is no such command on the server!')


# создаем обработчик ошибок
# который говорит что нету такой команды 


@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content.lower()
    if msg in bad_words:
        await message.delete()
        await message.author.send(f'{message.author.name}, '
                                  f'not to express!')


# филт чата


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=707261130392862810)

    await member.add_roles(role)


# выдача роли при входе на сервер


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


# очистка чата


@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    await ctx.author.send('Hello {}'.format(author.mention))


# приветсвие пользователя


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Ban',
                        colour=discord.Colour.red())
    # задаём заголовок
    await ctx.channel.purge(limit=1)
    # удаляем сообщение
    await member.ban(reason=reason)
    # далее просто занимаемся интрефейсом сообщения
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Ban user', value='Baned user: '
                                         '{}'.
                  format(member.mention))
    emb.set_footer(text='Was banned by the administrator {}'.
                   format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


# бан участника


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    # настройка интерфейса сообщения
    emb = discord.Embed(title='Kick', colour=discord.Colour.blue())
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Kick user', value='Kick user: {}'.
                  format(member.mention))
    emb.set_footer(text='Was kicked by the administrator {}'.
                   format(ctx.author.name),
                   icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
# кик участника


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    # удаляем сообщение
    banners_users = await ctx.guild.bans()
    # получаем список забаненых участников
    # ищем нужного участника
    for i in banners_users:
        user = i.user
        await ctx.guild.unban(user)
        # разбаниваем участника
        await ctx.send("Unabanned user {}".
                       format(user.mention))
        return


# анбан участника

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    emb = discord.Embed(title="Server commands:")
    # тут мы выводим все команды сервера
    emb.add_field(name='.hello', value='A greeting to the user')
    emb.add_field(name='.clean', value='Clearing messages')
    emb.add_field(name='.kick', value='Deleting a participant from the server')
    emb.add_field(name='.ban', value='Restricting access to the server')
    emb.add_field(name='.unban',
                  value='The removal of restrictions to the server')
    emb.add_field(name='.time', value='Time and date')
    emb.add_field(name='.mute', value='Mute user')
    emb.add_field(name='.send_msg', value='Send greetings')
    emb.add_field(name='.music', value='Send music file from YouTube')
    await ctx.author.send(author, embed=emb)


# команда help

@client.command(pass_context=True)
async def time(ctx):
    emb = discord.Embed(title='Exact time',
                        description='Click on '
                                    '"Exact time" to find out the exact time',
                        colour=discord.Color.blue(),
                        url='https://www.timeserver.ru')
    # задаем заголовок
    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    # задаем имя и аву
    emb.set_footer(text='Thanks, for using our bot!',
                   icon_url=ctx.author.avatar_url)
    # задаём текст к аве
    emb.set_image(url='https://yt3.ggpht.com/a/AGF-l7__'
                      'Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg'
                      '=s900-c-k-c0xffffffff-no-rj-mo')
    # задаем картинку по ссылке
    emb.set_thumbnail(url='https://yt3.ggpht.com/a/AGF-l7__'
                          'Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg='
                          's900-c-k-c0xffffffff-no-rj-mo')
    # задаем картинку по ссылке
    emb.add_field(name="Time and date:", value='{}'.
                  format(datetime.datetime.now()))
    # печатаем время
    await ctx.author.send(embed=emb)


# выводим время

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    # удаляем последнее сообщение
    mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTE')
    # вытаскиваем роль
    await member.add_roles(mute_role)
    # добавляем роль
    await ctx.send('From {}, the restriction of chat, '
                   'for violations of the rights '
                   'of the user!'.format(member.mention))


# выводим на печать сообщения
# команда запрещения сообщений

@client.command()
async def send_msg(ctx, member: discord.Member):
    await member.send(f'{member.name}, greetings from {ctx.author.name}')


# отправляем в личку приветствие

@client.command()
async def music(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    #
    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Старый файл удалён')
    except PermissionError:
        print('[log] Не удалось удалить файл')
    # обработка ошибок
    await ctx.send('Please wait')
    # посылаем сообщение
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    # задаём праметры для музыки
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку...')
        ydl.download([url])
    # загружаем музыку с YouTube
    for file in os.listdir('./'):
        # ищем файл с раширанием mp3
        if file.endswith('.mp3'):
            name = file
            print('[log] Высылаю файл {}'.format(file))
            os.rename(file, 'song.mp3')
            # переименовыем файл 
    await ctx.author.send(file=discord.
                          File(open('song.mp3',
                                    "rb"), name))


# выслылаем музыку лично пользователю

# обработка ошибок на подобии отсуствуют права или не указан аргумент
@music.error
async def music_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the arguments!')


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the arguments!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, you don`t have enough rights!')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the user!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, you don`t have enough rights!')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the user!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, you don`t have enough rights!')


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the user!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, you don`t have enough rights!')


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, you must specify the user!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.name}, you don`t have enough rights!')


client.run(TOKEN)
# запуск бота
