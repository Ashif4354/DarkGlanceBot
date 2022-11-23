#DarkGlanceBot

import discord
from discord.ext import commands
from darkglance import *
from kcg.Student import student
from kcg.finddob import find_student_dob
from kcg.check import *
import os

import os #to get current working directory and user name
from logger.logger import logger

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("DarkGlanceBot is ready to go")

@client.command()
async def hi(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')            
    await text_channel.send('DarkGlanceBot at your service')
    
@client.command()   
async def kcgstudent(text_channel):    
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')    
    functions = ('photo', 'dob', 'name', 'marks', 'details')
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
        None
    else:
        await text_channel.send('Invalid RegisterNo/RollNo')
        return 

    try:
        year = command[3]
    except:                
        year = None      

    try:        
        #get photo
        if command[1] == 'photo':
            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                None
            else:
                await text_channel.send('You dont have authorization to use this command')
                return

            try:
                photo = r"c:\Users\{}\Desktop\collected_pics\{}.png".format(os.getlogin(), user_id)
                with open(photo, 'rb') as f:
                    None

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
            with open(photo, 'rb') as f:
                photo = discord.File(f)
                await text_channel.send(file=photo)
                logger.discord_output_kcg(os.getcwd() + '\logger', '{}.png'.format(user_id))
                
                

        #get date of birth
        elif command[1] == 'dob': 
            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                None
            else:
                await text_channel.send('You dont have authorization to use this command')
                return           

            await text_channel.send('Please wait while we crack the date of birth')           
            d_o_b = find_student_dob(user_id, year)  
            d_o_b = d_o_b[:2] + '/' + d_o_b[2:4] + '/' + d_o_b[4:] 
            await text_channel.send('DOB has been Found successfully')
            await text_channel.send(d_o_b)
            logger.discord_output_kcg(os.getcwd() + '\logger', d_o_b)

        #get name
        elif command[1] == 'name':            

            student.fees_login(user_id)
            name = student.get_name()
            await text_channel.send(name)
            logger.discord_output_kcg(os.getcwd() + '\logger', name)
        
        #get marks
        elif command[1] == 'marks':
            try:
                await text_channel.send('Please wait while we crack the date of birth') 
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB has been Found successfully')
                student.student_login(user_id, d_o_b)
            except:
                await text_channel.send('Login failed.. Please try again')
            
            await text_channel.send('Please wait while we fetch the marks')
            try:
                student.get_marks(user_id)
            except:
                await text_channel.send('failed to get marks.. Please try again')  
            
            await text_channel.send('Marks has been fetched')

           
            marks = r'c:\Users\{}\Desktop\collected_pics\{}_marks.png'.format(os.getlogin(), user_id)
            with open(marks, 'rb') as f:
                photo = discord.File(f)
                await text_channel.send(file=photo)
                logger.discord_output_kcg(os.getcwd() + '\logger', '{}_marks.png'.format(user_id))
            os.remove(marks)
        
        elif command[1] == 'details':

            if discord_.check_authorization(text_channel, 'admin') or discord_.check_authorization(text_channel, 'owner'):
                None
            else:
                await text_channel.send('You dont have authorization to use this command')
                return
            try:
                await text_channel.send('Please wait while we crack the date of birth') 
                d_o_b = find_student_dob(user_id, year)
                await text_channel.send('DOB has been Found successfully')
                student.student_login(user_id, d_o_b)
            except:
                await text_channel.send('Login failed.. Please try again')
            
            await text_channel.send('Please wait while we fetch the details')
            try:
                student.get_details(user_id)
            except:
                await text_channel.send('failed to get details.. Some error occurred.. Please try again')  
            
            await text_channel.send('Details has been fetched')

           
            details = r'c:\Users\{}\Desktop\collected_pics\{}_details.png'.format(os.getlogin(), user_id)
            with open(details, 'rb') as f:
                photo = discord.File(f)
                await text_channel.send(file=photo)
                logger.discord_output_kcg(os.getcwd() + '\logger', '{}_detaills.png'.format(user_id))
            os.remove(details)
                              

    except:
        None 

@client.command()
async def authorize(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')

    if discord_.check_authorization(text_channel, 'owner'):
        None
    else:
        await text_channel.send('You dont have authorization to use this command')
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        await text_channel.send('No username given')
        return
    
    try:
        role = command[2]
    except:
        await text_channel.send('No role specified')
        return
    
    if role in discord_.roles:
        None
    else:
        await text_channel.send('Invalid role')
        return

    discord_.authorize(user_name, role)
    await text_channel.send('{} has been authorized with {} role'.format(user_name, role))

@client.command()
async def revoke(text_channel):
    logger.discord_input_kcg(text_channel, os.getcwd() + '\logger')

    if discord_.check_authorization(text_channel, 'owner'):
        None
    else:
        await text_channel.send('You dont have authorization to use this command')
        return

    command = text_channel.message.content.split()

    try:
        user_name = command[1]
    except:
        await text_channel.send('No username given')
        return
    
    try:
        role = command[2]
    except:
        await text_channel.send('No role specified')
        return
    
    if role in discord_.roles:
        None
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


