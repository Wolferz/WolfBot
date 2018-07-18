import discord
from discord.ext.commands import Bot
import diceRollerV2
import daylightSavings
import asyncio
from time import localtime, timezone

version = 2.1

bot_prefixes = '!', '?'

client = Bot(bot_prefixes)

dndc = '428010154743693312'  # D&D Text Channel ID


async def dndscheduler():
    await client.wait_until_ready()
    channel = discord.Object(id=dndc)
    while not client.is_closed:
        hr = 18
        dasave = daylightSavings.daySave()
        if dasave == True:
            hr = 18
        elif dasave == False:
            hr = 17
        if localtime().tm_wday == 6 and localtime().tm_hour == hr and localtime().tm_min == 0:
            await client.send_message(channel, '<@&428010612514226214>' + " HOLD ON TO YOUR BUTTS! IT'S D&D TIME" + '/n' + '<@216455910703366144>' + " Don't forget to sneak attack ya fool!")
        await asyncio.sleep(60)  # task runs every 60 seconds


@client.command(name='roll',
                description='Use 4d6+2 format to roll the dice',
                brief='Rolls Dice',
                aliases=['rolldice', 'rolls'])
async def roll(dice):
    rolly = diceRollerV2.diceroller(dice)
    await client.say(rolly)


@client.command(name='changeplay',
                 description='Changes the game that the bot is playing',
                 brief='Change the Game')
async def changeplay(game):
    await client.change_presence(game=discord.Game(name=game))
    await client.say("Success! I'm now playing " + game)


@client.command(name='cdndr',
                description='Utility for Finding an Id for Development, Console Required',
                brief='follow with an @mention')
async def cdndr(rle):
    print(rle)
    await client.say('`' + rle + '`')


@client.command(name='hello',
                description='It is good to be polite when meeting new friends',
                brief='Make a first impression',
                aliases=['hi, hia, hiya'],
                pass_context=True)
async def hello(context):
    await client.say('Hello, ' + context.message.author.mention)


@client.command(name='time',
                description='Returns the time of the bot',
                brief='Bot Time')
async def time():
    await client.say('Time: ' + str(localtime().tm_hour) + ':' + str(localtime().tm_min) + '\n' + 'Timezone: ' + str(timezone) + '\n' + 'Daylight Savings: ' + str(localtime().tm_isdst))


@client.command(pass_context=True)
async def stop(context):
    await client.say('Sorry ' + context.message.author.mention + ", I can't let you do that.")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Version ' + str(version)))

client.loop.create_task(dndscheduler())
client.run('TOKEN')
