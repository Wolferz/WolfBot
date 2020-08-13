import discord
from discord.ext.commands import Bot
import asyncio
import logging
import config
from time import localtime

version = '3.3'

startup_extensions = ["Music", 'dnd', 'utilities', 'CharacterCommands']
bot_prefixes = '!'

client = Bot(bot_prefixes)

dndc = '428010154743693312'  # D&D Text Channel ID


async def ismoderator(ctx):
    return any(x in config.moderator_roles for x in ctx.message.author.roles)


@client.command()
async def load(ctx, extension):
    if await ismoderator(ctx):
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    elif ctx.message.author == discord.utils.get(client.get_all_members(), id='257380719729311745'):
        try:
            client.load_extension(extension)
            print('Loaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    elif not ismoderator(ctx):
        await ctx.send('You do not have permission to perform this command.')


@client.command()
async def unload(ctx, extension):
    if await ismoderator(ctx):
        try:
            client.unload_extension(extension)
            print('Unloaded {}'.format(extension))
        except Exception as error:
            print('{} cannot be unloaded. [{}]'.format(extension, error))
    elif not ismoderator(ctx):
        await ctx.send('You do not have permission to perform this command.')


@client.command()
async def reload(ctx, extension):
    try:
        if await ismoderator(ctx):
            try:
                client.unload_extension(extension)
                await ctx.send('Unloaded {}'.format(extension))
            except Exception as error:
                await ctx.send('{} cannot be unloaded. [{}]'.format(extension, error))
            await asyncio.sleep(1)
            try:
                client.load_extension(extension)
                await ctx.send('Loaded {}'.format(extension))
            except Exception as error:
                await ctx.send('{} cannot be loaded. [{}]'.format(extension, error))
        elif not await ismoderator(ctx):
            await ctx.send('You do not have permission to perform this command.')
    except AttributeError:
        if ctx.message.author == discord.utils.get(client.get_all_members(), id=config.bot_admin_id):
            try:
                client.unload_extension(extension)
                await ctx.send('Unloaded {}'.format(extension))
            except Exception as error:
                await ctx.send('{} cannot be unloaded. [{}]'.format(extension, error))
            await asyncio.sleep(1)
            try:
                client.load_extension(extension)
                await ctx.send('Loaded {}'.format(extension))
            except Exception as error:
                await ctx.send('{} cannot be loaded. [{}]'.format(extension, error))


@client.command(name='sdu',
                brief='Mods Only',
                no_pm=True)
async def sdu(ctx, password):
    await ctx.message.delete()
    if 'moderator' in [y.name.lower() for y in ctx.message.author.roles]:
        if password == 'wbsd':
            message = await ctx.send('Shutting Down')
            print('Shutdown Utility Activated')
            await asyncio.sleep(3)
            await message.delete()
            await client.logout()
            await asyncio.sleep(2)
            raise SystemExit('Shutdown Via Command')
        else:
            message = await ctx.send('Incorrect Password')
            await asyncio.sleep(3)
            await message.delete(message)
    if 'moderator' not in [y.name.lower() for y in ctx.message.author.roles]:
        message = await ctx.send("You do not have permission to use this command")
        await asyncio.sleep(3)
        await message.delete()


if __name__ == '__main__':
    logger = logging.getLogger('discord')  # Setup Logging
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename='wolfbot.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    for extension in startup_extensions:  # Start Extensions
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

'''
@client.event
async def on_command_error(error):
    user = discord.utils.get(client.get_all_members(), id='257380719729311745')
    if user is not None:
        await channel.send(user, 'ERROR' + '\n' + str(error))
'''


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='Version ' + str(version)))


client.run(config.token)
