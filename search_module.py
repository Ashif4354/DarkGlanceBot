import discord
from discord.ext import commands
from darkglance import *
from kcg.Student import student, server_down
from logger.logger import logger
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to Search")

@client.command(aliases=['kcgs', 'search'])
async def kcgsearch(ctx): # .kcgs 2020 ashif cs
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')     

    if not await check_auth(ctx, ('owner')):
        return
        
    command = ctx.message.content.split()
    #print(command)
    
    try:
        if len(command[1]) == 4 :
            batch = str(int(command[1]) % 100)
        else:
            raise Exception
    except:
        embed = discord.Embed(title = 'Invalid Year / Invalid Input', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        search_text = command[2].upper().strip("' ")
    except:
        embed = discord.Embed(description = 'No id was given', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    depts = command[3:]
    
    try:
        if depts[0].lower() == 'all':
            depts = ['all']
            if not await check_auth(ctx, ('owner',), 'You are not authorized to search all departments'):
                return
    except IndexError:
        pass

    embed = discord.Embed(title = 'Search started..', description =  f'Batch : {batch}\nKeyword : {search_text}\n departments = {depts}', color = 0xffffff)
    await ctx.send(embed = embed)

    try:
        students = student.search(batch, search_text, depts, log_path = f'{os.getcwd()}\logger\searchlogs\\')
    except server_down:
        await ctx.send(embed = server_error_embed)
        return

    #print(students)

    if not students == []:
        embed = discord.Embed(title = 'Search results for {} {}'.format(command[1], search_text), color = 0xffffff)
        for i in students:
            embed.add_field(name = i[0], value = i[1], inline = False)
    else:
        embed = discord.Embed(title = 'Search results for {} {}'.format(command[1], search_text), description = 'No results found!!', color = 0xffffff)
    
    await ctx.send(embed = embed)
    logger.discord_output_kcg(os.getcwd() + '\logger', 'Search results was fetched')


############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################