import discord
from discord.ext import commands
from threading import Thread
import asyncio

client = commands.Bot(command_prefix = '.')

from game_invite import games
from administration import admin

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
    thread = Thread(await games.invite(ctx))
    thread.start()
    print(thread.getName())


@client.command()
async def authorize(ctx):
    class CommandAurthorize(Thread):
        def run(self):
            asyncio.new_event_loop().create_task(admin.authorize(ctx))
    print('authorize')
    CommandAurthorize().start()



















@client.command()
async def stopbot(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    exit(0)







############################
##------------------------##
client.run(admin.discord_.token)##
##------------------------##
############################