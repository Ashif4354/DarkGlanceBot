#DarkGlanceBot

import discord
from discord.ext import commands
from darkglance import discord_
from kcg.student_login import kcg_student, driver 
from kcg.finddob import find_dob
from kcg.check import *
import os #to get current working directory

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("DarkGlanceBot has been started")

@client.command()
async def hello(text):
    await text.send('Hi')
    
@client.command()   
async def kcg(text):
    command = text.message.content.split()
    year = '0000'
    try:
        if command[1] == 'photo':
            if check_id(command[2]):
                
                user_id = command[2]
                try:
                    year = command[3] 
                except:
                    None  
                            
                d_o_b = find_dob(user_id, year)                
                kcg_student.login(user_id, d_o_b)
                kcg_student.get_photo(path = os.getcwd() + '\kcg', uid = user_id)
                
                photo = "{}\kcg\collected_pics\{}.png".format(os.getcwd(), user_id)
                with open(photo, 'rb') as f:
                    photo = discord.File(f)
                    await text.send(file=photo)
                
            else:
                await text.send("Invalid RegisterNo/RollNo")
    except:
        None       
            
        

    



client.run(discord_.token)


