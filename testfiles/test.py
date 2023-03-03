import requests 
from bs4 import BeautifulSoup

url = 'http://studentlogin.kcgcollege.ac.in/'

payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : None,
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : None,
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : '20cs008',
    'txtpassword' : '25112002',
    'Button1' : 'Login'
}


 
with requests.Session() as session:
    page = session.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')
    element = soup.find("input", {"id": "__VIEWSTATE"})
    payload['__VIEWSTATE'] = element.attrs['value']

    element = soup.find("input", {"id": "__EVENTVALIDATION"})
    payload['__EVENTVALIDATION'] = element.attrs['value']
    page = session.post(url, data = payload)

    with open('page.html', 'w') as file:
        file.write(page.text)
