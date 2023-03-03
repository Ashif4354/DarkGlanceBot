#DarkGlanceBot

import discord
from discord.ext import commands
from Student import student, server_down, NoPhoto
from finddob import find_student_dob
from check import *
from datetime import date, datetime
from os import getcwd, remove
import help_embed

from sys import path
path.append(getcwd().rstrip('kcg'))
from logger.logger import logger
from darkglance import *

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("\nServer has been started")
    print("DarkGlanceBot is ready to perform kcg tasks")

@client.command()
async def kcghelp(ctx) :
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')
    await ctx.send(embed = help_embed.help_embed)

@client.command(aliases = ['cks'])
async def checkkcgserver(ctx):    
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')

    if not await check_auth(ctx, ('owner', 'admin')):
        return
    #print('wait')
    
    await ctx.send(embed = check_server()[0])
       
@client.command(aliases = ['kcg', 'student'])   
async def kcgstudent(ctx):    
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')     

    if str(ctx.message.author) != 'DarkGlance#6849':
        sorry_embed = discord.Embed(title = 'Sorry for Inconvenience', description = 'KCG tasks are currently under maintenance', color = 0xffffff)
        await ctx.send(embed = sorry_embed)
        return
    else:
        pass

    functions = ('photo', 'dob', 'name', 'marks', 'details', 'all',
                 'registernumber', 'reg', 'rollnumber', 'roll',
                 'namephoto', 'np')

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

    except IndexError :
        embed = discord.Embed(description = 'No ID was given', color = 0xffffff)
        await ctx.send(embed = embed)
        return    

    try:
        if check_student_id(user_id):
            pass
        else:
            if not check_server()[1]:
                raise server_down
                
            embed = discord.Embed(description = 'Invalid Register / Roll number', color = 0xffffff)
            await ctx.send(embed = embed)
            return

    except server_down:
        await ctx.send(embed = server_error_embed)
        return 

    except Exception as text:
        logger.exception_logs('dgb/kcg/kcg_main/kcgstudent ', text, getcwd().rstrip('kcg') + 'logger')

    try:
        year = command[3]
    except IndexError:                
        year = None      
    
    try:#1
        #=========================================================================================================================================                
        if command[1] == 'photo': #get photo
            
            if not await check_auth(ctx, ('owner', 'admin', 'all')):
                return                    
                
            student.get_photo(user_id)
                
            photo = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), user_id)

            embed = discord.Embed(title = user_id,color = 0xffffff)
            try:
                pic = discord.File(photo, filename = 'temp_photo.png')
                embed.set_image(url = 'attachment://temp_photo.png')            
            
                await ctx.send(embed = embed, file = pic)
                remove(photo)
                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '{}_photo.png'.format(user_id))

            except NoPhoto:
                embed.set_footer(text = "Photo not found")
                await ctx.send(embed = embed)
                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', 'Photo not found')
                
            except FileNotFoundError as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (photo)', text, getcwd().rstrip('kcg') + 'logger')
                embed.set_footer(text = "Photo not found")
                await ctx.send(embed = embed)

                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', 'Photo not found')
        
        #2
        #=========================================================================================================================================
        elif command[1] == 'dob': #get date of birth

            if not await check_auth(ctx, ('owner', 'admin', 'all')):
                return           
          
            try:
                d_o_b = await find_student_dob(user_id, year)
            except DobNotFound:
                embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                await ctx.send(embed = embed)
                return
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (dob)',text, getcwd().rstrip('kcg') + 'logger')
                return
            

            d_o_b = d_o_b[:2] + '/' + d_o_b[2:4] + '/' + d_o_b[4:] 

            embed = discord.Embed(title = user_id, description = d_o_b, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', d_o_b)
        
        #3
        #=========================================================================================================================================
        elif command[1] == 'name': #get name           

            #student.fees_login(user_id)
            name = student.get_name(user_id)

            embed = discord.Embed(title = user_id, description = name, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', name)
        
        #4
        #=========================================================================================================================================
        elif command[1] == 'marks': #get marks
            try:
                try:
                    d_o_b = await find_student_dob(user_id, year)
                except DobNotFound:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (marks1)', text, getcwd().rstrip('kcg') + 'logger')
                    return
                    
                await ctx.send('DOB has been Found successfully')

                await ctx.send('Please wait while we try to fetch the marks')
                student.student_login(user_id, d_o_b)
                await ctx.send('Login successful')

            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (marks2)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)           
                return
                
            try:
                student.get_marks(user_id)
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (marks3)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'failed to get marks.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)  
                return

            await ctx.send('Marks has been fetched')

           
            marks = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('kcg'), user_id)

            embed = discord.Embed(title = user_id, description  = 'Marks',color = 0xffffff)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')

            await ctx.send(embed = embed, file = pic)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '{}_marks.png'.format(user_id))            

            remove(marks)
        
        #5
        #=========================================================================================================================================
        elif command[1] == 'details': #get details

            if not await check_auth(ctx, ('owner', 'admin', 'all')):
                return

            try:
                try:
                    d_o_b = await find_student_dob(user_id, year)
                except DobNotFound:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (details1)', text, getcwd().rstrip('kcg') + 'logger')
                    return

                await ctx.send('DOB has been Found successfully')

                await ctx.send('Please wait while we fetch the details')
                student.student_login(user_id, d_o_b)
                await ctx.send('Login successful')

            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (details2)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)  
                return          
            
            try:
                student.get_details(user_id)
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (details3)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'failed to get details.. Some error occurred..\n Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return
            
            await ctx.send('Details has been fetched')

           
            details = r"{}\temp_pics\{}_details.png".format(getcwd().rstrip('kcg'), user_id)
            embed = discord.Embed(title = user_id, description  = 'Details',color = 0xffffff)
            pic = discord.File(details, filename = 'temp_details.png')
            embed.set_image(url = 'attachment://temp_details.png')
            
            await ctx.send(embed = embed, file = pic)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '{}_details.png'.format(user_id))

            remove(details)   

        #6
        #=========================================================================================================================================
        elif command[1] in ('registernumber', 'reg'): #get register number
            if check_student_rollno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Roll no..Try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            try:
                try:
                    d_o_b = await find_student_dob(user_id, year)
                
                except DobNotFound:                    
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (reg1)', text, getcwd().rstrip('kcg') + 'logger')
                    return

                regno = student.get_regno(user_id, d_o_b)
                
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstdent (reg2)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = regno, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', regno)
        
        #7
        #=========================================================================================================================================
        elif command[1] in ('rollnumber', 'roll'): #get roll number
            if check_student_registerno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Register no..Try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            try:
                try:
                    d_o_b = await find_student_dob(user_id, year)
                except DobNotFound:                
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (roll1)', text, getcwd().rstrip('kcg') + 'logger')
                    return

                student.student_login(user_id, d_o_b)
                rollno = student.get_rollno(user_id)
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (roll2)', text, getcwd().rstrip('kcg') + 'logger')
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = rollno, color = 0xffffff)
            await ctx.send(embed = embed)

            logger.output_kcg(getcwd().rstrip('kcg') + '\logger', rollno)

        #8
        #=========================================================================================================================================
        elif command[1] == 'all': #get all details

            if not await check_auth(ctx, ('owner', 'admin', 'all')):
                return
            
            await ctx.send('This may take a while so please be patient..')

            try:

                try:
                    d_o_b = await find_student_dob(user_id, year)
                except DobNotFound:
                    embed = discord.Embed(description = 'Unable to find DOB.. Please try again\nTry specifying year of birth', color = 0xffffff)
                    await ctx.send(embed = embed)
                    return
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (all1)', text, getcwd().rstrip('kcg') + 'logger')
                    return
                
                await ctx.send('DOB found')          

                try:
                    student.get_photo(user_id)
                    got_photo = True
                    await ctx.send('Photo fetched')
                except Exception as text:
                    logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (all2)(ignorable)', text, getcwd().rstrip('kcg') + 'logger')
                    got_photo = False
                    await ctx.send('Photo not available')                

                student.student_login(user_id, d_o_b)
                student.get_details(user_id)
                await ctx.send('Details fetched')

                student.student_login(user_id, d_o_b)
                student.get_marks(user_id)
                await ctx.send('Marks fetched')

            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (all3)', text, getcwd().rstrip('kcg') + 'logger')

                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await ctx.send(embed = embed)
                return

            if got_photo:
                embed = discord.Embed(title = user_id, color = 0xffffff)
                photo = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), user_id)
                pic = discord.File(photo, filename = 'temp_photo.png')
                embed.set_image(url = 'attachment://temp_photo.png')
                await ctx.send(embed = embed, file = pic)
            
            embed = discord.Embed(title = user_id, color = 0xffffff)            
            details = r"{}\temp_pics\{}_details.png".format(getcwd().rstrip('kcg'), user_id)          
            pic = discord.File(details, filename = 'temp_details.png')            
            embed.set_image(url = 'attachment://temp_details.png')
            await ctx.send(embed = embed, file = pic)

            embed = discord.Embed(title = user_id, color = 0xffffff)            
            marks = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('kcg'), user_id)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')            
            await ctx.send(embed = embed, file = pic)
            
            if got_photo:
                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '{0}_photo.png | {0}_details.png | {0}_marks.png'.format(user_id))
            else:
                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '<no photo> | {0}_details.png | {0}_marks.png'.format(user_id))

            remove(photo)
            remove(details)
            remove(marks)
        
        #9
        #=========================================================================================================================================
        elif command[1] in ('namephoto', 'np'): #get all details

            if not await check_auth(ctx, ('owner', 'admin', 'all')):
                return

            student_ = student.get_np(user_id)
            name = student_[0]

            photo = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), user_id)
            
            embed = discord.Embed(title = user_id, description = name, color = 0xffffff)
            try:
                pic = discord.File(photo, filename = 'temp_photo.png')
                embed.set_image(url = 'attachment://temp_photo.png')            
            
                await ctx.send(embed = embed, file = pic)
                remove(photo)
                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', '{}_photo.png'.format(user_id))
            except Exception as text:
                logger.exception_logs('dgb/kcg/kcg_main/kcgstudent (np)', text, getcwd().rstrip('kcg') + 'logger')

                embed.set_footer(text = "Photo not found")
                await ctx.send(embed = embed)

                logger.output_kcg(getcwd().rstrip('kcg') + '\logger', 'Photo not found')
        
    except Exception as text:
        logger.exception_logs('dgb/kcg/kcg_main/kcgstudent overall', text, getcwd().rstrip('kcg') + 'logger')


@client.command()
async def adddob(ctx):
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')

    if not await check_auth(ctx, ('owner','admin')):
        return

    try:
        command = ctx.message.content.split()

        user_id = command[1]
        dob_ = command[2]

        mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root", database = 'kcg', autocommit = True)
        mysql_cursor = mycon.cursor()

        try:
            mysql_cursor.execute(f"INSERT INTO dobs VALUES('{user_id}', '{dob_}')")
        except:
            mysql_cursor.execute(f"UPDATE dobs SET dob = '{dob_}' WHERE id = '{user_id}'")
        mysql_cursor.close()
        mycon.close()

    except Exception as text:
        logger.exception_logs('dgb/kcg/kcg_main/adddob', text, getcwd().rstrip('kcg') + 'logger')
        
        embed = discord.Embed(title = 'ERROR', description = text, color = 0xffffff)
        await ctx.send(embed = embed)    

@client.command()
async def stopbot(ctx):
    logger.input_kcg(ctx, getcwd().rstrip('kcg') + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    exit(0)


############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################

