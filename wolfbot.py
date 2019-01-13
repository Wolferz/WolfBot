import discord
from discord.ext.commands import Bot
import asyncio
from time import localtime

version = '2.8 Beta'

startup_extensions = ["Music", 'dnd', 'utilities']
bot_prefixes = '!'

client = Bot(bot_prefixes)

dndc = '428010154743693312'  # D&D Text Channel ID


class Main_Commands():
    def __init__(self, client):
        self.bot = client


async def dndscheduler():
    await client.wait_until_ready()
    channel = discord.Object(id=dndc)
    while not client.is_closed:
        hr = 15  # IN JULY (Usually 18, which equals 2PM EST (in July))
        '''
        dasave = daylightSavings.daySave()
        if dasave:
            hr = hr
        elif not dasave:
            hr = hr - 1
        '''
        if localtime().tm_wday == 6 and localtime().tm_hour == hr and localtime().tm_min == 0:
            await client.send_message(channel, '<@&428010612514226214>' + " HOLD ON TO YOUR BUTTS! IT'S D&D TIME" + '\n' + '<@216455910703366144>' + " Don't forget to sneak attack and use lucky ya fool!")
        await asyncio.sleep(60)  # task runs every 60 seconds


@client.command(pass_context=True)
async def load(ctx, extension):
    if 'moderator' in [y.name.lower() for y in ctx.message.author.roles] or ctx.message.author == discord.Server.owner:
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    if 'moderator' not in [y.name.lower() for y in ctx.message.author.roles] and ctx.message.author != discord.Server.owner:
        await client.say('You do not have permission to perform this command.')


@client.command(pass_context=True)
async def unload(ctx, extension):
    if 'moderator' in [y.name.lower() for y in ctx.message.author.roles] or ctx.message.author == discord.Server.owner:
        try:
            client.unload_extension(extension)
            print('Unloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded. [{}]'.format(extension, error))
    if 'moderator' not in [y.name.lower() for y in ctx.message.author.roles] and ctx.message.author != discord.Server.owner:
        await client.say('You do not have permission to perform this command.')


@client.command(pass_context=True)
async def reload(ctx, extension):
    try:
        if 'moderator' in [y.name.lower() for y in ctx.message.author.roles] or ctx.message.author == discord.Server.owner:
            try:
                client.unload_extension(extension)
                await client.say('Unloaded {}'.format(extension))
            except Exception as error:
                await client.say('{} cannot be unloaded. [{}]'.format(extension, error))
            await asyncio.sleep(1)
            try:
                client.load_extension(extension)
                await client.say('Loaded {}'.format(extension))
            except Exception as error:
                await client.say('{} cannot be loaded. [{}]'.format(extension, error))
        if 'moderator' not in [y.name.lower() for y in ctx.message.author.roles] and ctx.message.author != discord.Server.owner:
            await client.say('You do not have permission to perform this command.')
    except AttributeError:
        if ctx.message.author == discord.utils.get(client.get_all_members(), id='257380719729311745'):
            try:
                client.unload_extension(extension)
                await client.say('Unloaded {}'.format(extension))
            except Exception as error:
                await client.say('{} cannot be unloaded. [{}]'.format(extension, error))
            await asyncio.sleep(1)
            try:
                client.load_extension(extension)
                await client.say('Loaded {}'.format(extension))
            except Exception as error:
                await client.say('{} cannot be loaded. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
# TODO Change error handling

'''
@client.event
async def on_command_error(error):
    user = discord.utils.get(client.get_all_members(), id='257380719729311745')
    if user is not None:
        await client.send_message(user, 'ERROR' + '\n' + str(error))
'''


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Version ' + str(version)))


client.loop.create_task(dndscheduler())
client.run('')
