import requests
import discord
from os import getcwd
from bs4 import BeautifulSoup
import json

from sys import path
path.append(getcwd().rstrip('kcg'))
from darkglance import *

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'
fees_login_payload = {}

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'
student_login_payload = {}

def get_payload():
    global fees_login_payload, student_login_payload

    with open('fees_login_payload.json', 'r') as f:
        fees_login_payload = json.load(f)
        #print(fees_login_payload)
    
    with open('student_login_payload.json', 'r') as f:
        student_login_payload = json.load(f)
        
#get_payload()

def check_student_id(user_id):
    get_payload()
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 0
    try:
        page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    except :
        
        raise server_down
    
    #print(fees_login_payload)
    if page.url != fees_url:
        return True
    
    fees_login_payload['rblOnlineAppLoginMode'] = 1
    
    try:
        page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    except:
        raise server_down

    if page.url != fees_url:
        return True
    
    return False

def check_student_rollno(user_id):
    get_payload()
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 0
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    
    if page.url != fees_url:
        return True
    
    return False

def check_student_registerno(user_id):
    get_payload()
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 1
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_server():
    get_payload()
        
    server_status_embed = discord.Embed(title = 'KCG Server status', color = 0xffffff)    

    fees_login_payload['rblOnlineAppLoginMode'] = '0'
    fees_login_payload['txtuname'] = '20cs008'

    student_login_payload['rblOnlineAppLoginMode'] = '0'
    student_login_payload['txtuname'] = '20cs008'
    student_login_payload['txtpassword'] = '25112002'

    with requests.Session() as s:
        try:
            page = s.get(fees_url, timeout = 3)
            #print(page.content)
            server_status_embed.add_field(name = 'Fees Login page', value = 'Positive', inline = False)
        except Exception as text:
            server_status_embed.add_field(name = 'Fees Login page', value = 'Negative', inline = False)

        try:
            page = s.post(fees_url, data = fees_login_payload, timeout = 3)
            #print(page.url)
            if page.url != fees_url:
                status = True
                server_status_embed.add_field(name = 'Fees Login', value = 'Positive', inline = False)
            else:
                status = False
                raise Exception

        except Exception:
            status = False
            server_status_embed.add_field(name = 'Fees Login', value = 'Negative', inline = False)
        
        try:
            page = s.get(student_login_url, timeout = 3)
            #print(page.status_code)
            server_status_embed.add_field(name = 'Student Login page', value = 'Positive', inline = False)
        except Exception:
            server_status_embed.add_field(name = 'Student Login page', value = 'Negative', inline = False)

        try:
            page = s.post(student_login_url, data = student_login_payload, timeout = 3)
            #print(page.url)
            if page.url != student_login_url:
                server_status_embed.add_field(name = 'Student Login', value = 'Positive', inline = False)
            else:
                raise Exception
            
        except Exception:
            server_status_embed.add_field(name = 'Student Login', value = 'Negative', inline = False)
        
    return (server_status_embed, status) 


#print(check_student_id('20cs008'))
#print(check_server())