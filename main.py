import discord
from discord.ext import commands
import threading
import asyncio

client = commands.Bot(command_prefix = '.')

from game_invite import games
from administration import admin

class AsyncLoopThread(threading.Thread):
    def __init__(self, coro):
        super().__init__()
        self.loop = asyncio.new_event_loop()
        self.coro = coro
        self.done = threading.Event()

    def run(self):
        asyncio.set_event_loop(self.loop)
        task = self.loop.create_task(self.coro)
        task.add_done_callback(self.set_done)
        self.loop.run_forever()

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.done.wait()

    def set_done(self, fut):
        self.done.set()

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to go")

@client.command()
async def hii(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')
    await ctx.send(embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff))

@client.command()
async def game(ctx):
    #games.invite(ctx)

    async_loop_thread = AsyncLoopThread(games.invite(ctx))
    async_loop_thread.start()



























'''
@client.command()
async def authorize(ctx):
    class CommandAurthorize(Thread):
        def run(self):
            asyncio.new_event_loop().create_task(admin.authorize(ctx))
    print('authorize')
    CommandAurthorize().start()


'''
















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