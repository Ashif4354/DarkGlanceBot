import requests
from os import getcwd, remove
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from bs4 import BeautifulSoup
import base64
import json
import imgkit

from sys import path
path.append(getcwd().rstrip('kcg'))
from logger.logger import logger
from darkglance import *

user_id_ = None
browser = None
#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])

departments = {
            'ad' : ('ad', 'aids',) , 
            'ae' : ('ae', 'aero', 'aeronautical') ,
            'ao' : ('ao', 'aerospace', 'ase') ,
            'at' : ('at', 'auto', 'automobile') ,
            'ce' : ('ce', 'civil',) ,
            'cs' : ('cs', 'cse','computer'),
            'ec' : ('ec', 'ece'),
            'ee' : ('ee', 'electrical', 'eee'),
            'ei' : ('ei', 'eie', 'instrumentation'),
            'ft' : ('ft', 'fashion'),
            'it' : ('it', 'info'),
            'mc' : ('mc', 'mechatronics', 'mechatronic'),
            'me' : ('me', 'mech', 'mechanical')
            }

options = {
    'format': 'png',
    'crop-w': '915'
}

fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'
fees_login_payload = {}

student_login_url = 'http://studentlogin.kcgcollege.ac.in/'
student_login_payload = {}

marks_payload = {}

def get_payload():
    global fees_login_payload, student_login_payload, marks_payload

    with open('fees_login_payload.json', 'r') as f:
        fees_login_payload = json.load(f)
    
    with open('student_login_payload.json', 'r') as f:
        student_login_payload = json.load(f)

    with open('marks_payload.json', 'r') as f:
        marks_payload = json.load(f)

get_payload()

