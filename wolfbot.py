import discord
from discord.ext.commands import Bot
import diceRollerV2
import daylightSavings
import asyncio
from time import localtime, timezone
from discord.voice_client import VoiceClient

version = '3.1'

startup_extensions = ["Music"]

bot_prefixes = '!', '?'

client = Bot(bot_prefixes)

dndc = '428010154743693312'  # D&D Text Channel ID

class Main_Commands():
    def __init__(self,client):
        self.bot = client

async def dndscheduler():
    await client.wait_until_ready()
    channel = discord.Object(id=dndc)
    while not client.is_closed:
        hr = 18  #IN JULY (Usually 18, which equals 2PM EST (in July))
        dasave = daylightSavings.daySave()
        if dasave == True:
            hr = hr
        elif dasave == False:
            hr = hr - 1
        if localtime().tm_wday == 6 and localtime().tm_hour == hr and localtime().tm_min == 0:
            await client.send_message(channel, '<@&428010612514226214>' + " HOLD ON TO YOUR BUTTS! IT'S D&D TIME" + '\n' + '<@216455910703366144>' + " Don't forget to sneak attack and use lucky ya fool!")
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
async def shutdown(context):
    await client.say('Sorry ' + context.message.author.mention + ", I can't let you do that.")


@client.command(name='msgdnd',
                brief='msg dnd',
                pass_context=True)
async def msgdnd(message,context):
    channel = discord.Object(id=dndc)
    await client.say('Sending: ' + message + 'to the dnd channel')
    await client.send_message(channel, message)

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Version ' + str(version), url='about:blank', type=1))

client.loop.create_task(dndscheduler())
client.run('Token')
