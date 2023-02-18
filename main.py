import discord
from discord.ext import commands
from threading import Thread
import asyncio

client = commands.Bot(command_prefix = '.')

from darkglance import *

from game_invite import games

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to go")

@client.command()
async def hi(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')
    await ctx.send(embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff))

@client.command()
async def gameinvite(ctx):
    class command_game_invite(Thread):
        def run(self):
            asyncio.run(games.game_invite_(ctx))
    

    command_game_invite().start()

############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################