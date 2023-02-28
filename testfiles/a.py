import requests
from aiohttp import ClientSession
from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup
import base64
import asyncio

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

student_login_payload = {
        '__EVENTTARGET' : '' ,
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS' : '',
        '__VIEWSTATE' : '/wEPDwUJMjkwMTA2NTY5D2QWAgIDD2QWCgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCGNvbGxuYW1lHg5EYXRhVmFsdWVGaWVsZAUMY29sbGVnZV9jb2RlHgtfIURhdGFCb3VuZGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnFgFmZAIFDxBkEBUCC1JvbGwgTnVtYmVyEVJlZ2lzdGVyZWQgTnVtYmVyFQIBMAExFCsDAmdnFgFmZAIHDw9kFgQeC3BsYWNlaG9sZGVyBQtSb2xsIE51bWJlch4MYXV0b2NvbXBsZXRlBQNvZmZkAgsPD2QWAh8EBQNvZmZkAg8PDxYCHgdWaXNpYmxlaGRkZP8sQxS46q1mNTMVnB8XKmifm4muh93nP685dZM0dyyi',
        '__VIEWSTATEGENERATOR' : 'CA0B0334',
        '__EVENTVALIDATION' : '/wEdAAerjpyqZPhQVi0g0sCSp89g1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+ZxpWckI3qdmfEJVCu2f5cHN+DvxnwFeFeJ9MIBWR6938qKBsMtBfVKztnpaWRmPF+AhsCuOEtmW/K8pPRoRI0o=',
        'rblOnlineAppLoginMode' : '0',
        'txtuname' : '20cs008',
        'txtpassword' : '25112002',
        'Button1' : 'Login'
        }

#page = requests.post(student_login_url, data = student_login_payload)
#print(page.url)
async def a():
    async with ClientSession() as session:
        page = await session.post(student_login_url, data = student_login_payload)

        print(page.url)

asyncio.run(a())










'''
with HTMLSession() as s:
    post_ = s.post(url, data = fees_login_payload)
    response = s.get(post_.url)
    
    name = response.html.find('td')
    
    print(len(name[6].html.split('\n')[1].rstrip('</span> ')[88:]))
'''