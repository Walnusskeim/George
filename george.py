"""
George. THE bot for watching bazaar prices on Hypixel Skyblock.
Maximilian
❤
28.08.2024
"""

import csv

import discord
from discord.ext import commands, tasks
from command_handler import GeorgeCommands



with open("data.txt") as token:
    reader = csv.reader(token)
    TOKEN = next(reader)

TOKEN = TOKEN[0]

bot = commands.AutoShardedBot(
    commands.when_mentioned_or('/'),
    intents=discord.Intents.all())

#bot.help_command = HelpCommand()


########################################################################

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                  name='the Bazaar prices...'))

    print("----------------------------------")

    print("Oi fam, George is online!")

    await bot.add_cog(GeorgeCommands(bot))
    await bot.tree.sync()

########################################################################

bot.run(TOKEN)