#_________________________________________________________________________________________________________________________________________________________
class student:
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def student_login(user_id, user_dob):

        global user_id_, browser
        user_id_ = user_id #simply

        #browser = webdriver.Chrome(options = options)
        browser = webdriver.Edge()
        browser.set_window_size(1152, 1080)
        browser.get('http://studentlogin.kcgcollege.ac.in/')
        #login with register no
        if user_id[:4] == '3110':               
            register_no_button = browser.find_element(By.XPATH, '//*[@id="rblOnlineAppLoginMode"]/option[2]')
            register_no_button.click()

        #login with roll no
        else:                          
            roll_no_button = browser.find_element(By.XPATH, '//*[@id="rblOnlineAppLoginMode"]/option[1]')
            roll_no_button.click()

        #roll/register no. input
        user__id = browser.find_element(By.XPATH, '//*[@id="txtuname"]')
        user__id.send_keys(user_id)

        dob = browser.find_element(By.XPATH, '//*[@id="txtpassword"]')
        dob.send_keys(user_dob)

        login_button = browser.find_element(By.XPATH, '//*[@id="Button1"]')
        login_button.click()    
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def fees_login(user_id):

        global user_id_, browser
        user_id_ = user_id #simply
        #browser = webdriver.Chrome(options = options)
        browser = webdriver.Edge()
        browser.get(fees_url)

        #login with register no
        if user_id[:4] == '3110':               
            register_no_button = browser.find_element(By.XPATH, '//*[@id="rblOnlineAppLoginMode"]/option[2]')
            register_no_button.click()

        #login with roll no
        else:                          
            roll_no_button = browser.find_element(By.XPATH, '//*[@id="rblOnlineAppLoginMode"]/option[1]')
            roll_no_button.click()
        
        #roll/register no. input
        user__id = browser.find_element(By.XPATH, '//*[@id="txtuname"]')
        user__id.send_keys(user_id)

        login_button = browser.find_element(By.XPATH, '//*[@id="Button1"]')
        login_button.click()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_name(uid = user_id_):
        if uid[:4] == '3110' :
            fees_login_payload['rblOnlineAppLoginMode'] = '1'
        else:
            fees_login_payload['rblOnlineAppLoginMode'] = '0'

        with requests.Session() as s:
            fees_login_payload['txtuname'] = uid
            try:
                page = s.post(fees_url, data = fees_login_payload, timeout = 10)
                page = s.get(page.url)

                souped = BeautifulSoup(page.content, 'html.parser')
                texts = souped.find_all('span')
                #print(texts)
                name = texts[2].text.strip()
                #print(name)

                return name

            except IndexError:
                return ''

            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student (getname)', text, getcwd().rstrip('kcg') + 'logger')
                try:
                    file.close()
                except:
                    pass
                raise server_down


    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_photo(uid = user_id_): 
        get_payload()
        if uid[:4] == '3110' :
            fees_login_payload['rblOnlineAppLoginMode'] = '1'
        else:
            fees_login_payload['rblOnlineAppLoginMode'] = '0'

        with requests.Session() as s:

            try:
                fees_login_payload['txtuname'] = uid

                page = s.post(fees_url, data = fees_login_payload, timeout = 5)
                page = s.get(page.url)

                souped = BeautifulSoup(page.content, 'html.parser')
                imgs = souped.find_all('img')
                img = imgs[0].attrs.get('src')[22:]

                if img[:3] != '/9j':
                    raise NoPhoto
        
                img = bytes(img, 'utf-8')   

                path = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), uid)
                with open(path, 'wb') as file:
                    file.write(base64.decodebytes(img))
            except NoPhoto:
                raise NoPhoto
            
            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student (get_photo)', text, getcwd().rstrip('kcg') + 'logger')
                try:
                    file.close()
                except:
                    pass
                raise server_down

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_marks(uid, dob):
        with requests.Session() as session:


            student_login_payload['txtuname'] = uid
            student_login_payload['txtpassword'] = dob
            student_login_payload['rblOnlineAppLoginMode'] = 1 if uid[:4] == '3110' else 0
            
            #print(student_login_payload)
            try:
                home = session.post(student_login_url, data = student_login_payload, timeout = 10)
                #print(home.status_code, home.url, home.text)
                marks_page = session.post(home.url, data = marks_payload, timeout = 10)
                #print()
                #print()
                #print()
                #print(marks_page.status_code, marks_page.url, marks_page.text)

                str__ = marks_page.text
                str__ = str__.replace('&nbsp;', '') 

                soup = BeautifulSoup(str__, 'html.parser')
                texts = soup.find('div', {'id': 'dispnl'})

                str_texts = str(texts)
                #print(str_texts)

                html_path = r"{}\temp_pics\{}_html.html".format(getcwd().rstrip('kcg'), uid)
                with open(html_path, 'w') as file:
                    file.write(str_texts)


                img_path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('kcg'), uid)
                with open(html_path, 'r') as f:
                    try:
                        imgkit.from_file(f, img_path, options=options)
                    except:
                        pass
                remove(html_path)
            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student/get_marks ', text, getcwd().rstrip('kcg') + 'logger')
                raise Exception
            finally:
                
                session.close()


        '''
        marks_detail_button = browser.find_element(By.XPATH, '//*[@id="pHeadermarks"]')
        marks_detail_button.click()

        time.sleep(2)

        cam_button = browser.find_element(By.XPATH, '//*[@id="ImageButtonCamv"]')
        cam_button.click()        

        browser.execute_script("window.scrollTo(40, 500)") 
        
        path = r"{}\temp_pics\{}_marks.png".format(getcwd().rstrip('kcg'), uid)
        marks_table = browser.find_element(By.XPATH, '//*[@id="Fpsmarks_viewport"]/table')
        marks_table.screenshot(path)
        browser.quit()'''
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_details(uid = user_id_):
        student_detail_button = browser.find_element(By.XPATH, '//*[@id="pHeaderpersonal"]')
        student_detail_button.click()

        time.sleep(2)
        bio_button = browser.find_element(By.XPATH, '//*[@id="ImageButtonbio"]')
        bio_button.click()

        browser.execute_script("window.scrollTo(0, 450)") 
        
        path = r"{}\temp_pics\{}_details.png".format(getcwd().rstrip('kcg'), uid)
        marks_table = browser.find_element(By.XPATH, '//*[@id="Fpspersonal_viewport"]')
        marks_table.screenshot(path)
        browser.quit()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_regno(user_id, dob_):
        get_payload()
        if user_id[:4] == '3110' :
            student_login_payload['rblOnlineAppLoginMode'] = '1'
        else:
            student_login_payload['rblOnlineAppLoginMode'] = '0'

        with requests.Session() as s:
            student_login_payload['txtuname'] = user_id
            student_login_payload['txtpassword'] = dob_
            try:
                page = s.post(student_login_url, data = student_login_payload, timeout = 10)
                page = s.get(page.url)

                souped = BeautifulSoup(page.content, 'html.parser')
                texts = souped.find_all('span')

                return texts[4].text
            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student (get_regno) ', text, getcwd().rstrip('kcg') + 'logger')
                raise server_down
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_rollno(roll_no = user_id_):
        student_detail_button = browser.find_element(By.XPATH, '//*[@id="pHeaderpersonal"]')
        student_detail_button.click()

        time.sleep(2)
        bio_button = browser.find_element(By.XPATH, '//*[@id="ImageButtonbio"]')
        bio_button.click()
        
        time.sleep(1)
        rollno_ = browser.find_element(By.XPATH, '//*[@id="Fpspersonal_viewport"]/tbody/tr[5]/td[3]')
        rollno_ = rollno_.text
        browser.quit()
        return rollno_

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def search(ctx, batch, text, depts, log_path = f'{getcwd()}\searchlogs\\'):

        date_time = datetime.now().strftime("%d-%m-%Y %H;%M;%S")

        if text == '*':
            text = 'all'

        try:
            file = open(f'{log_path}[{date_time}]   {batch} {text} {depts}.log', 'a')
        except:
            file = open(f'{log_path}[{date_time}]   {batch} {text} (invalid dept).log', 'a')
        file.write(f'Search LOG for  {batch} {text} {depts}\n')
        file.write(f'Requested by {ctx.message.author}\n\n')

        
        corrected_depts = []
        length = 0
        students = []
        traverse_count = 1
        
        try:
            if depts[0] == 'all':
                corrected_depts = departments.keys()
            else:
                for element in depts:
                    for dept_ in departments:
                        if element.lower() in departments[dept_]:
                            if dept_ not in corrected_depts:
                                corrected_depts.append(dept_)
        except IndexError:
            pass
        
        file.write(f'\nCorrected departments  :  {corrected_depts}\n')
        file.write(f'\nKeyword  :  {text}\n')
        
        get_payload()

        def check_student_rollno(user_id):
            fees_login_payload['txtuname'] = user_id    
            #print(user_id)
            try:
                page = requests.post(fees_url, data = fees_login_payload, timeout = 10)
                if page.url != fees_url:
                    return True    
                return False
            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student (check_student_rollno)', text, getcwd().rstrip('kcg') + 'logger')
                
                file.close()
                raise server_down
        
        def add_zero(value, length):
            value_len = len(value)
            req_len = length - value_len
            value = req_len * '0' + value

            return value

        for dept in corrected_depts:            

            file.write(f'\n\nSearching in dept {dept}\n')
            if check_student_rollno(batch + dept + '1'):
                length = 1
                file.write(f"roll number format found out to be  :  {batch + dept + '1'}")
            
            elif check_student_rollno(batch + dept + '01'):
                length = 2
                file.write(f"roll number format found out to be  :  {batch + dept + '01'}")
            
            elif check_student_rollno(batch + dept + '001'):
                length = 3
                file.write(f"roll number format found out to be  :  {batch + dept + '001'}")

            num = 1
            null_count = 0   
            student_count = 1         
            
            file.write('\n\n')

            while null_count < 5:

                The_roll_no = batch + dept + add_zero(str(num), length)
                #print(The_roll_no)

                name = student.get_name(The_roll_no)

                file.write(f'{traverse_count}  {student_count}  {The_roll_no}  {name}')
                
                if name == '':
                    null_count += 1
                    file.write('(no student)\n')
                else:
                    null_count = 0
                    if text in name or text == 'all':
                        students.append((The_roll_no, name))
                        file.write('  (MATCH)\n')
                    else:
                        file.write('\n')
                num += 1
                traverse_count += 1
                student_count += 1

        file.close()

        return students

    #----------------------------------------------------------------------------------------------------------------------------------------------------- 
    def get_np(uid):
        if uid[:4] == '3110' :
            fees_login_payload['rblOnlineAppLoginMode'] = '1'
        else:
            fees_login_payload['rblOnlineAppLoginMode'] = '0'

        with requests.Session() as s:
            
            try:
                fees_login_payload['txtuname'] = uid

                page = s.post(fees_url, data = fees_login_payload, timeout = 5)
                page = s.get(page.url)

                souped = BeautifulSoup(page.content, 'html.parser')
                texts = souped.find_all('span')
                name = texts[2].text.strip()

                imgs = souped.find_all('img')
                img = imgs[0].attrs.get('src')[22:]

                if img[:3] != '/9j':
                    raise NoPhoto
        
                img = bytes(img, 'utf-8')   

                path = r"{}\temp_pics\{}_photo.png".format(getcwd().rstrip('kcg'), uid)
                with open(path, 'wb') as file:
                    file.write(base64.decodebytes(img))
                
                return (name, True)
            
            

            except NoPhoto:
                return (name, False)
                
            except Exception as text:
                logger.exception_logs('dgb/kcg/Student/student (get_np)', text, getcwd().rstrip('kcg') + 'logger')
                






#_________________________________________________________________________________________________________________________________________________________
            