import discord
from discord.ext import commands
from random import choice
import otp_sites
import asyncio

from sys import path
from os import getcwd
path.append(getcwd().rstrip('sms_blaster'))
from logger.logger import logger
from darkglance import *

client = commands.Bot(command_prefix = '.')

sms_sent = {}  
total_sms_sent = 0
stop = False

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to blast sms")


@client.command(aliases = ['smsb'])
async def smsblast(ctx):#[.smsblast <ph_number> <count> <delay>] .smsblast 9566782699 2 5
    global sms_sent, stop, total_sms_sent
    
    logger.input_sms_blast(ctx, getcwd().rstrip('sms_blaster') + '\logger')

    if not await check_auth(ctx, ('owner', 'admin')):
        return

    command = ctx.message.content.split()

    try:
        ph_num = command[1]
    except :
        embed = discord.Embed(title = 'Phone number not entered or Invalid input', description = ctx.message.author.mention, color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    #---------------------------------------------------------------------------------------------
    if ph_num in ('+919566782699', '9566782699'):
        embed = discord.Embed(title = 'If you are bad, DarkGlance is your dad', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    #---------------------------------------------------------------------------------------------
    
    try:
        count = int(command[2])
        if not count >= 0:
            raise NegativeNumber
    except IndexError:
        embed = discord.Embed(title = 'Count not entered or Invalid input', description = ctx.message.author.mention, color = 0xffffff)
        await ctx.send(embed = embed)
        return
    except NegativeNumber:
        embed = discord.Embed(title = 'Count cannot be negative', description = ctx.message.author.mention, color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        delay = int(command[3])
        if delay < 5:
            raise InvalidDelay

    except IndexError:
        delay = 10
    except InvalidDelay:
        embed = discord.Embed(title = 'Delay time cannot be less than 5 seconds', description = ctx.message.author.mention, color = 0xffffff)
        await ctx.send(embed = embed)
        return

    sms_sent[ph_num] = 0
    #print(sms_sent)
    
    embed = discord.Embed(title = 'SMS Blasting..', description =  f'Number : {ph_num}\nCount : {count}\nDelay : {delay}\n' + ctx.message.author.mention, color = 0xffffff)
    await ctx.send(embed = embed)
    
    for count_ in range(count):
        if stop:
            stop = False
            break

        choice(otp_sites.sites)(ph_num)

        try:
            sms_sent[ph_num] += 1
        except:
            return

        total_sms_sent += 1
        
        await asyncio.sleep(delay)
    else:
        embed = discord.Embed(title = 'SMS Blasted', description =  f'Number : {ph_num}\n{sms_sent[ph_num]} sms sent\n' + ctx.message.author.mention, color = 0xffffff)
        await ctx.send(embed = embed)
        
        del sms_sent[ph_num]


@client.command()
async def stopsms(ctx):
    global sms_sent, stop, total_sms_sent

    if not await check_auth(ctx, ('owner', 'admin')):
         return

    stop = True

    embed = discord.Embed(title = 'SMS Blasting stopped', description =  f'{total_sms_sent} sms sent in total', color = 0xffffff)
    for ph_num in sms_sent:
        embed.add_field(name = ph_num, value = sms_sent[ph_num], inline = False)
    await ctx.send(embed = embed)      
    
    sms_sent = {}
    total_sms_sent = 0    

@client.command()
async def stopbot(ctx):

    if not await check_auth(ctx, ('owner',)):
        return

    exit(0)      
    








############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################

    
