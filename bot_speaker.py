import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command('help')

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
hello_words = ['hi', 'hello', 'привет', 'здравствуйте', 'ky', 'ку']
answer_questions = ['узнать информацию о сервере',
                    'какая информация вас интересует',
                    'команды', 'команды сервера',
                    'что здесь делать']
sign = "'!@#№$;:/|}{][><*&^%?'"


@client.event
async def on_ready():
    print('BOT is ready!')


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@client.command(pass_context=True)
async def hello(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    author = ctx.message.author
    await ctx.send('Hello {}'.format(author.mention))


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send('Ban user {}'.format(member.mention))


@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)
    await ctx.send('Kick user {}'.format(member.mention))


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
    await ctx.send(author, embed=emb)

client.run(TOKEN)
