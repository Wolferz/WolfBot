import discord
from discord.ext.commands import Bot
import diceRoller
import daylightSavings
import asyncio
from time import localtime, timezone
from discord.voice_client import VoiceClient

version = '4 Beta'

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
        hr = 18  # IN JULY (Usually 18, which equals 2PM EST (in July))
        dasave = daylightSavings.daySave()
        if dasave:
            hr = hr
        elif not dasave:
            hr = hr - 1
        if localtime().tm_wday == 6 and localtime().tm_hour == hr and localtime().tm_min == 0:
            await client.send_message(channel, '<@&428010612514226214>' + " HOLD ON TO YOUR BUTTS! IT'S D&D TIME" + '\n' + '<@216455910703366144>' + " Don't forget to sneak attack and use lucky ya fool!")
        await asyncio.sleep(60)  # task runs every 60 seconds


@client.command(name='roll',
                description='Use 4d6+2 format to roll the dice. Can add and subtract independently',
                brief='Rolls Dice',
                aliases=['rolldice', 'rolls'])
async def roll(dice):
    rolly = diceRoller.diceroller(dice)
    await client.say(rolly)


@client.command(name='spam',
                description='Spams a message that follow the command',
                brief='Spams a Message')
async def spam(msg):
    iti = 1
    while iti != 6:
        await client.say(msg)
        iti = iti + 1


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


@client.command(name='movechan',
                pass_context=True,
                no_pm=True)  # FIXME movechan does not work
async def movechan(newchan,context):
    chan = context.message.author.voice_channel
    print(str(chan))
    members = chan.voice_members
    users = []
    for member in members:
        users.append(member.id)
    print(str(users))


@client.command(name='rc',
                description='A ready Check',
                brief='Ready Check',
                aliases=['Readycheck','readycheck'])
async def rc(tot):
    global ready
    tot = int(tot)
    if tot <= 0:
        await client.say('You need to specify how many people we are waiting on')
    else:
        await client.say('Ready Check! Waiting on ' + str(tot) + 'People!' + '\n' + "Ready Up with '!r'")
        ready = 0
        tim = 0
        while ready < tot:
            if tim == (15 * 3):
                await client.say("The ready check has timed out")
                break
            tim = tim + 3
            await asyncio.sleep(3)
        if ready >= tot:
            await client.say('Everyone is Ready!')


@client.command(name='r',
                brief='Used in a Ready Check',
                aliases=['ready'],
                pass_context=True)
async def r(context):
    global ready
    ready = ready + 1
    await client.say(context.message.author.mention + 'has readied up!')


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
                brief='message the dnd as wolfbot',
                pass_context=False)
async def msgdnd(message):
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


@client.event  # TODO Change error handling
async def on_command_error(error,  *args, **kwargs):
    #message = args[0]
    #print('error: ' + str(error))
    #print('args: ' + str(args))
    #print('message: ' + str(message))
    #print('kwargs: ' + str(kwargs))
    #await client.send_message(message.channel, 'ERROR' + '\n' + str(error))
    user = discord.utils.get(client.get_all_members(), id='257380719729311745')
    if user is not None:
        await client.send_message(user, 'ERROR' + '\n' + str(error))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Version ' + str(version)))

client.loop.create_task(dndscheduler())
client.run('TOKEN')
