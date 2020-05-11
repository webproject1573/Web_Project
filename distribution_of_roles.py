import discord
from discord import utils


TOKEN = input('Ведите токен:')
# bot token

POST_ID = int(input('Ведите свой POST_ID:')) 
# post id to read reactions from

# roles list according to emotes
ROLES = {
    "🎮": int(input('Введите ID для игровой роли:')),
    # gamer role
    "🎧": int(input('Введите ID для IT роли:')),
    # it
    "🎓": int(input('Введите ID для учённой роли:')),
    # scienctist user
}

# exclude this roles from counting
EXCROLES = ()

MAX_ROLES_PER_USER = 2
# max amount of roles a user can have


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == POST_ID:
            channel = self.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = utils.get(message.guild.members, id=payload.user_id)
            try:
                emoji = str(payload.emoji)
                role = utils.get(message.guild.roles, id=ROLES[emoji])
                if(len([i for i in member.roles if
                        i.id not in EXCROLES])
                        <= MAX_ROLES_PER_USER):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has '
                          'been granted with role {1.name}'.
                          format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.
                          format(member))
            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))

    async def on_raw_reaction_remove(self, payload):
        channel = self.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = utils.get(message.guild.members, id=payload.user_id)
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=ROLES[emoji])
            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user '
                  '{0.display_name}'.format(member, role))
        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


client = MyClient()
client.run(TOKEN)
