from requests import get, Session
from bs4 import BeautifulSoup
import json
from os import getcwd, environ

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

        #---------------------------------------------------------------------------

        with open('marks_payload.json', 'r') as f:
            data2 = json.load(f)
        
        data['txtuname'] = environ['ROLL_NO']
        data['txtpassword'] = environ['DOB']
        data['rblOnlineAppLoginMode'] = 0
        #print(data)

        response = session.post('http://studentlogin.kcgcollege.ac.in/', data = data)
        page = response.text
        soup = BeautifulSoup(page, 'html.parser')

        element = soup.find("input", {"id": "__VIEWSTATE"})
        __VIEWSTATE = element.attrs['value']
        if data2['__VIEWSTATE'] != __VIEWSTATE:
            data2['__VIEWSTATE'] = __VIEWSTATE

        with open('marks_payload.json', 'w') as json_file:
            json.dump(data2, json_file)

        with open(f'{gang_path}\\marks_payload.json', 'w') as json_file:
            json.dump(data2, json_file)

        #print(data2)






#get_payload()