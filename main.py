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
    print("\nDarkGlanceBot is ready to go")

@client.command()
async def hi(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')            
    embed = discord.Embed(description = 'DarkGlanceBot at your service', color = 0xffffff)
    await text_channel.send(embed = embed)

@client.command()
async def dghelp(text_channel) :
    await text_channel.send(embed = help_embed)
       
@client.command(aliases=['kcgs', 'kcg'])   
async def kcgstudent(text_channel):    
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')    
    functions = ('photo', 'dob', 'name', 'marks', 'details', 'registernumber', 'rollnumber', 'all')
    command = text_channel.message.content.split()

    try:
        if command[1] not in functions:
            embed = discord.Embed(title = 'Invalid request', color = 0xffffff)
            await text_channel.send(embed = embed)
            return
    except:
        return

    try:
        user_id = command[2]
    except:
        embed = discord.Embed(description = 'No ID was given', color = 0xffffff)
        await text_channel.send(embed = embed)
        return    

    if check_student_id(user_id):
        pass
    else:
        embed = discord.Embed(description = 'Invalid Register / Roll number', color = 0xffffff)
        await text_channel.send(embed = embed)
        return 

    try:
        year = command[3]
    except:                
        year = None      

    try:                
        if command[1] == 'photo': #get photo
            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            try:
                photo = r"c:\Users\{}\Desktop\collected_pics\{}_photo.png".format(os.getlogin(), user_id)
                with open(photo, 'rb') as f:
                    pass

            except:                             
                await text_channel.send('Please wait while we fetch the photo')

                student.fees_login(user_id)
                try:
                    student.get_photo(uid = user_id)
                except:
                    await text_channel.send('No photo available in server')
                    return
                
            await text_channel.send('Photo has been fetched')
            photo = r'c:\Users\{}\Desktop\collected_pics\{}_photo.png'.format(os.getlogin(), user_id)

            embed = discord.Embed(title = user_id, description  = 'Photo',color = 0xffffff)
            pic = discord.File(photo, filename = 'temp_photo.png')
            embed.set_image(url = 'attachment://temp_photo.png')
            
            await text_channel.send(embed = embed, file = pic)
            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_photo.png'.format(user_id))


        elif command[1] == 'dob': #get date of birth

            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await text_channel.send(embed = embed)
                return           

            await text_channel.send('Please wait while we crack the date of birth')           
            d_o_b = find_student_dob(user_id, year)  
            d_o_b = d_o_b[:2] + '/' + d_o_b[2:4] + '/' + d_o_b[4:] 
            await text_channel.send('DOB has been Found successfully')
            embed = discord.Embed(title = user_id, description = d_o_b, color = 0xffffff)
            await text_channel.send(embed = embed)
            logger.discord_output_kcg(os.getcwd() + '\logger', d_o_b)

        
        elif command[1] == 'name': #get name           

            student.fees_login(user_id)
            name = student.get_name()
            embed = discord.Embed(title = user_id, description = name, color = 0xffffff)
            await text_channel.send(embed = embed)
            logger.discord_output_kcg(os.getcwd() + '\logger', name)  

        
        elif command[1] == 'marks': #get marks
            try:
                await text_channel.send('Please wait while we crack the date of birth') 
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB has been Found successfully')

                await text_channel.send('Please wait while we try to fetch the marks')
                student.student_login(user_id, d_o_b)
                await text_channel.send('Login successful')

            except:
                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)           
                return
                
            try:
                student.get_marks(user_id)
            except:
                embed = discord.Embed(description = 'failed to get marks.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)  
                return

            await text_channel.send('Marks has been fetched')

           
            marks = r'c:\Users\{}\Desktop\collected_pics\{}_marks.png'.format(os.getlogin(), user_id)

            embed = discord.Embed(title = user_id, description  = 'Marks',color = 0xffffff)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')

            await text_channel.send(embed = embed, file = pic)
            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_marks.png'.format(user_id))
            

            os.remove(marks)

        
        elif command[1] == 'details': #get details

            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await text_channel.send(embed = embed)
                return
            try:
                await text_channel.send('Please wait while we crack the date of birth') 
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB has been Found successfully')

                await text_channel.send('Please wait while we fetch the details')
                student.student_login(user_id, d_o_b)
                await text_channel.send('Login successful')

            except:
                embed = discord.Embed(description = 'Login failed.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)  
                return          
            
            try:
                student.get_details(user_id)
            except:
                embed = discord.Embed(description = 'failed to get details.. Some error occurred..\n Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return
            
            await text_channel.send('Details has been fetched')

           
            details = r'c:\Users\{}\Desktop\collected_pics\{}_details.png'.format(os.getlogin(), user_id)
            embed = discord.Embed(title = user_id, description  = 'Details',color = 0xffffff)
            pic = discord.File(details, filename = 'temp_details.png')
            embed.set_image(url = 'attachment://temp_details.png')
            
            await text_channel.send(embed = embed, file = pic)
            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_details.png'.format(user_id))

            os.remove(details)   


        elif command[1] == 'registernumber': #get register number
            if check_student_rollno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Roll no..Try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            await text_channel.send('Please wait while we fetch the Register number..')

            try:
                d_o_b = find_student_dob(user_id, year)
                student.student_login(user_id, d_o_b)
                regno = student.get_regno()
            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = regno, color = 0xffffff)
            await text_channel.send(embed = embed)
            logger.discord_output_kcg(os.getcwd() + '\logger', regno)
        
        elif command[1] == 'rollnumber': #get roll number
            if check_student_registerno(user_id):
                pass
            else:
                embed = discord.Embed(description = 'Please give valid Register no..Try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            await text_channel.send('Please wait while we fetch the Roll number..')

            try:
                d_o_b = find_student_dob(user_id, year)
                student.student_login(user_id, d_o_b)
                rollno = student.get_rollno(user_id)
            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            embed = discord.Embed(title = user_id, description = rollno, color = 0xffffff)
            await text_channel.send(embed = embed)
            logger.discord_output_kcg(os.getcwd() + '\logger', rollno)


        elif command[1] == 'all': #get all details
            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
                await text_channel.send(embed = embed)
                return
            
            await text_channel.send('This may take a while so please be patient..')

            try:
                await text_channel.send('DOB is being cracked')
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB found')          

                student.fees_login(user_id)
                try:
                    student.get_photo(user_id)
                    got_photo = True
                    await text_channel.send('Photo fetched')
                except:
                    got_photo = False
                    await text_channel.send('Photo not available')
                

                student.student_login(user_id, d_o_b)
                student.get_details(user_id)
                await text_channel.send('Details fetched')

                student.student_login(user_id, d_o_b)
                student.get_marks(user_id)
                await text_channel.send('Marks fetched')

            except:
                embed = discord.Embed(description = 'Some error occured in the process.. Please try again', color = 0xffffff)
                await text_channel.send(embed = embed)
                return

            if got_photo:
                embed = discord.Embed(title = user_id, color = 0xffffff)
                photo = r'c:\Users\{}\Desktop\collected_pics\{}_photo.png'.format(os.getlogin(), user_id)
                pic = discord.File(photo, filename = 'temp_photo.png')
                embed.set_image(url = 'attachment://temp_photo.png')
                await text_channel.send(embed = embed, file = pic)
            
            embed = discord.Embed(title = user_id, color = 0xffffff)            
            details = r'c:\Users\{}\Desktop\collected_pics\{}_details.png'.format(os.getlogin(), user_id)            
            pic = discord.File(details, filename = 'temp_details.png')            
            embed.set_image(url = 'attachment://temp_details.png')
            await text_channel.send(embed = embed, file = pic)

            embed = discord.Embed(title = user_id, color = 0xffffff)            
            marks = r'c:\Users\{}\Desktop\collected_pics\{}_marks.png'.format(os.getlogin(), user_id)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')            
            await text_channel.send(embed = embed, file = pic)

            logger.discord_output_kcg(os.getcwd() + '\logger', '{0}_photo.png | {0}_details.png | {0}_marks.png'.format(user_id))

            os.remove(details)
            os.remove(marks)

    except:
        pass

@client.command()
async def authorize(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')  

    if discord_.check_authorization(text_channel, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await text_channel.send(embed = embed)
        return
    
    if user_name == 'all':
        discord_.auth_all()
        embed = discord.Embed(description = 'Every one has been authorized with admin role', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    try:
        role = command[2]
    except:
        embed = discord.Embed(description = 'No role specified', color = 0xffffff)
        await text_channel.send(embed = embed)
        return
    
    if role in discord_.roles:
        pass
    else:
        embed = discord.Embed(description = 'Invalid role', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    try:
        discord_.authorize(user_name, role)
    except:
        embed = discord.Embed(description = 'User already authorized', color = 0xffffff)
        await text_channel.send(embed = embed)
        return
    
    embed = discord.Embed(title = user_name, description = 'authorized with {} role'.format(role), color = 0xffffff)
    await text_channel.send(embed = embed)

@client.command()
async def revoke(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')

    if discord_.check_authorization(text_channel, 'owner'):
        pass
    else:
        embed = discord.Embed(description = 'You dont have authorization to use this command', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        embed = discord.Embed(description = 'No username given', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    if user_name == 'all':
        discord_.rev_all() 
        embed = discord.Embed(description = 'Every one has been revoked of admin role', color = 0xffffff)
        await text_channel.send(embed = embed)
        return
    
    try:
        role = command[2]
    except:
        embed = discord.Embed(description = 'No role specified', color = 0xffffff)
        await text_channel.send(embed = embed)
        return
    
    if role in discord_.roles:
        pass
    else:
        embed = discord.Embed(description = 'Invalid role', color = 0xffffff)
        await text_channel.send(embed = embed)
        return

    try:
        discord_.revoke(user_name, role)
    except:
        embed = discord.Embed(description = 'user is already authorized', color = 0xffffff)
        await text_channel.send(embed = embed)
        return 

    embed = discord.Embed(title = user_name,description = 'revoked of the role {}'.format(role), color = 0xffffff)
    await text_channel.send(embed = embed)


client.run(discord_.token)


