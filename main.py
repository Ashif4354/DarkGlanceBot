#DarkGlanceBot

import discord
from discord.ext import commands
from darkglance import *
from kcg.Student import student
from kcg.finddob import find_student_dob
from kcg.check import *
import os
from logger.logger import logger

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to go")

@client.command()
async def hi(ctx):
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')            
    embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff)
    await ctx.send(embed = embed)

@client.command()
async def dghelp(ctx) :
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')
    await ctx.send(embed = help_embed)
       
@client.command(aliases=['kcg', 'student'])   
async def kcgstudent(ctx):    
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')     

    functions = ('photo', 'dob', 'name', 'marks', 'details', 'registernumber', 'rollnumber', 'all')
    command = ctx.message.content.split()

    try:
        if command[1] not in functions:
            embed = discord.Embed(title = 'Invalid request', color = 0xffffff)
            await ctx.send(embed = embed)
            return
    except:
        return

    try:
        user_id = command[2]
    except:
        embed = discord.Embed(description = 'No ID was given', color = 0xffffff)
        await ctx.send(embed = embed)
        return    

    if check_student_id(user_id):
        pass
    else:
        embed = discord.Embed(description = 'Invalid Register / Roll number', color = 0xffffff)
        await ctx.send(embed = embed)
        return 

    try:
        year = command[3]
    except:                
        year = None      
    
    try:#1
        #=========================================================================================================================================                
        if command[1] == 'photo': #get photo
            if discord_.check_authorization(ctx, 'admin') or discord_.check_authorization(ctx, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            try:
                photo = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), user_id)
                with open(photo, 'rb') as f:
                    pass

            except:                             
                await ctx.send('Please wait while we fetch the photo')
                student.fees_login(user_id)
                try:
                    student.get_photo(uid = user_id)
                except:
                    await ctx.send('No photo available in server')
                    return
                
            await ctx.send('Photo has been fetched')
            photo = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), user_id)

            embed = discord.Embed(title = user_id, description  = 'Photo',color = 0xffffff)
            pic = discord.File(photo, filename = 'temp_photo.png')
            embed.set_image(url = 'attachment://temp_photo.png')
            
            await ctx.send(embed = embed, file = pic)
            os.remove(photo)
            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_photo.png'.format(user_id))
        
        #2
        #=========================================================================================================================================
        elif command[1] == 'dob': #get date of birth

            if discord_.check_authorization(ctx, 'admin') or discord_.check_authorization(ctx, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await ctx.send(embed = embed)
                return           

            await ctx.send('Please wait while we crack the date of birth')           
            try:
                d_o_b = find_student_dob(user_id, year)
            except:
                embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            d_o_b = d_o_b[:2] + '/' + d_o_b[2:4] + '/' + d_o_b[4:] 

            await ctx.send('DOB has been Found successfully')

            embed = discord.Embed(title = user_id, description = d_o_b, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.discord_output_kcg(os.getcwd() + '\logger', d_o_b)
        
        #3
        #=========================================================================================================================================
        elif command[1] == 'name': #get name           

            student.fees_login(user_id)
            name = student.get_name()

            embed = discord.Embed(title = user_id, description = name, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.discord_output_kcg(os.getcwd() + '\logger', name)
        
        #4
        #=========================================================================================================================================
        elif command[1] == 'marks': #get marks
            try:
                await ctx.send('Please wait while we crack the date of birth') 
                try:
                    d_o_b = find_student_dob(user_id, year)
                except:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                    
                await ctx.send('DOB has been Found successfully')

                await ctx.send('Please wait while we try to fetch the marks')
                student.student_login(user_id, d_o_b)
                await ctx.send('Login successful')

            except:
                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)           
                return
                
            try:
                student.get_marks(user_id)
            except:
                embed = discord.Embed(description = 'failed to get marks.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)  
                return

            await ctx.send('Marks has been fetched')

           
            marks = r"{}\temp_pics\{}_marks.png".format(os.getcwd(), user_id)

            embed = discord.Embed(title = user_id, description  = 'Marks',color = 0xffffff)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')

            await ctx.send(embed = embed, file = pic)

            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_marks.png'.format(user_id))            

            os.remove(marks)
        
        #5
        #=========================================================================================================================================
        elif command[1] == 'details': #get details

            if discord_.check_authorization(ctx, 'admin') or discord_.check_authorization(ctx, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await ctx.send(embed = embed)
                return
            try:
                await ctx.send('Please wait while we crack the date of birth') 
                try:
                    d_o_b = find_student_dob(user_id, year)
                except:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return

                await ctx.send('DOB has been Found successfully')

                await ctx.send('Please wait while we fetch the details')
                student.student_login(user_id, d_o_b)
                await ctx.send('Login successful')

            except:
                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)  
                return          
            
            try:
                student.get_details(user_id)
            except:
                embed = discord.Embed(description = 'failed to get details.. Some error occurred..\n Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return
            
            await ctx.send('Details has been fetched')

           
            details = r"{}\temp_pics\{}_details.png".format(os.getcwd(), user_id)
            embed = discord.Embed(title = user_id, description  = 'Details',color = 0xffffff)
            pic = discord.File(details, filename = 'temp_details.png')
            embed.set_image(url = 'attachment://temp_details.png')
            
            await ctx.send(embed = embed, file = pic)

            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_details.png'.format(user_id))

            os.remove(details)   

        #6
        #=========================================================================================================================================
        elif command[1] == 'registernumber': #get register number
            if check_student_rollno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Roll no..Try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            await ctx.send('Please wait while we fetch the Register number..')

            try:
                try:
                    d_o_b = find_student_dob(user_id, year)
                except:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return

                student.student_login(user_id, d_o_b)
                regno = student.get_regno()
            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = regno, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.discord_output_kcg(os.getcwd() + '\logger', regno)
        
        #7
        #=========================================================================================================================================
        elif command[1] == 'rollnumber': #get roll number
            if check_student_registerno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Register no..Try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            await ctx.send('Please wait while we fetch the Roll number..')

            try:
                try:
                    d_o_b = find_student_dob(user_id, year)
                except:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return

                student.student_login(user_id, d_o_b)
                rollno = student.get_rollno(user_id)
            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = rollno, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.discord_output_kcg(os.getcwd() + '\logger', rollno)

        #8
        #=========================================================================================================================================
        elif command[1] == 'all': #get all details
            if discord_.check_authorization(ctx, 'admin') or discord_.check_authorization(ctx, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await ctx.send(embed = embed)
                return
            
            await ctx.send('This may take a while so please be patient..')

            try:
                await ctx.send('DOB is being cracked')

                try:
                    d_o_b = find_student_dob(user_id, year)
                except:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                
                await ctx.send('DOB found')          

                student.fees_login(user_id)
                try:
                    student.get_photo(user_id)
                    got_photo = True
                    await ctx.send('Photo fetched')
                except:
                    got_photo = False
                    await ctx.send('Photo not available')
                

                student.student_login(user_id, d_o_b)
                student.get_details(user_id)
                await ctx.send('Details fetched')

                student.student_login(user_id, d_o_b)
                student.get_marks(user_id)
                await ctx.send('Marks fetched')

            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            if got_photo:
                embed = discord.Embed(title = user_id, color = 0xffffff)
                photo = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), user_id)
                pic = discord.File(photo, filename = 'temp_photo.png')
                embed.set_image(url = 'attachment://temp_photo.png')
                await ctx.send(embed = embed, file = pic)
            
            embed = discord.Embed(title = user_id, color = 0xffffff)            
            details = r"{}\temp_pics\{}_details.png".format(os.getcwd(), user_id)          
            pic = discord.File(details, filename = 'temp_details.png')            
            embed.set_image(url = 'attachment://temp_details.png')
            await ctx.send(embed = embed, file = pic)

            embed = discord.Embed(title = user_id, color = 0xffffff)            
            marks = r"{}\temp_pics\{}_marks.png".format(os.getcwd(), user_id)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')            
            await ctx.send(embed = embed, file = pic)

            logger.discord_output_kcg(os.getcwd() + '\logger', '{0}_photo.png | {0}_details.png | {0}_marks.png'.format(user_id))

            os.remove(photo)
            os.remove(details)
            os.remove(marks)
        
        #=========================================================================================================================================
        
    except:
        pass



@client.command(aliases=['kcgs', 'search'])
async def kcgsearch(ctx): # .kcgs 2020 ashif cs
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger') 

    if discord_.check_authorization(ctx, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await ctx.send(embed = embed)
        return
        
    command = ctx.message.content.split()

    try:
        if len(command[1]) == 4:
            batch = str(int(command[1]) % 100)

    except:
        embed = discord.Embed(description = 'Invalid Year', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    try:
        user_id = command[2]
    except:
        embed = discord.Embed(description = 'No id was given', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    depts = command[3:]


    student.search(batch, user_id, depts)
    
        
    

    
    













@client.command()
async def authorize(ctx):
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')  

    if discord_.check_authorization(ctx, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await ctx.send(embed = embed)
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
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')

    if discord_.check_authorization(ctx, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await ctx.send(embed = embed)
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
    except:
        embed = discord.Embed(description = 'user is already authorized', color = 0xffffff)
        await ctx.send(embed = embed)
        return 

    embed = discord.Embed(title = user_name,description = 'revoked of the role {}'.format(role), color = 0xffffff)
    await ctx.send(embed = embed)


@client.command()
async def dbcheck(ctx):
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger') 
    
    if discord_.check_authorization(ctx, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await ctx.send(embed = embed)
        return

    if not mycon.is_connected():
        embed = discord.Embed(description = 'database not connected', color = 0xffffff)
        await ctx.send(embed = embed) 
    else:  
        embed = discord.Embed(description = 'database connection Alive', color = 0xffffff)
        await ctx.send(embed = embed) 
    
    try:
        mysql_cursor.execute('select * from auth_all')
        embed = discord.Embed(description = 'Fetching Not active', color = 0xffffff)
        await ctx.send(embed = embed)
    except:
        embed = discord.Embed(description = 'Fetching Not active', color = 0xffffff)
        await ctx.send(embed = embed) 


@client.command()
async def tempcheck(ctx):
    logger.discord_input_kcg(ctx, os.getcwd() + '\logger')

    mysql_cursor.execute('select * from auth_all')
    mysql_cursor.fetchall()
    



    
        


client.run(discord_.token)


