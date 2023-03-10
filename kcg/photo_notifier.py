import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import datetime
from datetime import datetime as dt
import json

print('Photo notifier active')

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'
fees_login_payload = {}

def get_payload():
    global fees_login_payload

    with open('fees_login_payload.json', 'r') as f:
            fees_login_payload = json.load(f)

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
    except IndexError:
        print('server down')
        
    except Exception as text:
        print(dt.now().strftime("%d-%m-%Y %H;%M;%S"), ' ', 'in photo got ', text)

webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/1062409359105208473/vR2kBGWZb2zyODbp1tJ6ll8x3gQ_xDZiqWo2w5oNy8Mg4LaqOvUbVkU1u1Y5EAjNGNdC')
embed = DiscordEmbed(title = 'PHOTOs Available now', description = 'PHOTOs now Availabe', color = 0xffffff)
webhook.add_embed(embed)

webhook2 = DiscordWebhook(url = 'https://discord.com/api/webhooks/1062409359105208473/vR2kBGWZb2zyODbp1tJ6ll8x3gQ_xDZiqWo2w5oNy8Mg4LaqOvUbVkU1u1Y5EAjNGNdC')
embed2 = DiscordEmbed(title = 'Program Check', description = 'Program still running', color = 0xffffff)
webhook2.add_embed(embed2)

photo_got_ = False

previous_date = datetime.date.today()

while not photo_got_:
    get_payload()
    with requests.Session() as s:
        if datetime.date.today() != previous_date:
            previous_date = datetime.date.today()
        
            webhook2.execute()
    

        for a in range(1, 21):
            rollno = '22cs0' + str(a)
            #print(a)

            if photo_got(s, rollno):
                photo_got_ = True
                for b in range(10):
                    time.sleep(5)
                    webhook.execute()
                break
            else:
                continue
        time.sleep(1800)


