import discord
import datetime
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

client = commands.Bot(command_prefix='.')
client.remove_command('help')
bad_words = ['fuck', 'bitch', 'in your mother', 'fuck you']

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


@client.event
async def on_ready():
    print('BOT is ready!')

    await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author.name}, there is no such command on the server!')


@client.event
async def on_message(message):
    await client.process_commands(message)
    msg = message.content.lower()
    if msg in bad_words:
        await message.delete()
        await message.author.send(f'{message.author.name}, not to express!')


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=707261130392862810)

    await member.add_roles(role)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    await ctx.author.send('Hello {}'.format(author.mention))


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Ban', colour=discord.Colour.red())

    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)

    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Ban user', value='Baned user: {}'.format(member.mention))
    emb.set_footer(text='Was banned by the administrator {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Kick', colour=discord.Colour.blue())
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    emb.set_author(name=member.name, icon_url=member.avatar_url)
    emb.add_field(name='Kick user', value='Kick user: {}'.format(member.mention))
    emb.set_footer(text='Was kicked by the administrator {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banners_users = await ctx.guild.bans()
    for i in banners_users:
        user = i.user
        await ctx.guild.unban(user)
        await ctx.send("Unabanned user {}".format(user.mention))
        return


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    emb = discord.Embed(title="Server commands:")
    
    emb.add_field(name='.hello', value='A greeting to the user')
    emb.add_field(name='.clean', value='Clearing messages')
    emb.add_field(name='.kick', value='Deleting a participant from the server')
    emb.add_field(name='.ban', value='Restricting access to the server')
    emb.add_field(name='.unban', value='The removal of restrictions to the server')
    emb.add_field(name='.time', value='Time and date')
    emb.add_field(name='.mute', value='Mute user')
    emb.add_field(name='.send_msg', value='Send greetings')
    await ctx.author.send(author, embed=emb)


@client.command(pass_context=True)
async def time(ctx):
    emb = discord.Embed(title='Exact time', description='Click on "Exact time" to find out the exact time', colour=discord.Color.blue(), url='https://www.timeserver.ru')

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text='Thanks, for using our bot!', icon_url=ctx.author.avatar_url)
    emb.set_image(url='https://yt3.ggpht.com/a/AGF-l7__Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg=s900-c-k-c0xffffffff-no-rj-mo')
    emb.set_thumbnail(url='https://yt3.ggpht.com/a/AGF-l7__Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg=s900-c-k-c0xffffffff-no-rj-mo')

    emb.add_field(name="Time and date:", value='{}'.format(datetime.datetime.now()))

    await ctx.author.send(embed=emb)


@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='MUTE')
    
    await member.add_roles(mute_role)
    await ctx.send('From {}, the restriction of chat, for violations of the rights of the user!'.format(member.mention))


@client.command()
async def send_msg(ctx, member: discord.Member):
    await member.send(f'{member.name}, greetings from {ctx.author.name}')


@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'The bot joined the channel: {channel}')


@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
        await ctx.send(f'The bot leave the channel: {channel}')


@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Старый файл удалён')
    except PermissionError:
        print('[log] Не удалось удалить файл')
        
    await ctx.send('Пожалуйста ожидайте')
    
    voice = get(client.voice_clients, guild=ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку...')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print('[log] Переименовую файл {}'.format(file))
            os.rename(file, 'song.mp3')

    voice.play((discord.FFmpegPCMAudio('song.mp3')), after=lambda e: print('[log] {}, музыка закончила своё проигрывание'.format(name)))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    song_name = name.rsplit('-', 2)
    await ctx.send('Сейчас проигрывается музыка: {}'.format(song_name[0]))


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
