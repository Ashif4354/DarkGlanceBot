#DarkGlanceBot

import discord
from discord.ext import commands
from darkglance import discord_
from kcg.student_login import kcg_student, driver 
from kcg.finddob import find_dob
from kcg.check import *
import os #to get current working directory and user name

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("DarkGlanceBot has been started")

@client.command()
async def hello(text_channel):
    await text_channel.send('Hi')
    
@client.command()   
async def kcg(text_channel):
    command = text_channel.message.content.split()
    year = '0000'
    try:
        if command[1] == 'photo':
            if check_id(command[2]):
                
                user_id = command[2]

                try:
                    photo = r"c:\Users\{}\Desktop\collected_pics\{}.png".format(os.getlogin(), user_id)
                    with open(photo, 'rb') as f:
                        None
                except:

                    try:
                        year = command[3] 
                    except:
                        None  
                    await text_channel.send("Please Wait while we crack the date of birth")           
                    d_o_b = find_dob(user_id, year)   
                    await text_channel.send("DOB FOUND")
                    await text_channel.send("Please wait while we fetch the photo")
                    kcg_student.login(user_id, d_o_b)
                    kcg_student.get_photo(path = os.getcwd() + '\kcg', uid = user_id)
                
                photo = r"c:\Users\{}\Desktop\collected_pics\{}.png".format(os.getlogin(), user_id)
                with open(photo, 'rb') as f:
                    photo = discord.File(f)
                    await text_channel.send(file=photo)
                
            else:
                await text_channel.send("Invalid RegisterNo/RollNo")
    except:
        None 

client.run(discord_.token)


