import requests
from requests_html import HTML, HTMLSession
from bs4 import BeautifulSoup
import base64

url = 'http://studentonlinepayment.kcgcollege.ac.in/'

payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : '20CS112',
    'Button1' : 'Login'
    }


with requests.Session() as s:
    page = s.post(url, data = payload)
    page = s.get(page.url)

    souped = BeautifulSoup(page.content, 'html.parser')
    imgs = souped.find_all('img')
    img = imgs[0].attrs.get('src')[22:]
    img = bytes(img, 'utf-8')   

    with open('a.png', 'wb') as file:
        file.write(base64.decodebytes(img))












'''
with HTMLSession() as s:
    post_ = s.post(url, data = fees_login_payload)
    response = s.get(post_.url)
    
    name = response.html.find('td')
    
    print(len(name[6].html.split('\n')[1].rstrip('</span> ')[88:]))
'''