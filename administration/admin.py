#This main function just contains some common funtions for the bot

import discord
from logger.logger import logger
from os import getcwd


class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')
    
    def check_authorization(ctx, role):
        dbconnect('darkglancebot')

        mysql_cursor.execute("SELECT * FROM block_list where name = '{}'".format(ctx.message.author))
        if mysql_cursor.fetchall() == []:
            pass
        else:
            raise Blocked

        if not role in discord_.roles:
            mysql_cursor.execute('select * from auth_all')
            value = mysql_cursor.fetchone()[0]
            if value == 'True':
                dbdisconnect()
                return True
            else:
                pass

        author = str(ctx.message.author)
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, author))
        users = mysql_cursor.fetchall()
        try:
            if author in users[0]:
                dbdisconnect()
                return True
            else:
                dbdisconnect()
                return False
        except:
            return False
    
    def authorize(user_name, role):
        dbconnect('darkglancebot')
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users != []:
            raise Exception
        else:
            pass

        mysql_cursor.execute("INSERT INTO role_{} VALUES('{}')".format(role, user_name))
        dbdisconnect()
    
    def revoke(user_name, role):
        dbconnect('darkglancebot')        
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users == []:
            raise Exception
        else:
            pass
        
        mysql_cursor.execute("DELETE FROM role_{} WHERE name = '{}';".format(role, user_name))
        dbdisconnect()
    
    def auth_all():
        dbconnect('darkglancebot')
        mysql_cursor.execute("UPDATE auth_all SET value = 'True'")
        dbdisconnect()
    
    def rev_all():
        dbconnect('darkglancebot')
        mysql_cursor.execute("UPDATE auth_all SET value = 'False'")
        dbdisconnect()
        
    def block(user_name):
        dbconnect('darkglancebot')
        mysql_cursor.execute("INSERT INTO block_list VALUES('{}')".format(user_name))
        dbdisconnect()
    
    def unblock(user_name):
        dbconnect('darkglancebot')
        mysql_cursor.execute("DELETE FROM block_list WHERE name = '{}';".format(user_name))
        dbdisconnect()

async def check_auth(ctx, roles, message = 'You dont have authorization to use this command'):
    try:
        for role in roles:
            if discord_.check_authorization(ctx, role):
                return True
        else:
            embed = discord.Embed(description = ctx.message.author.mention + message, color = 0xffffff)
            await ctx.send(embed = embed)
            return False

    except Blocked:
        embed = discord.Embed(title = 'YOU ARE BLOCKED', description = 'Contact DarkGlance#6849 for queries', color = 0xffffff)
        await ctx.send(embed = embed)
        return False

async def authorize(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')  

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


async def revoke(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')

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

async def block(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')

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

async def unblock(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')

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

async def dbcheck(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger') 
    
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

async def tempcheck(ctx):
    return
    logger.input_kcg(ctx, getcwd() + '\logger')
    
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

async def stopbot(ctx):
    logger.input_kcg(ctx, getcwd() + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    exit(0)
