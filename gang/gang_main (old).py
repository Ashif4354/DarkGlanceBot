import discord
from discord.ext import commands
import mysql.connector
#from msedge.selenium_tools import Edge, EdgeOptions
#from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By

import asyncio
from time import sleep
from threading import Thread

from sys import path
from os import getcwd, remove
path.append(getcwd().rstrip('gang'))
from logger.logger import logger
from darkglance import *
from kcg.finddob import find_student_dob as getdob
from kcg.check import check_server

mycon = None
mysql_cursor = None

#options = webdriver.Options()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])

#options = EdgeOptions()
#options.use_chromium = True
#options.add_argument('headless')

client = commands.Bot(command_prefix = '.')



@client.event
async def on_ready():
    print("\nServer has been started")
    print("Gang Active")

@client.command()
async def addgangmember(ctx): #.addgangmember <roll> <name> <ddmmyyyy>
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

    threads = []

    for gang_member in gang_members:        
        
        #print(gang_member)
        class gang_(Thread):
            def __init__(self, gangster_object):
                super().__init__()
                self.gangster_object = gangster_object

            def run(self):
                browser = webdriver.Edge()
                browser.set_window_size(1152, 1080)
                #browser = Edge(options = options)
                browser.get('http://studentlogin.kcgcollege.ac.in/')
                #gangsters[gang_member] = gangster(gang_member[0], gang_member[1])
                #print(gangsters)
                roll_no, dob = self.gangster_object.roll_no, self.gangster_object.dob
                #print(roll_no, dob)

                roll_no_button = browser.find_element(By.XPATH, '//*[@id="rblOnlineAppLoginMode"]/option[1]')
                roll_no_button.click()

                user__id = browser.find_element(By.XPATH, '//*[@id="txtuname"]')
                user__id.send_keys(roll_no)

                dob_ = browser.find_element(By.XPATH, '//*[@id="txtpassword"]')
                #print(dob)
                dob_.send_keys(dob)

                login_button = browser.find_element(By.XPATH, '//*[@id="Button1"]')
                login_button.click() 
                
                marks_detail_button = browser.find_element(By.XPATH, '//*[@id="pHeadermarks"]')
                marks_detail_button.click()

                sleep(2)

                cam_button = browser.find_element(By.XPATH, '//*[@id="ImageButtonCamv"]')
                cam_button.click()

                browser.execute_script("window.scrollTo(40, 500)")  

                path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
                marks_table = browser.find_element(By.XPATH, '//*[@id="Fpsmarks_viewport"]/table')
                marks_table.screenshot(path)
                browser.quit()

        class gangster:
            def __init__(self, roll_no, dob):
                self.roll_no = roll_no
                self.dob = dob
        
        
        thread = gang_(gangster(gang_member[0], gang_member[2]))
        threads.append(thread)
        thread.start()
        
    for thread_ in threads:
        thread_.join()

    #print(gangsters)
    tasks = []

    for gang_member in gang_members:
        roll_no = gang_member[0]
        path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
        embed = discord.Embed(title = roll_no, description = gang_member[1], color = 0xffffff)
        pic = discord.File(path, filename = f'{roll_no}.png')
        embed.set_image(url = f'attachment://{roll_no}.png')

        tasks.append(asyncio.create_task(ctx.send(embed = embed, file = pic)))        

    await asyncio.gather(*tasks)
    await ctx.send(embed = discord.Embed(title = 'Marks of all gang members has been fetched', color = 0xffffff))


    for gang_member in gang_members:
        roll_no = gang_member[0]
        path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
        remove(path)
    
    mysql_cursor.close()
    mycon.close()

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