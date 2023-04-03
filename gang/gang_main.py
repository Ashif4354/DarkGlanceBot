import discord
from discord.ext import commands
import mysql.connector
#from msedge.selenium_tools import Edge, EdgeOptions
#from selenium import webdriver

#from selenium import webdriver
#from selenium.webdriver.common.by import By

import asyncio
from time import sleep
from threading import Thread
from requests import Session
from bs4 import BeautifulSoup
import json
import imgkit
from sys import path
from os import getcwd, remove

path.append(getcwd().rstrip('gang'))
from logger.logger import logger
from darkglance import *
from kcg.finddob import find_student_dob as getdob
from kcg.check import check_server

mycon = None
mysql_cursor = None
success = True

#options = webdriver.Options()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])

#options = EdgeOptions()
#options.use_chromium = True
#options.add_argument('headless')

options = {
    'format': 'png',
    'crop-w': '915'
}

client = commands.Bot(command_prefix = '.')

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'
student_login_payload = {}
marks_payload = {}

def get_payload():
    global student_login_payload, marks_payload

    with open('student_login_payload.json', 'r') as f:
            student_login_payload = json.load(f)

    with open('marks_payload.json', 'r') as f:
            marks_payload = json.load(f)

get_payload()


@client.event
async def on_ready():
    print("\nServer has been started")
    print("Gang Active")

@client.command()
async def addgangmember(ctx): #.addgangmember 20cs008 Ashif 25112002
    logger.input_kcg(ctx, getcwd().rstrip('gang') + '\logger')

    if not await check_auth(ctx, ('owner',)):
        return

    mycon =  mysql.connector.connect(host='localhost', passwd='rootmysql',user='root', database = 'darkglancebot', autocommit = True)
    mysql_cursor = mycon.cursor()
    
    command = ctx.message.content.split()

    try:
        mysql_cursor.execute(f"INSERT INTO gang_members values('{command[1]}', '{command[2]}', '{command[3]}')")
        await ctx.send(embed = discord.Embed(title = 'New gangster added', description = f'{command[2]}  {command[1]}', color = 0xffffff))
    except IndexError:
        await ctx.send(embed = discord.Embed(title = 'Invalid command', color = 0xffffff))
    except Exception as text:
        logger.exception_logs('dgb/gang/gang_main/addgangmember ', text, getcwd().rstrip('gang') + 'logger')
    
    mysql_cursor.close()
    mycon.close()


@client.command()
async def gangmarks(ctx):
    global success

    logger.input_kcg(ctx, getcwd().rstrip('gang') + '\logger')

    if not await check_auth(ctx, ('owner','admin')):
        return
    
    if not check_server()[1]:
        await ctx.send(embed = server_error_embed)
        return
    
    await ctx.send(embed = discord.Embed(title = 'Kindly Wait', description = 'Marks are being fetched', color = 0xffffff))

    mycon = mysql.connector.connect(host='localhost', passwd='rootmysql',user='root', database = 'darkglancebot', autocommit = True)
    mysql_cursor = mycon.cursor()
    mysql_cursor.execute('select * from gang_members')
    gang_members = mysql_cursor.fetchall()

    #print(gang_members)    
    #gang_members = [('20cs007','arunvel', '22112002')]

    threads = []
    
    for gang_member in gang_members:        
        
        #print(gang_member)
        class gangster:
            def __init__(self, roll_no, dob):
                self.roll_no = roll_no
                self.dob = dob
        
        class gang_(Thread):
            def __init__(self, gangster_object, ssesion_object):
                super().__init__()
                self.gangster_object = gangster_object
                self.session = ssesion_object

            def run(self):
                global success

                student_login_payload_local = student_login_payload.copy()

                roll_no, dob = self.gangster_object.roll_no, self.gangster_object.dob
                session = self

                student_login_payload_local['txtuname'] = roll_no
                student_login_payload_local['txtpassword'] = dob
                student_login_payload_local['rblOnlineAppLoginMode'] = 0


                try:
                    home = self.session.post(student_login_url, data = student_login_payload_local, timeout = 10)
                    next_page = self.session.post(home.url, data = marks_payload, timeout = 10)

                    str__ = next_page.text
                    str__ = str__.replace('&nbsp;', '') 
                    soup = BeautifulSoup(str__, 'html.parser')
                    texts = soup.find('div', {'id': 'dispnl'})

                    str_texts = str(texts)

                    html_path = r"{}\temp_pics\{}_html.html".format(getcwd().rstrip('gang'), roll_no)
                    with open(html_path, 'w') as file:
                        file.write(str_texts)


                    img_path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
                    with open(html_path, 'r') as f:
                        try:
                            imgkit.from_file(f, img_path, options=options)
                        except:
                            pass
                except Exception as text:
                    success = False
                    logger.exception_logs('dgb/gang/gang_main/gangmarks ', text, getcwd().rstrip('gang') + 'logger')

                    
        thread = gang_(gangster(gang_member[0], gang_member[2]), Session())
        threads.append(thread)
        thread.start()
        
    for thread_ in threads:
        thread_.join()

    #print(gangsters)
    tasks = []
    if success:
        for gang_member in gang_members:
            roll_no = gang_member[0]
            path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
            embed = discord.Embed(title = roll_no, description = gang_member[1], color = 0xffffff)
            pic = discord.File(path, filename = f'{roll_no}.png')
            embed.set_image(url = f'attachment://{roll_no}.png')
            
            tasks.append(asyncio.create_task(ctx.send(embed = embed, file = pic))) 
             

        await asyncio.gather(*tasks)
        await ctx.send(embed = discord.Embed(title = 'Marks of all gang members has been fetched', color = 0xffffff))
    else:
        description = '''
        This may be due to one of the following reasons
        - College server down
        - College server timed out 
        - College server took too long to respond
        - Marks of all gang members could not be fetched
        '''
        embed = discord.Embed(title = 'Some error occured', description = description, color = 0xffffff)
        await ctx.send(embed = embed)


    for gang_member in gang_members:
        roll_no = gang_member[0]
        img_path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
        html_path = r"{}\temp_pics\{}_html.html".format(getcwd().rstrip('gang'), roll_no)
        try:
            remove(img_path)
            remove(html_path)
        except:
            pass
    
    mysql_cursor.close()
    mycon.close()
    success = True

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