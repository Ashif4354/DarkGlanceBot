import discord
from discord.ext import commands
from threading import Thread
from time import sleep
from sys import path
from os import getcwd
path.append(getcwd().rstrip('testfiles'))
from darkglance import *

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to go")

def a():
    print('Hello')


@client.command()
async def hello(ctx):   

    a()
    sleep(10) 
    '''        
    class B(Thread):
        def run(self):
            a()
            sleep(10)
    b = B()
    b.start()'''

@client.command()
async def hell(ctx):            
    embed = discord.Embed(description = 'DarkGlanceBot', color = 0xffffff)
    await ctx.send(embed = embed)




############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################





