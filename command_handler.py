import time
import typing
import requests

import discord
from discord.ext import commands


class GeorgeCommands(commands.Cog):
    bot = commands.AutoShardedBot(commands.when_mentioned_or('/'), intents=discord.Intents.all())

    def __init__(self, bot):
        self.bot = bot

    def freigabe():
        async def case(ctx):
            return (ctx.author.id == 695885580629704734)  # Walnusskeim

        return commands.check(case)

    @bot.hybrid_command()
    async def george(self, ctx):
        await ctx.send("What's good fam?")

    @bot.hybrid_command(description="Gibt dir Daten zu einem Item auf dem Hypixel Skyblock Bazaar")
    async def summary(self, ctx):
        link = "https://api.slothpixel.me/api/skyblock/bazaar/HOT_POTATO_BOOK"

        response = requests.get(link)
        data = response.json()
        data = data["buy_summary"]

        await ctx.send(data)


    @bot.hybrid_command()
    @freigabe()
    async def syncg(self, ctx):
        print("Syncing...")
        await ctx.send("Hold on a sec mate...")
        await ctx.bot.tree.sync()
        await ctx.send("Sync complete")
        print("Sync complete")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Dieser Befehl existiert nicht bozo!")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Leider fehlt ein Argument! Bitte versuche es noch einmal :)")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send('Du bist nicht cool genug um diesen Befehl auszuführen. Tut mir leid :)')
        else:
            await ctx.send("Ein Fehler ist aufgetreten!")
            print(error)
