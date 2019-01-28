import discord
import openpyxl
import random
import diceRoller
from discord.ext import commands
from time import localtime


class DnD:
    def __init__(self, client):
        self.client = client

    @commands.command(name='roll',
                    description='Use 4d6+2 format to roll the dice. Can add and subtract independently',
                    brief='Rolls Dice',
                    aliases=['rolldice', 'rolls'])
    async def roll(self, dice):
        rolly = diceRoller.diceroller(dice)
        await self.client.say(rolly)

    @commands.command(name='msgdnd',
                      brief='message the dnd channel as wolfbot',
                      pass_context=False)
    async def msgdnd(self, *, message):
        channel = discord.Object(id='428010154743693312')
        await self.client.say('Sending: ' + message + 'to the dnd channel')
        await self.client.send_message(channel, message)

    @commands.command(name='raisehand',
                      brief='Get attention from the dm',
                      pass_context=True)
    async def raisehand(self, ctx):
        dayofweek = localtime().tm_wday
        if dayofweek == 6:  # Sunday Session
            await self.client.start_private_message(discord.User(id='97413850386669568'))
            await self.client.send_message(discord.User(id='97413850386669568'), ctx.message.author.mention +
                                           ' Wants Your Attention')
        elif dayofweek == 4:  # Friday Session
            await self.client.start_private_message(discord.User(id='188981744714776577'))
            await self.client.send_message(discord.User(id='188981744714776577'), ctx.message.author.mention +
                                           ' Wants Your Attention')
        else:
            await self.client.say('There is no session today.')

    @commands.command(name='aroll')
    async def aroll(self, character, *, ability):
        chardir = openpyxl.load_workbook('dnd sheets.xlsx')
        characters = chardir.sheetnames
        blacklist = ['naias',
                     'mira',
                     'gil']
        if character.lower() in blacklist:
            await self.client.say(character.capitalize() + ' is not a supported character for this function')
        elif character.lower() in characters:
            charsheet = chardir[character.lower()]
            ability = ability.lower()
            abilities = {
                'strength': 'B2',
                'dexterity': 'B3',
                'constitution': 'B4',
                'intelligence': 'B5',
                'wisdom': 'B6',
                'charisma': 'B7',
                'acrobatics': 'B8',
                'animal handling': 'B9',
                'animalhandling': 'B9',
                'arcana': 'B10',
                'athletics': 'B11',
                'deception': 'B12',
                'history': 'B13',
                'insight': 'B14',
                'intimidation': 'B15',
                'investigation': 'B16',
                'medicine': 'B17',
                'nature': 'B18',
                'perception': 'B19',
                'performance': 'B20',
                'persuasion': 'B21',
                'religion': 'B22',
                'slight of hand': 'B23',
                'slightofhand': 'B23',
                'stealth': 'B24',
                'survival': 'B25',
            }
            cell = abilities.get(ability)
            if cell is not None:
                modifier = int(charsheet[cell].value)
                roll = random.randint(1, 20)
                result = roll + int(modifier)
                if modifier >= 0:
                    modsy = ' + ' + str(modifier)
                elif modifier < 0:
                    modsy = ' - ' + str(modifier * -1)
                extra = ''
                if roll == 20:
                    extra = ' **Critical Success**'
                elif roll == 1:
                    extra = ' **Critical Failure**'
                await self.client.say('Rolling 1d20' + '\n' + '[' + str(roll) + ']' + modsy + '\n' + 'Total: ' +
                                      str(result) + '\n' + extra)
            else:
                await self.client.say('Unknown Skill')
        else:
            await self.client.say(character.capitalize() +
                                  ' is most likely not in the campaign. Please use first names only.')

    @commands.command(name='char',
                      brief='Displays Character  Sheets',
                      description='Shows the specified character sheet, for The Price of Infinity campaign')
    async def char(self, character):
        chardir = openpyxl.load_workbook('dnd sheets.xlsx')
        characters = chardir.sheetnames
        if character.lower() in characters:
            charsheet = chardir[character.lower()]
            name = str(charsheet['A1'].value)
            desc = str(charsheet['B1'].value + ' : ' + charsheet['C1'].value + '\n' + charsheet['D1'].value)
            image = str(charsheet['D8'].value)
            strength = '**Strength:** ' + str(int(charsheet['B2'].value))
            dexterity = '**Dexterity:** ' + str(int(charsheet['B3'].value))
            constitution = '**Constitution:** ' + str(int(charsheet['B4'].value))
            intelligence = '**Intelligence:** ' + str(int(charsheet['B5'].value))
            wisdom = '**Wisdom:** ' + str(int(charsheet['B6'].value))
            charisma = '**Charisma**: ' + str(int(charsheet['B7'].value))
            acrobatics = '**Acrobatics**: ' + str(int(charsheet['B8'].value))
            animalhandling = '**Animal Handling**: ' + str(int(charsheet['B9'].value))
            arcana = '**Arcana**: ' + str(int(charsheet['B10'].value))
            athletics = '**Athletics**: ' + str(int(charsheet['B11'].value))
            deception = '**Deception**: ' + str(int(charsheet['B12'].value))
            history = '**History**: ' + str(int(charsheet['B13'].value))
            insight = '**Insight**: ' + str(int(charsheet['B14'].value))
            intimidation = '**Intimidation**: ' + str(int(charsheet['B15'].value))
            investigation = '**Investigation**: ' + str(int(charsheet['B16'].value))
            medicine = '**Medicine**: ' + str(int(charsheet['B17'].value))
            nature = '**Nature**: ' + str(int(charsheet['B18'].value))
            perception = '**Perception**: ' + str(int(charsheet['B19'].value))
            performance = '**Performance**: ' + str(int(charsheet['B20'].value))
            persuasion = '**Persuasion**: ' + str(int(charsheet['B21'].value))
            religion = '**Religion**: ' + str(int(charsheet['B22'].value))
            slightofhand = '**Slight of Hand**: ' + str(int(charsheet['B23'].value))
            stealth = '**Stealth**: ' + str(int(charsheet['B24'].value))
            survival = '**Survival**: ' + str(int(charsheet['B25'].value))
            initiative = '**Initiative**: ' + str(int(charsheet['B25'].value))
            proficiency = '**Proficiency Bonus**: ' + str(int(charsheet['D3'].value))
            armour = '**Armour Proficiencies**: ' + str(charsheet['D4'].value)
            weapon = '**Weapon Proficiencies**: ' + str(charsheet['D5'].value)
            tool = '**Tool Proficiencies**: ' + str(charsheet['D6'].value)
            languages = 'Languages: ' + str(charsheet['D7'].value)

            charclass = str(charsheet['D1'].value).lower()
            if charclass == 'barbarian':
                classcolor = discord.Color.orange()
            elif charclass == 'bard':
                classcolor = discord.Color.magenta()
            elif charclass == 'cleric':
                classcolor = discord.Color.light_grey()
            elif charclass == 'druid':
                classcolor = discord.Color.green()
            elif charclass == 'fighter':
                classcolor = discord.Color.red()
            elif charclass == 'monk':
                classcolor = discord.Color.teal()
            elif charclass == 'paladin':
                classcolor = discord.Color.gold()
            elif charclass == 'ranger':
                classcolor = discord.Color.dark_green()
            elif charclass == 'rogue':
                classcolor = discord.Color.darker_grey()
            elif charclass == 'sorcerer':
                classcolor = discord.Color.red()
            elif charclass == 'warlock':
                classcolor = discord.Color.dark_purple()
            elif charclass == 'wizard':
                classcolor = discord.Color.dark_blue()
            elif charclass == 'blood hunter':
                classcolor = discord.Color.dark_red()
            else:
                classcolor = discord.Color.default()

            embed = discord.Embed(
                title=name,
                description=desc,
                colour=classcolor,
            )
            embed.add_field(name=strength, value=constitution, inline=True)
            embed.add_field(name=dexterity, value=intelligence, inline=True)
            embed.add_field(name=wisdom, value='\u200b', inline=True)
            embed.add_field(name=charisma, value='\u200b', inline=True)
            embed.add_field(name='**Abilities:**', value=acrobatics, inline=True)
            embed.add_field(name='\u200b', value=animalhandling, inline=True)
            embed.add_field(name=arcana, value=deception, inline=True)
            embed.add_field(name=athletics, value=history, inline=True)
            embed.add_field(name=insight, value=investigation, inline=True)
            embed.add_field(name=intimidation, value=medicine, inline=True)
            embed.add_field(name=nature, value=performance, inline=True)
            embed.add_field(name=perception, value=persuasion, inline=True)
            embed.add_field(name=religion, value=stealth, inline=True)
            embed.add_field(name=slightofhand, value=survival, inline=True)
            embed.add_field(name=initiative, value=proficiency)
            embed.add_field(name=tool, value=weapon, inline=False)
            embed.add_field(name=armour, value=languages, inline=False)
            try:
                embed.set_thumbnail(url=image)
            except TypeError:
                embed.set_thumbnail(url='https://discordapp.com/assets/f8389ca1a741a115313bede9ac02e2c0.svg')
            await self.client.say(embed=embed)
        else:
            await self.client.say(character.capitalize() +
                                  ' is most likely not in the campaign. Please use first names only.')


def setup(client):
    client.add_cog(DnD(client))
    print('Dnd is loaded')
