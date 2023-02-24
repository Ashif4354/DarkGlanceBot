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
async def hii(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')
    await ctx.send(embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff))

@client.command()
async def game(ctx):
    '''
    def invite_():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = loop.run_in_executor(None, games.invite, ctx)
        loop.run_until_complete(future)
        loop.close()
    
    
    
    class game_(Thread):
        def run(self):
            #loop = asyncio.new_event_loop()
            #asyncio.set_event_loop(loop)
            #task = loop.create_task(games.invite(ctx))
            #asyncio.run(asyncio.gather(task))
            #await games.invite(ctx)
            invite_()

    
    game_().start()
    '''
    
    task = asyncio.create_task(games.invite(ctx))
    result = await asyncio.gather(task, asyncio.sleep(5))
    print(result)
    

    



    #await asyncio.get_running_loop().run_in_executor(None, await games.invite(ctx))
    #print('hi')
    #await asyncio.to_thread(games.invite(ctx))
































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