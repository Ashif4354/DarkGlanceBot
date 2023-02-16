import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
from datetime import datetime as dt

print('Photo notifier active')

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'

fees_login_payload = {
    '__EVENTTARGET' : '' ,
    '__EVENTARGUMENT' : '',
    '__LASTFOCUS' : '',
    '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
    '__VIEWSTATEGENERATOR' : 'CA0B0334',
    '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
    'rblOnlineAppLoginMode' : '0',
    'txtuname' : None,
    'Button1' : 'Login'
    }

def photo_got(s, rollno): 
    fees_login_payload['txtuname'] = rollno
    
   

    try:

        page = s.post(fees_url, data = fees_login_payload, timeout = 10)
        page = s.get(page.url)

        souped = BeautifulSoup(page.content, 'html.parser')
        imgs = souped.find_all('img')
        img = imgs[0].attrs.get('src')[22:]
        #print('hi')
        if img[:3] != '/9j':
            #print('False')
            return False
        else:
            #print('True')
            return True

    except Exception as e:
        print(dt.now().strftime("%d-%m-%Y %H;%M;%S"), ' ', 'in get photo ', e)

webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1062409359105208473/vR2kBGWZb2zyODbp1tJ6ll8x3gQ_xDZiqWo2w5oNy8Mg4LaqOvUbVkU1u1Y5EAjNGNdC')
embed = DiscordEmbed(title = 'PHOTOs Available now', description = 'PHOTOs now Availabe', color = 0xffffff)
webhook.add_embed(embed)

webhook2 = DiscordWebhook(url = 'https://discord.com/api/webhooks/1062409359105208473/vR2kBGWZb2zyODbp1tJ6ll8x3gQ_xDZiqWo2w5oNy8Mg4LaqOvUbVkU1u1Y5EAjNGNdC')
embed2 = DiscordEmbed(title = 'Program Check', description = 'Program still running', color = 0xffffff)
webhook2.add_embed(embed2)

photo_got_ = False

previous_date = datetime.date.today()

while not photo_got_:
    with requests.Session() as s:
        if datetime.date.today() != previous_date:
            previous_date = datetime.date.today()
        
            webhook2.execute()
    

        for a in range(1, 21):
            rollno = '20cs0' + str(a)
            #print(a)

            if photo_got(s, rollno):
                photo_got_ = True
                for b in range(10):
                    time.sleep(5)
                    webhook.execute()
                break
            else:
                continue
        time.sleep(600)


