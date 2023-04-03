from requests import Session
import json
from bs4 import BeautifulSoup
import imgkit

options = {
    'format': 'png',
    'crop-w': '915'
}

url = 'http://studentlogin.kcgcollege.ac.in/'
fees_login_payload = {}

def get_payload():
    global fees_login_payload

    with open('student_login_payload.json', 'r') as f:
            fees_login_payload = json.load(f)

get_payload()

new_Payload = {}
def get_payload():
    global new_payload

    with open('a.json', 'r') as f:
            new_payload = json.load(f)

get_payload()

with Session() as session:
    print(1)
    home = session.post(url, data = fees_login_payload, timeout = 2)
    #with open('page.html', 'wb') as file:
    #    file.write(home.content)
    print(2)
    next_page = session.post(home.url, data = new_payload)
    #with open('page2.html', 'wb') as file:
        #file.write(next_page.content)

    str__ = next_page.text
    str__ = str__.replace('&nbsp;', '')   


    print(3)
    soup = BeautifulSoup(str__, 'html.parser')
    texts = soup.find('div', {'id': 'dispnl'})
    #print(type(texts), str(texts))
    print(4)

    str_texts = str(texts)

    
    with open('page3.html', 'w') as file:
        file.write(str_texts)

    with open('page3.html', 'r') as f:
        try:
            imgkit.from_file(f, 'example.png', options=options)
        except:
            pass
    
