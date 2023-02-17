import requests
import discord

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'

fees_login_payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
    'rblOnlineAppLoginMode' : None,
    'txtuname' : None,
    'Button1' : 'Login'
    }


student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

student_login_payload = {
        '__EVENTTARGET' : '' ,
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS' : '',
        '__VIEWSTATE' : '/wEPDwUJMjkwMTA2NTY5D2QWAgIDD2QWCgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCGNvbGxuYW1lHg5EYXRhVmFsdWVGaWVsZAUMY29sbGVnZV9jb2RlHgtfIURhdGFCb3VuZGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnFgFmZAIFDxBkEBUCC1JvbGwgTnVtYmVyEVJlZ2lzdGVyZWQgTnVtYmVyFQIBMAExFCsDAmdnFgFmZAIHDw9kFgQeC3BsYWNlaG9sZGVyBQtSb2xsIE51bWJlch4MYXV0b2NvbXBsZXRlBQNvZmZkAgsPD2QWAh8EBQNvZmZkAg8PDxYCHgdWaXNpYmxlaGRkZEUh8Q9VeEnmpvJTjWVIwQmtVpX5IBYcjkAZZqWYNv5m', 
        '__VIEWSTATEGENERATOR' : 'CA0B0334',
        '__EVENTVALIDATION' : '/wEdAAfEhVpMiIC9PlqrGxNesSta1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+ZxpWckI3qdmfEJVCu2f5cHN+DvxnwFeFeJ9MIBWR6935FJfAFbS62yyYTlq6hIkdlrWUyRFAO0MmBe4dmPHJe8=',
        'rblOnlineAppLoginMode' : None,
        'txtuname' : None,
        'txtpassword' : None,
        'Button1' : 'Login'
        }

def check_student_id(user_id):
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 0
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    fees_login_payload['rblOnlineAppLoginMode'] = 1
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_student_rollno(user_id):
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 0
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_student_registerno(user_id):
    fees_login_payload['txtuname'] = user_id
    
    fees_login_payload['rblOnlineAppLoginMode'] = 1
    page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
    if page.url != fees_url:
        return True
    
    return False

def check_server():
        
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
                server_status_embed.add_field(name = 'Fees Login', value = 'Positive', inline = False)
            else:
                status = False
                raise Exception

        except Exception:
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
print(check_server())