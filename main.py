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
    print("\nDarkGlanceBot is ready to go")

@client.command()
async def hi(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')            
    await text_channel.send('DarkGlanceBot at your service')

    
@client.command(aliases=['kcgs', 'kcg'])   
async def kcgstudent(text_channel):    
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')    
    functions = ('photo', 'dob', 'name', 'marks', 'details', 'registernumber', 'all')
    command = text_channel.message.content.split()

    try:
        if command[1] not in functions:
            await text_channel.send('Invalid request')
            return
    except:
        return

    try:
        user_id = command[2]
    except:
        await text_channel.send('No id was given')
        return    

    if check_student_id(user_id):
        pass
    else:
        await text_channel.send('Invalid RegisterNo/RollNo')
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
                await text_channel.send('You dont have authorization to use this command')
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

            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_photo.png'.format(user_id))
            await text_channel.send(embed = embed, file = pic)
            


        elif command[1] == 'dob': #get date of birth

            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                await text_channel.send('You dont have authorization to use this command')
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
                await text_channel.send('Login failed.. Please try again')            
                return
            try:
                student.get_marks(user_id)
            except:
                await text_channel.send('failed to get marks.. Please try again')  
                return

            await text_channel.send('Marks has been fetched')

           
            marks = r'c:\Users\{}\Desktop\collected_pics\{}_marks.png'.format(os.getlogin(), user_id)

            embed = discord.Embed(title = user_id, description  = 'Marks',color = 0xffffff)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')

            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_marks.png'.format(user_id))
            await text_channel.send(embed = embed, file = pic)

            os.remove(marks)

        
        elif command[1] == 'details': #get details

            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                await text_channel.send('You dont have authorization to use this command')
                return
            try:
                await text_channel.send('Please wait while we crack the date of birth') 
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB has been Found successfully')

                await text_channel.send('Please wait while we fetch the details')
                student.student_login(user_id, d_o_b)
                await text_channel.send('Login successful')

            except:
                await text_channel.send('Login failed.. Please try again')  
                return          
            
            try:
                student.get_details(user_id)
            except:
                await text_channel.send('failed to get details.. Some error occurred.. Please try again')  
                return
            
            await text_channel.send('Details has been fetched')

           
            details = r'c:\Users\{}\Desktop\collected_pics\{}_details.png'.format(os.getlogin(), user_id)
            embed = discord.Embed(title = user_id, description  = 'Details',color = 0xffffff)
            pic = discord.File(details, filename = 'temp_details.png')
            embed.set_image(url = 'attachment://temp_details.png')

            logger.discord_output_kcg(os.getcwd() + '\logger', '{}_details.png'.format(user_id))
            await text_channel.send(embed = embed, file = pic)

            os.remove(details)   


        elif command[1] == 'registernumber': #get register number
            if check_student_rollno(user_id):
                pass
            else:
                await text_channel.send('give only roll no, not register no..Try again')
                return

            await text_channel.send('Please wait while we fetch the Register number..')

            try:
                d_o_b = find_student_dob(user_id, year)
                student.student_login(user_id, d_o_b)
                regno = student.get_regno()
            except:
                await text_channel.send('Some error occured in the process.. Please try again')

            embed = discord.Embed(title = user_id, description = regno, color = 0xffffff)
            await text_channel.send(embed = embed)
            logger.discord_output_kcg(os.getcwd() + '\logger', regno)


        elif command[1] == 'all': #get all details
            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                pass
            else:
                await text_channel.send('You dont have authorization to use this command')
                return
            
            await text_channel.send('This may take a while so please be patient..')

            try:
                d_o_b = find_student_dob(user_id, year)

                student.fees_login(user_id)
                name = student.get_name(user_id)

                student.fees_login(user_id)
                student.get_photo(user_id)

                student.student_login(user_id, d_o_b)
                student.get_details(user_id)

                student.student_login(user_id, d_o_b)
                student.get_marks(user_id)
            except:
                await text_channel.send('Some error occured in the process.. Please try again')
                
            embed = discord.Embed(title = user_id, color = 0xffffff)

            photo = r'c:\Users\{}\Desktop\collected_pics\{}_photo.png'.format(os.getlogin(), user_id)
            pic = discord.File(photo, filename = 'temp_photo.png')
            embed.set_image(url = 'attachment://temp_photo.png')
            embed.add_field(name = 'Name', value = name)
            await text_channel.send(embed = embed, file = pic)

            embed = discord.Embed(title = user_id, color = 0xffffff)
            
            details = r'c:\Users\{}\Desktop\collected_pics\{}_details.png'.format(os.getlogin(), user_id)
            pic = discord.File(details, filename = 'temp_details.png')
            embed.set_image(url = 'attachment://temp_details.png')
            
            logger.discord_output_kcg(os.getcwd() + '\logger', '{0} | {1}_photo.png | {1}_details.png'.format(name, user_id))
            await text_channel.send(embed = embed, file = pic)

            embed = discord.Embed(title = user_id, color = 0xffffff)
            
            marks = r'c:\Users\{}\Desktop\collected_pics\{}_marks.png'.format(os.getlogin(), user_id)
            pic = discord.File(marks, filename = 'temp_marks.png')
            embed.set_image(url = 'attachment://temp_marks.png')
            
            logger.discord_output_kcg(os.getcwd() + '\logger', '{0} | {1}_photo.png | {1}_details.png | {1}_marks.png' .format(name, user_id))
            await text_channel.send(embed = embed, file = pic)

            os.remove(details)







    except:
        pass

@client.command()
async def authorize(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')  

    if discord_.check_authorization(text_channel, 'owner'):
        pass
    else:
        await text_channel.send('You dont have authorization to use this command')
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        await text_channel.send('No username given')
        return
    
    if user_name == 'all':
        discord_.auth_all()
        await text_channel.send('Every one has been authorized with admin role')
        return

    try:
        role = command[2]
    except:
        await text_channel.send('No role specified')
        return
    
    if role in discord_.roles:
        pass
    else:
        await text_channel.send('Invalid role')
        return

    discord_.authorize(user_name, role)
    await text_channel.send('{} has been authorized with {} role'.format(user_name, role))

@client.command()
async def revoke(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')

    if discord_.check_authorization(text_channel, 'owner'):
        pass
    else:
        await text_channel.send('You dont have authorization to use this command')
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        await text_channel.send('No username given')
        return

    if user_name == 'all':
        discord_.rev_all() 
        await text_channel.send('Every one has been revoked admin role')  
        return
    
    try:
        role = command[2]
    except:
        await text_channel.send('No role specified')
        return
    
    if role in discord_.roles:
        pass
    else:
        await text_channel.send('Invalid role')
        return

    try:
        discord_.authorize(user_name, role)
    except:
        await text_channel.send('user is alreaddy not authorized')
    
    discord_.revoke(user_name, role)
    await text_channel.send('{} has been revoked of the role {}'.format(user_name, role))


client.run(discord_.token)


