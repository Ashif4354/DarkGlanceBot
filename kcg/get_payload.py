from requests import get, Session
from bs4 import BeautifulSoup
import json
from os import getcwd

def get_payload():
    gang_path = getcwd().rstrip('kcg\\') + '\gang'

    with Session() as session:
        with open('fees_login_payload.json', 'r') as f:
            data = json.load(f)

        response = session.get('http://studentonlinepayment.kcgcollege.ac.in/')
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        element = soup.find("input", {"id": "__VIEWSTATE"})
        __VIEWSTATE = element.attrs['value']
        if data['__VIEWSTATE'] != __VIEWSTATE:
            data['__VIEWSTATE'] = __VIEWSTATE

        element = soup.find("input", {"id": "__EVENTVALIDATION"})
        __EVENTVALIDATION = element.attrs['value']
        #print(__EVENTVALIDATION)
        if data['__EVENTVALIDATION'] != __EVENTVALIDATION:
            data['__EVENTVALIDATION'] = __EVENTVALIDATION
        #print(data)
        with open('fees_login_payload.json', 'w') as json_file:
            json.dump(data, json_file)
        
        with open(f'{gang_path}\\fees_login_payload.json', 'w') as json_file:
            json.dump(data, json_file)
        #---------------------------------------------------------------------------

        with open('student_login_payload.json', 'r') as f:
            data = json.load(f)

        response = session.get('http://studentlogin.kcgcollege.ac.in/')
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        element = soup.find("input", {"id": "__VIEWSTATE"})
        __VIEWSTATE = element.attrs['value']
        if data['__VIEWSTATE'] != __VIEWSTATE:
            data['__VIEWSTATE'] = __VIEWSTATE

        element = soup.find("input", {"id": "__EVENTVALIDATION"})
        __EVENTVALIDATION = element.attrs['value']
        if data['__EVENTVALIDATION'] != __EVENTVALIDATION:
            data['__EVENTVALIDATION'] = __EVENTVALIDATION
        
        with open('student_login_payload.json', 'w') as json_file:
            json.dump(data, json_file)

        with open(f'{gang_path}\\student_login_payload.json', 'w') as json_file:
            json.dump(data, json_file)

#get_payload()