import discord
from discord.ext import commands
from darkglance import *
from kcg.Student import student, server_down
from logger.logger import logger
import os
from datetime import date

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to Search")

@client.command(aliases = ['kcgs', 'search'])
async def kcgsearch(ctx): # .kcgs 2020 ashif cs it
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')     

    if not await check_auth(ctx, ('owner', 'admin')):
        return
        
    command = ctx.message.content.split()
    #print(command)
    
    try:
        if len(command[1]) == 4 and int(command[1]) in range(2012, date.today().year + 1):
            batch = str(int(command[1]) % 100)
        else:
            raise Exception
    except:
        embed = discord.Embed(title = 'Invalid Year / Invalid Input', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        search_text = command[2].upper()
    except:
        embed = discord.Embed(description = 'No search keyword was given', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    depts = command[3:]
    
    try:
        if depts[0].lower() in ('all', '*'): 
            depts = ['all']
            if not await check_auth(ctx, ('owner',), 'You are not authorized to search all departments'):
                return
    except IndexError:
        pass
    
    depts_ = str(depts).strip("[]").replace("'", ' ')
    embed = discord.Embed(title = 'Search started..', description =  f'Batch : {command[1]}\nKeyword : {search_text}\nDepartments : {depts_}', color = 0xffffff)
    await ctx.send(embed = embed)

    try:
        students = student.search(ctx, batch, search_text, depts, log_path = f'{os.getcwd()}\logger\searchlogs\\')
    except server_down:
        await ctx.send(embed = server_error_embed)
        return

    #print(students)
    

    if not students == []:
        if len(students) <= 25:
            embed = discord.Embed(title = 'Search results for {} {}'.format(command[1], search_text), color = 0xffffff)
            for i in students:
                embed.add_field(name = i[0], value = i[1], inline = False)
            await ctx.send(embed = embed)
                
        else:
            count = 0 
            page = 1  
            embeds = {} 
            
            for i in students:
                if count == 0:
                    embeds[f'Page{page}'] = discord.Embed(title = 'Search results for {} {}'.format(command[1], search_text), description = f'(Page {page})', color = 0xffffff)

                embeds[f'Page{page}'].add_field(name = i[0], value = i[1], inline = False)

                if count == 24:
                    page += 1
                    count = 0
            
                else:
                    count += 1

            for embed in embeds:
                await ctx.send(embed = embeds[embed])
            
    else:
        embed = discord.Embed(title = 'Search results for {} {}'.format(command[1], search_text), description = 'No results found!!', color = 0xffffff)
        await ctx.send(embed = embed)
    
    logger.discord_output_kcg(os.getcwd() + '\logger', 'Search results was fetched')


############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################