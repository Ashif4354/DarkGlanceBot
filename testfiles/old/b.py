import requests


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
    'txtpassword' : '25112002',
    'Button1' : 'Login'
}

page = requests.post(student_login_url, data = student_login_payload)
print(page.url)