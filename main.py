#This main function just contains some common funtions for the bot

import discord
from discord.ext import commands
from logger.logger import logger
from darkglance import *
from game_invite import games
from os import getcwd

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to go")

@client.command()
async def hi(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger')            
    embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff)
    await ctx.send(embed = embed)


@client.command()
async def gameinvite(ctx):

    command = ctx.message.content.split()

    try:
        game_name = command[1]
        
        for game in games.games:
            if game_name in games.games[game]:
                game_name = game
                break
        else:
            raise GameNotAvailable
            
    except IndexError:
        embed = discord.Embed(description = 'No game mentioned', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    except GameNotAvailable:
        embed = discord.Embed(description = 'This game invite not available yet', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    
    await games.send_invite(ctx, game_name, path = getcwd() + '\game_invite')


@client.command()
async def authorize(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger')  

    if not await check_auth(ctx, ('owner',)):
        return

    command = ctx.message.content.split()

    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    if user_name == 'all':
        discord_.auth_all()
        embed = discord.Embed(description = 'Every one has been authorized with admin role', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        role = command[2]
    except:
        embed = discord.Embed(description = 'No role specified', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    if role in discord_.roles:
        pass
    else:
        embed = discord.Embed(description = 'Invalid role', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        discord_.authorize(user_name, role)
    except:
        embed = discord.Embed(description = 'User already authorized', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    embed = discord.Embed(title = user_name, description = 'authorized with {} role'.format(role), color = 0xffffff)
    await ctx.send(embed = embed)

@client.command()
async def revoke(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    command = ctx.message.content.split()

    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    if user_name == 'all':
        discord_.rev_all() 
        embed = discord.Embed(description = 'Every one has been revoked of admin role', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    try:
        role = command[2]
    except:
        embed = discord.Embed(description = 'No role specified', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    if role in discord_.roles:
        pass
    else:
        embed = discord.Embed(description = 'Invalid role', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        discord_.revoke(user_name, role)
        embed = discord.Embed(title = user_name,description = 'revoked of the role {}'.format(role), color = 0xffffff)
    except:
        embed = discord.Embed(description = 'user is already authorized', color = 0xffffff)
        await ctx.send(embed = embed)
        return 

    
    await ctx.send(embed = embed)

@client.command()
async def block(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    command = ctx.message.content.split()
    
    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    try:
        discord_.block(user_name)
        embed = discord.Embed(title = user_name,description = 'has been blocked', color = 0xffffff)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(description = 'User is already blocked', color = 0xffffff)
        await ctx.send(embed = embed)
        return

@client.command()
async def unblock(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    command = ctx.message.content.split()
    
    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await ctx.send(embed = embed)
        return
    
    try:
        discord_.unblock(user_name)
        embed = discord.Embed(title = user_name,description = 'has been unblocked', color = 0xffffff)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(description = 'User is not blocked', color = 0xffffff)
        await ctx.send(embed = embed)
        return


@client.command()
async def dbcheck(ctx):
    logger.discord_input_kcg(ctx, getcwd() + '\logger') 
    
    if not await check_auth(ctx, ('owner',)):
        return

    if not mycon.is_connected():
        embed = discord.Embed(description = 'database not connected', color = 0xffffff)
        await ctx.send(embed = embed) 
    else:  
        embed = discord.Embed(description = 'database connection Alive', color = 0xffffff)
        await ctx.send(embed = embed) 
    
    try:
        mysql_cursor.execute('select * from auth_all')
        embed = discord.Embed(description = 'Fetching active', color = 0xffffff)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(description = 'Fetching Not active', color = 0xffffff)
        await ctx.send(embed = embed) 


@client.command()
async def tempcheck(ctx):
    return
    logger.discord_input_kcg(ctx, getcwd() + '\logger')
    
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('Checking select')
    mysql_cursor.execute('select * from auth_all')
    mysql_cursor.fetchall()
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')
    print('Checking insert')
    mysql_cursor.execute("insert into block_list values('qwerty')")
    mysql_cursor.fetchall()
    print('=========================================================================================================================================')
    print('=========================================================================================================================================')

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