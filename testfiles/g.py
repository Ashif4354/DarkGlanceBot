import json

fees_login_payload = {
        '__EVENTTARGET' : '' ,
        '__EVENTARGUMENT' : '',
        '__LASTFOCUS' : '',
        '__VIEWSTATE' : None,
        '__EVENTVALIDATION' : None,
        'rblOnlineAppLoginMode' : None,
        'txtuname' : None,
        'txtpassword' : None,
        'Button1' : 'Login'
        }

with open('a.json', 'w') as json_file:
  json.dump(fees_login_payload, json_file)