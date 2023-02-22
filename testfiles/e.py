import discord
from discord.ext import commands
import threading
from time import sleep
from sys import path
from os import getcwd
path.append(getcwd().rstrip('testfiles'))
from administration import admin
import asyncio

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nready")

async def a():
    print('Hello')
    sleep(5)


@client.command()
async def m(ctx):   

    t = threading.Thread(target = asyncio.create_task(a()))
    t.start()

    '''      
    class B(Thread):
        async def run(self):
            await a()
            pass
            #a()
            #sleep(10)
    b = B()
    b.start()'''






############################
##------------------------##
client.run(admin.discord_.token)##
##------------------------##
############################





