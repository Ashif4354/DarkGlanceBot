#DarkGlanceBot

import discord
from discord.ext import commands
from darkglance import discord_
from kcg.Student import student
from kcg.finddob import find_student_dob
from kcg.check import *

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
    functions = ('photo', 'dob', 'name')
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
        #get photo
        if command[1] == 'photo':

            try:
                photo = r"c:\Users\{}\Desktop\collected_pics\{}.png".format(os.getlogin(), user_id)
                with open(photo, 'rb') as f:
                    None

            except:                             
                await text_channel.send('Please wait while we fetch the photo')

                student.fees_login(user_id)
                
                student.get_photo(uid = user_id)
                
            await text_channel.send('Photo has been fetched')
            photo = r'c:\Users\{}\Desktop\collected_pics\{}.png'.format(os.getlogin(), user_id)
            with open(photo, 'rb') as f:
                photo = discord.File(f)
                await text_channel.send(file=photo)
                logger.discord_file_output_kcg(os.getcwd() + '\logger', '{}.png'.format(user_id))
                
                

        #get date of birth
        elif command[1] == 'dob':
            try:
                year = command[3]
            except:                
                year = '0000'

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

    except:
        None 

client.run(discord_.token)


