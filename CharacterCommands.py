import discord
import asyncio
from discord.ext import commands
import json
import os


class CharacterCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def getsheetdir(self):
        global active_chars
        if not os.path.isdir(os.getcwd() + "/charactersheets"):
            print('Character Sheet Directory Not Found, Remaking It')
            try:
                os.mkdir(os.getcwd() + "/charactersheets")
            except OSError as e:
                print('Error In Creating Character Sheet Directory. [{}]'.format(e))
            else:
                print('Current Directory: ' + os.getcwd())
                active_chars = []
        else:
            active_chars = []
            for char in os.listdir(os.getcwd() + '/charactersheets'):
                active_chars.append(char.replace('.json', ''))
            return active_chars

    async def checkfordm(self, message):
        return 'Direct Message with' in str(message.channel)

    # async def checkabilityscore(self, ctx, score):
    #    score = await self.client.wait_for('message', timeout=60, check=lambda message: message.author == ctx.author)
    #    return 1 <= score <= 30

    @commands.command()
    async def pdfimport(self, ctx):
        return 

    @commands.command(name='chardebug')
    async def chardebug(self, ctx):
        chars = await self.getsheetdir()
        directory = os.getcwd() + "/charactersheets"
        await ctx.send("Active Characters: {0}\nDirectory Location:{1}".format(chars, directory))

    @commands.command(name='char')
    async def char(self, ctx, charcommand):
        if charcommand.lower() == 'add':
            if await self.checkfordm(ctx.message):
                await self.addchar(ctx, await self.getsheetdir())
            else:
                await ctx.send('This command can spam public channels, please only use in a private message')
        elif charcommand.lower() == 'edit':
            if await self.checkfordm(ctx.message):
                await self.editchar(ctx)
            else:
                await ctx.send('This command can spam public channels, please only use in a private message')
        elif charcommand.lower() == 'view' or charcommand.lower() in (await self.getsheetdir()):
            await self.getsheetdir()
            if charcommand.lower() == 'view':
                await self.viewchar(ctx, 'none')
            else:
                await self.viewchar(ctx, charcommand.lower())
        elif charcommand.lower() == 'remove':
            if await self.checkfordm(ctx.message):
                await self.getsheetdir()
                await self.removechar(ctx)
            else:
                await ctx.send('This command can spam public channels, please only use in a private message')
        else:
            await ctx.send('Invalid Argument, Please follow with either "add" "change" "view" or "remove"')

    async def addchar(self, ctx, active_chars):
        def check(m):
            return m.author == ctx.author

        await ctx.send('What is the name of the character?')
        cname = (await self.client.wait_for('message', timeout=60, check=check)).content

        if cname.lower() in active_chars:
            await ctx.send('Character with that name already exists.')
            return

        await ctx.send('What race is the character?')
        crace = (await self.client.wait_for('message', timeout=60, check=check)).content

        await ctx.send('What is the level of the character?')
        clevel = (await self.client.wait_for('message', timeout=60, check=check)).content

        await ctx.send('What class is the character?')
        cclass = (await self.client.wait_for('message', timeout=60, check=check)).content

        await ctx.send('Enter URL to image of character. (url ends in .png, .jpg or similar)')
        cimage = (await self.client.wait_for('message',timeout=60, check=check)).content

        await ctx.send('Every single score references the modifier, (usually between -5 and 5)')
        await asyncio.sleep(2)

        await ctx.send("What is the character's Strength score?")
        cstr = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Dexterity score?")
        cdex = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Constitution score?")
        ccon = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Intelligence score?")
        cint = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Wisdom score?")
        cwis = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Charisma score?")
        ccha = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Acrobatics score?")
        cacr = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Animal Handling score?")
        cani = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Arcana score?")
        carc = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Athletics score?")
        cath = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Deception score?")
        cdec = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's History score?")
        chis = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Insight score?")
        cins = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Intimidation score?")
        cinti = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Investigation score?")
        cinv = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Medicine score?")
        cmed = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Nature score?")
        cnat = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Perception score?")
        cperc = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Performance score?")
        cperf = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Persuasion score?")
        cpers = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Religion score?")
        crel = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Slight of Hand score?")
        csli = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Stealth score?")
        cste = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Survival score?")
        csur = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Strength Save?")
        cstrsave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Dexterity Save?")
        cdexsave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Constitution Save?")
        cconsave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Intelligence Save?")
        cintsave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Wisdom Save?")
        cwissave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Charisma Save?")
        cchasave = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Initiative Bonus?")
        cintbon = (await self.client.wait_for('message', timeout=20, check=check)).content

        await ctx.send("What is the character's Proficiency Bonus?")
        cprofbon = (await self.client.wait_for('message', timeout=20, check=check)).content

        cauthor = str(ctx.author)

        character = {
            'name': cname,
            'race': crace,
            'level': clevel,
            'class': cclass,
            'strength': cstr,
            'dexterity': cdex,
            'constitution': ccon,
            'wisdom': cwis,
            'intelligence': cint,
            'charisma': ccha,
            'acrobatics': cacr,
            'animal_handling': cani,
            'arcana': carc,
            'athletics': cath,
            'deception': cdec,
            'history': chis,
            'insight': cins,
            'intimidation': cinti,
            'investigation': cinv,
            'medicine': cmed,
            'nature': cnat,
            'perception': cperc,
            'performance': cperf,
            'persuasion': cpers,
            'religion': crel,
            'slight_of_hand': csli,
            'stealth': cste,
            'survival': csur,
            'strength_save': cstrsave,
            'dexterity_save': cdexsave,
            'constitution_save': cconsave,
            'intelligence_save': cintsave,
            'wisdom_save': cwissave,
            'charisma_save': cchasave,
            'proficiency_bonus': cprofbon,
            'initiative_bonus': cintbon,
            'image': cimage,
            'author': cauthor
        }

        try:
            with open(os.getcwd() + "/charactersheets/" + character.get('name').lower() + '.json', 'w') as char_file:
                char_file.write(json.dumps(character))
        except PermissionError as e:
            await ctx.send('Failure to write file: [{}]'.format(e))
        else:
            await ctx.send('Success! added {0}, call the sheet with !char {0}'.format(character.get('name')))

    async def editchar(self, ctx):
        def check(m):
            return m.author == ctx.author
        characters = await self.getsheetdir()

        await ctx.send('What is the name of the character?')
        cname = (await self.client.wait_for('message', timeout=20, check=check)).content

        if cname.lower() in characters:
            with open(os.getcwd() + '/charactersheets/' + cname.lower() + '.json') as char_file:
                character = json.load(char_file)

            if character.get('author') != str(ctx.author):
                await ctx.send('You do not own this character')
                return

            editor = ''

            async def getedit():
                await ctx.send('What would you like to edit?')
                editor = (await self.client.wait_for('message', timeout=20, check=check)).content
                if editor.lower() in character.keys():
                    await ctx.send('Unknown Ability, Please Try Again')
                    return False, editor.lower()
                else:
                    return True, editor.lower()

            invalid = True
            while invalid is True:
                invalid, editor = await getedit()
            else:
                wordmods = {
                    'name': character.get('name'),
                    'race': character.get('race'),
                    'class': character.get('class'),
                    'image': character.get('image')
                }
                numbermods = {
                    'level': character.get('level'),
                    'strength': character.get('strength'),
                    'dexterity': character.get('dexterity'),
                    'constitution': character.get('constitution'),
                    'wisdom': character.get('wisdom'),
                    'intelligence': character.get('intelligence'),
                    'charisma': character.get('charisma'),
                    'acrobatics': character.get('acrobatics'),
                    'animal handling': character.get('animal_handling'),
                    'arcana': character.get('arcana'),
                    'athletics': character.get('athletics'),
                    'deception': character.get('deception'),
                    'history': character.get('history'),
                    'insight': character.get('insight'),
                    'intimidation': character.get('intimidation'),
                    'investigation': character.get('investigation'),
                    'medicine': character.get('medicine'),
                    'nature': character.get('nature'),
                    'perception': character.get('perception'),
                    'performance': character.get('performance'),
                    'persuasion': character.get('persuasion'),
                    'religion': character.get('religion'),
                    'slight_of_hand': character.get('slight_of_hand'),
                    'stealth': character.get('stealth'),
                    'survival': character.get('survival'),
                    'strength save': character.get('strength_save'),
                    'dexterity save': character.get('dexterity_save'),
                    'constitution save': character.get('constitution_save'),
                    'intelligence save': character.get('intelligence_save'),
                    'wisdom save': character.get('wisdom_save'),
                    'charisma save': character.get('charisma_save'),
                    'initiative bonus': character.get('initiative_bonus'),
                }
                uneditablemods = [
                    'author',
                    'proficiency bonus'
                ]

                async def updater(updatecharacter):
                    try:
                        with open(os.getcwd() + "/charactersheets/" + updatecharacter.get('name').lower() + '.json',
                                  'w') as char_file:
                            char_file.write(json.dumps(updatecharacter))
                    except PermissionError as e:
                        await ctx.send('Failure to write file: [{}]'.format(e))
                    else:
                        await ctx.send(
                            'Success! Updated {0}, call the sheet with !char {0}'.format(character.get('name')))

                if editor in wordmods:
                    await ctx.send('What would you like {} to say'.format(editor.title()))
                    newvalue = (await self.client.wait_for('message', timeout=20, check=check)).content
                    character[editor] = newvalue
                    await updater(character)
                elif editor in numbermods:
                    while True:
                        await ctx.send('What is the new value of {}'.format(editor.title()))
                        newvalue = (await self.client.wait_for('message', timeout=20, check=check)).content
                        try:
                            newvalue = int(newvalue)
                        except ValueError:
                            await ctx.send('That is not a number, {} needs to be a number'.format(editor.title()))
                            continue
                        else:
                            character[editor] = str(newvalue)
                            await updater(character)
                            break

                elif editor in uneditablemods:
                    await ctx.send('Sorry, {} is set automatically and is not editable'.format(editor.title()))
        else:
            await ctx.send('Unknown Character')

    async def removechar(self, ctx):
        def check(m):
            return m.author == ctx.author
        characters = await self.getsheetdir()
        await ctx.send('What is the name of the character?')
        cname = (await self.client.wait_for('message', timeout=20, check=check)).content
        if cname.lower() in characters:
            with open(os.getcwd() + '/charactersheets/' + cname.lower() + '.json') as char_file:
                character = json.load(char_file)
            if character.get('author') == str(ctx.author):
                await ctx.send('Please type DELETE to confirm deletion of character: ' + character.get('name'))
                try:
                    deletion = (await self.client.wait_for('message', timeout=10, check=check)).content
                except TimeoutError:
                    char_file.close()
                    await ctx.send('Cancelled Deletion due to Non-Response')
                else:
                    if deletion == 'DELETE':
                        char_file.close()
                        try:
                            os.remove(os.getcwd() + '/charactersheets/' + cname.lower() + '.json')
                        except OSError as e:
                            print("Error in deleting character: {}".format(e))
                        else:
                            await ctx.send('Successfully removed character: ' + character.get('name'))
                    else:
                        await ctx.send('Cancelled')

    async def viewchar(self, ctx, char):
        def check(m):
            return m.author == ctx.author
        characters = await self.getsheetdir()
        if char == 'none':
            await ctx.send('What is the name of the character?')
            cname = (await self.client.wait_for('message', timeout=20, check=check)).content
        else:
            cname = char
        if cname.lower() in characters:
            with open(os.getcwd() + '/charactersheets/' + cname.lower() + '.json') as char_file:
                character = json.load(char_file)

            name = str(character.get('name'))
            desc = str(character.get('race') + ' : Level ' + character.get('level') + '\n' + character.get('class'))
            image = str(character.get('image'))
            strength = '**Strength:** ' + str(int(character.get('strength')))
            dexterity = '**Dexterity:** ' + str(int(character.get('dexterity')))
            constitution = '**Constitution:** ' + str(int(character.get('constitution')))
            intelligence = '**Intelligence:** ' + str(int(character.get('intelligence')))
            wisdom = '**Wisdom:** ' + str(int(character.get('wisdom')))
            charisma = '**Charisma**: ' + str(int(character.get('charisma')))
            acrobatics = '**Acrobatics**: ' + str(int(character.get('acrobatics')))
            animalhandling = '**Animal Handling**: ' + str(int(character.get('animal_handling')))
            arcana = '**Arcana**: ' + str(int(character.get('arcana')))
            athletics = '**Athletics**: ' + str(int(character.get('athletics')))
            deception = '**Deception**: ' + str(int(character.get('deception')))
            history = '**History**: ' + str(int(character.get('history')))
            insight = '**Insight**: ' + str(int(character.get('insight')))
            intimidation = '**Intimidation**: ' + str(int(character.get('intimidation')))
            investigation = '**Investigation**: ' + str(int(character.get('investigation')))
            medicine = '**Medicine**: ' + str(int(character.get('medicine')))
            nature = '**Nature**: ' + str(int(character.get('nature')))
            perception = '**Perception**: ' + str(int(character.get('perception')))
            performance = '**Performance**: ' + str(int(character.get('performance')))
            persuasion = '**Persuasion**: ' + str(int(character.get('persuasion')))
            religion = '**Religion**: ' + str(int(character.get('religion')))
            slightofhand = '**Slight of Hand**: ' + str(int(character.get('slight_of_hand')))
            stealth = '**Stealth**: ' + str(int(character.get('stealth')))
            survival = '**Survival**: ' + str(int(character.get('survival')))
            initiative = '**Initiative**: ' + str(int(character.get('initiative_bonus')))
            proficiency = '**Proficiency Bonus**: ' + str(int(character.get('proficiency_bonus')))
            strengthsave = '**Strength Save**: ' + str(character.get('strength_save'))
            dexteritysave = '**Dexterity Save**: ' + str(character.get('dexterity_save'))
            constitutionsave = '**Constitution Save**: ' + str(character.get('constitution_save'))
            intelligencesave = '**Intelligence Save**: ' + str(character.get('intelligence_save'))
            wisdomsave = '**Wisdom Save**: ' + str(character.get('wisdom_save'))
            charismasave = '**Charisma Save**: ' + str(character.get('charisma_save'))
            player = 'Player: ' + str(character.get('author'))

            charclass = str(character.get('class')).lower()
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
            elif charclass == 'artificer':
                classcolor = discord.Color.dark_gold()
            else:
                classcolor = discord.Color.default()

            embed = discord.Embed(
                title=name,
                description=desc,
                colour=classcolor,
            )

            embed.add_field(name='\u200b', value=initiative, inline=True)
            embed.add_field(name='\u200b', value=proficiency, inline=True)
            embed.add_field(name='\u200b', value='\u200b', inline=True)

            embed.add_field(name='\u200b', value=strength, inline=True)
            embed.add_field(name='\u200b', value=dexterity, inline=True)
            embed.add_field(name='\u200b', value=constitution, inline=True)
            embed.add_field(name=intelligence, value='\u200b', inline=True)
            embed.add_field(name=wisdom, value='\u200b', inline=True)
            embed.add_field(name=charisma, value='\u200b', inline=True)

            embed.add_field(name='\u200b', value=strengthsave, inline=True)
            embed.add_field(name='\u200b', value=dexteritysave, inline=True)
            embed.add_field(name='\u200b', value=constitutionsave, inline=True)
            embed.add_field(name=intelligencesave, value='\u200b', inline=True)
            embed.add_field(name=wisdomsave, value='\u200b', inline=True)
            embed.add_field(name=charismasave, value='\u200b', inline=True)

            embed.add_field(name=acrobatics, value=athletics, inline=True)
            embed.add_field(name=animalhandling, value=deception, inline=True)
            embed.add_field(name=arcana, value=history, inline=True)

            embed.add_field(name=insight, value=medicine, inline=True)
            embed.add_field(name=intimidation, value=nature, inline=True)
            embed.add_field(name=investigation, value=perception, inline=True)

            embed.add_field(name=performance, value=slightofhand, inline=True)
            embed.add_field(name=persuasion, value=stealth, inline=True)
            embed.add_field(name=religion, value=survival, inline=True)

            embed.set_footer(text=player)

            try:
                embed.set_thumbnail(url=image)
            except TypeError:
                embed.set_thumbnail(url='https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png')
            await ctx.send(embed=embed)
        else:
            await ctx.send('Unknown Character')


def setup(client):
    client.add_cog(CharacterCommands(client))
    print('Character Commands is loaded')
