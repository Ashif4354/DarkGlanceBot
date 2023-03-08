import discord
from discord.ext import commands
import mysql.connector
from selenium import webdriver
import asyncio
from time import sleep
from threading import Thread

from sys import path
from os import getcwd, remove
path.append(getcwd().rstrip('gang'))
from logger.logger import logger
from darkglance import *
from kcg.finddob import find_student_dob as getdob
from kcg.Student import student

mycon = None
mysql_cursor = None

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

client = commands.Bot(command_prefix = '.')

'''
class gang:
    def add_member(roll_no, name, discord_id = 'null'):
        dbconnect('darkglancebot')
'''      

@client.event
async def on_ready():
    print("\nServer has been started")
    print("Gang Active")

@client.command()
async def gangmarks(ctx):

    if not await check_auth(ctx, ('owner','admin')):
        return
    
    if not check_server()[1]:
        await ctx.send(embed = server_error_embed)
        return

    mycon = mysql.connector.connect(host='localhost', passwd='rootmysql',user='root', database = 'darkglancebot', autocommit = True)
    mysql_cursor = mycon.cursor()
    mysql_cursor.execute('select * from gang_members')
    gang_members = mysql_cursor.fetchall()
    #print(gang_members)    
    
    gangsters = {}

    for gang_member in gang_members:
        class gangster:
            def __init__(self, roll_no, dob):
                self.roll_no = roll_no
                self.dob = dob
        gangsters[gang_member] = gangster(gang_member[0], gang_member[1])
        
        #print(gang_member)
        class gang_(Thread):
            def run(self):
                
                browser = webdriver.Chrome(options = options)
                browser.get('http://studentlogin.kcgcollege.ac.in/')
                #gangsters[gang_member] = gangster(gang_member[0], gang_member[1])
                print(gangsters)
                roll_no, dob = gangsters[gang_member].roll_no, gangsters[gang_member].dob
                roll_no_button = browser.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[1]') 
                roll_no_button.click()

                user__id = browser.find_element_by_xpath('//*[@id="txtuname"]')
                user__id.send_keys(gangsters[gang_member].roll_no)

                dob_ = browser.find_element_by_xpath('//*[@id="txtpassword"]')
                #print(dob)
                dob_.send_keys(gangsters[gang_member].dob)

                login_button = browser.find_element_by_xpath('//*[@id="Button1"]')
                login_button.click() 
                
                marks_detail_button = browser.find_element_by_xpath('//*[@id="pHeadermarks"]')
                marks_detail_button.click()

                sleep(2)

                cam_button = browser.find_element_by_xpath('//*[@id="btnsubjectchooser"]')
                cam_button.click()

                cam_button = browser.find_element_by_xpath('//*[@id="ImageButtonCamv"]')
                cam_button.click()

                browser.execute_script("window.scrollTo(40, 500)")  

                path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
                marks_table = browser.find_element_by_xpath('//*[@id="Fpsmarks_viewport"]/table')
                marks_table.screenshot(path)

                browser.quit()

        thread = gang_()
        thread.start()
        sleep(3)
    thread.join()

    #print(gangsters)
    tasks = []

    for gang_member in gang_members:
        roll_no = gang_member[0]
        path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
        embed = discord.Embed(title = roll_no, color = 0xffffff)
        pic = discord.File(path, filename = 'temp_marks.png')
        embed.set_image(url = 'attachment://temp_marks.png')

        tasks.append(asyncio.create_task(ctx.send(embed = embed, file = pic)))        

    await asyncio.gather(*tasks)

    for gang_member in gang_members:
        roll_no = gang_member[0]
        path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('gang'), roll_no)
        remove(path)

############################
##------------------------##
client.run(discord_.token)##
##------------------------##
############################