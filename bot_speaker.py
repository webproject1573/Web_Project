import discord
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command('help')

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


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

    await ctx.send(author, embed=emb)


@client.command(pass_context=True)
async def time(ctx):
    emb = discord.Embed(title='Exact time', description='Click on "Exact time" to find out the exact time', colour=discord.Color.blue(), url='https://www.timeserver.ru')

    emb.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    emb.set_footer(text='Thanks, for using our bot!', icon_url=ctx.author.avatar_url)
    emb.set_image(url='https://yt3.ggpht.com/a/AGF-l7__Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg=s900-c-k-c0xffffffff-no-rj-mo')
    emb.set_thumbnail(url='https://yt3.ggpht.com/a/AGF-l7__Vf7dLdr-fCTm0dN4GbnBMVoTjm4MOWmatg=s900-c-k-c0xffffffff-no-rj-mo')

    emb.add_field(name="Time and date:", value='{}'.format(datetime.datetime.now()))

    await ctx.send(embed=emb)

client.run(TOKEN)
