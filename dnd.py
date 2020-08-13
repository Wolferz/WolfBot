import discord
import openpyxl
import random
import asyncio
import os
from random import randint
import diceRoller
from discord.ext import commands
from randomCharacterCreator import create_random_character


class DnD(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='roll')
    async def roll(self, ctx, *, selection):
        await ctx.send(diceRoller.roller(selection))

    @commands.command(name='rollstats')
    async def rollstats(self, ctx, *, u_msg):
        stats = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': []}
        mathstats = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': []}
        for stat in stats:
            i = 0
            while i < 4:
                i += 1
                roll = 1
                while roll == 1:
                    roll = randint(1, 6)
                else:
                    stats[stat].append(roll)
                    mathstats[stat].append(roll)

        for stat in stats:
            strrolls = []
            for roll in stats[stat]:
                if roll == min(stats[stat]) and '~~' + str(roll) + '~~' not in strrolls:
                    roll = '~~' + str(roll) + '~~'
                strrolls.append(str(roll))
            stats[stat] = strrolls

        for stat in mathstats:
            mathstats[stat].remove(min(mathstats[stat]))
            mathstats[stat] = sum(mathstats[stat])
        fstats = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': []}
        for stat in fstats:
            fstats[stat] = str(stats[stat]) + ' -> ' + str(mathstats[stat])

        # print(stats)
        # print(mathstats)
        msg = "Rolling Random Stats using 4d6, Dropping the Lowest, Re-rolling 1s:\n{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}"
        await ctx.send(msg.format(fstats['1'], fstats['2'], fstats['3'], fstats['4'], fstats['5'], fstats['6'], u_msg))

    @commands.command(name='msgdnd',
                      brief='message the dnd channel as wolfbot')
    async def msgdnd(self, ctx, *, message):
        channel = self.client.get_channel(519722527908429829)
        await ctx.send('Sending: "' + message + '" to the dnd channel')
        await channel.send(message)

    @commands.command(name='charactermancer',
                      brief='Quick level 1 character builder, ready to go!')
    async def charactermancer(self, ctx):
        name, file_path, scores, race, c_class = create_random_character()
        if os.path.isfile(file_path):
            fmt = "Created randomized character:\n{0}\n{1} {2} Level:1\nStr:{3} Dex:{4} Con:{5} Int:{6} Wis:{7} Cha:{8}"
            msg = fmt.format(name, race.capitalize(), c_class.capitalize(), scores["str"],
                             scores["dex"], scores["con"], scores["int"], scores["wis"], scores["cha"])
            with open(file=file_path, mode="rb") as file:
                binaryfile = discord.File(file, filename=name + ".xlsx")
                await ctx.send(content=msg, file=binaryfile)
            os.remove(file_path)
        else:
            await ctx.send(name)


def setup(client):
    client.add_cog(DnD(client))
    print('Dnd is loaded')
