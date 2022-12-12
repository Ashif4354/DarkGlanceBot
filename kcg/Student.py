import requests
import os
from selenium import webdriver
import time
from requests_html import HTML, HTMLSession
from datetime import datetime
from bs4 import BeautifulSoup
import base64

user_id_ = None
browser = None
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

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



class server_down(Exception):
    pass

class NoPhoto(Exception):
    pass

#_________________________________________________________________________________________________________________________________________________________
class student:
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def student_login(user_id, user_dob):

        global user_id_, browser
        user_id_ = user_id #simply

        browser = webdriver.Chrome(options = options)
        browser.get('http://studentlogin.kcgcollege.ac.in/')
        #login with register no
        if user_id[:4] == '3110':               
            register_no_button = browser.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[2]')
            register_no_button.click()

        #login with roll no
        else:                          
            roll_no_button = browser.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[1]') 
            roll_no_button.click()

        #roll/register no. input
        user__id = browser.find_element_by_xpath('//*[@id="txtuname"]')
        user__id.send_keys(user_id)

        dob = browser.find_element_by_xpath('//*[@id="txtpassword"]')
        dob.send_keys(user_dob)

        login_button = browser.find_element_by_xpath('//*[@id="Button1"]')
        login_button.click()    
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def fees_login(user_id):

        global user_id_, browser
        user_id_ = user_id #simply
        browser = webdriver.Chrome(options = options)
        browser.get(fees_url)

        #login with register no
        if user_id[:4] == '3110':               
            register_no_button = browser.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[2]')
            register_no_button.click()

        #login with roll no
        else:                          
            roll_no_button = browser.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[1]') 
            roll_no_button.click()
        
        #roll/register no. input
        user__id = browser.find_element_by_xpath('//*[@id="txtuname"]')
        user__id.send_keys(user_id)

        login_button = browser.find_element_by_xpath('//*[@id="Button1"]')
        login_button.click()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_name(uid = user_id_):
        if uid[:4] == '3110' :
            fees_login_payload['rblOnlineAppLoginMode'] = '1'

        with requests.Session() as s:
            fees_login_payload['txtuname'] = uid
            try:
                page = s.post(fees_url, data = fees_login_payload, timeout = 10)
                page = s.get(page.url)

                souped = BeautifulSoup(page.content, 'html.parser')
                texts = souped.find_all('span')
                name = texts[2].text.strip()

                return name

            except Exception as e:
                print(datetime.now().strftime("%d-%m-%Y %H;%M;%S"), '  ', e)
                try:
                    file.close()
                except:
                    pass
                raise server_down
        '''
        name_ = browser.find_element_by_xpath('//*[@id="lblsname"]')
        name_ = name_.text
        browser.quit()
        return name_'''

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_photo(uid = user_id_): 
        if uid[:4] == '3110' :
            fees_login_payload['rblOnlineAppLoginMode'] = '1'

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

                path = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), uid)
                with open(path, 'wb') as file:
                    file.write(base64.decodebytes(img))
            except NoPhoto:
                pass
            except Exception as e:
                print(datetime.now().strftime("%d-%m-%Y %H;%M;%S"), ' ', 'in get photo ', e)
                try:
                    file.close()
                except:
                    pass
                raise server_down
        '''
        try:
            img_src = browser.find_element_by_xpath('//*[@id="Imagestudent"]').get_attribute("src")
        except:
            browser.quit()
            raise Exception
         
        browser.get(img_src)
            
        pic_ = browser.find_element_by_xpath('/html/body/img')

        path = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), uid)
        with open(path, 'wb') as file:            
            
            file.write(pic_.screenshot_as_png)
        browser.quit()
        '''

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_marks(uid = user_id_):
        marks_detail_button = browser.find_element_by_xpath('//*[@id="pHeadermarks"]')
        marks_detail_button.click()

        time.sleep(2)

        cam_button = browser.find_element_by_xpath('//*[@id="btnsubjectchooser"]')
        cam_button.click()

        cam_button = browser.find_element_by_xpath('//*[@id="ImageButtonCamv"]')
        cam_button.click()

        

        browser.execute_script("window.scrollTo(40, 500)") 
        
        path = r"{}\temp_pics\{}_marks.png".format(os.getcwd(), uid)
        marks_table = browser.find_element_by_xpath('//*[@id="Fpsmarks_viewport"]/table')
        marks_table.screenshot(path)
        browser.quit()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_details(uid = user_id_):
        student_detail_button = browser.find_element_by_xpath('//*[@id="pHeaderpersonal"]')
        student_detail_button.click()

        time.sleep(2)
        bio_button = browser.find_element_by_xpath('//*[@id="ImageButtonbio"]')
        bio_button.click()

        browser.execute_script("window.scrollTo(0, 450)") 
        
        path = r"{}\temp_pics\{}_details.png".format(os.getcwd(), uid)
        marks_table = browser.find_element_by_xpath('//*[@id="Fpspersonal_viewport"]')
        marks_table.screenshot(path)
        browser.quit()
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_regno(roll_no = user_id_):
        regno_ = browser.find_element_by_xpath('//*[@id="Label15"]')
        regno_ = regno_.text
        browser.quit()
        return regno_
    
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def get_rollno(roll_no = user_id_):
        student_detail_button = browser.find_element_by_xpath('//*[@id="pHeaderpersonal"]')
        student_detail_button.click()

        time.sleep(2)
        bio_button = browser.find_element_by_xpath('//*[@id="ImageButtonbio"]')
        bio_button.click()
        
        time.sleep(1)
        rollno_ = browser.find_element_by_xpath('//*[@id="Fpspersonal_viewport"]/tbody/tr[5]/td[3]')
        rollno_ = rollno_.text
        browser.quit()
        return rollno_

    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def search(ctx, batch, text, depts, log_path = f'{os.getcwd()}\searchlogs\\'):

        date_time = datetime.now().strftime("%d-%m-%Y %H;%M;%S")

        if text == '*':
            text = 'all'
        file = open(f'{log_path}[{date_time}]   {batch} {text} {depts}.log', 'a')
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

        def check_student_rollno(user_id):
            fees_login_payload['txtuname'] = user_id    
            #print(user_id)
            try:
                page = requests.post(fees_url, data = fees_login_payload, timeout = 10)
                if page.url != fees_url:
                    return True    
                return False
            except Exception as e:
                print(date_time, '  ', e)
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
            
            file.write('\n\n')

            while null_count < 5:

                profile_page = None
                The_roll_no = batch + dept + add_zero(str(num), length)

                name = student.get_name(The_roll_no)

                file.write(f'{traverse_count}  {The_roll_no}  {name}')
                
                if name == '':
                    null_count += 1
                    file.write('\n')
                else:
                    null_count = 0
                    if text in name or text == 'all':
                        students.append((The_roll_no, name))
                        file.write('  (MATCH)\n')
                    else:
                        file.write('\n')
                num += 1
                traverse_count += 1

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

                path = r"{}\temp_pics\{}_photo.png".format(os.getcwd(), uid)
                with open(path, 'wb') as file:
                    file.write(base64.decodebytes(img))
                
                return (name, True)

            except NoPhoto:
                return (name, False)


            except Exception as e:
                print(datetime.now().strftime("%d-%m-%Y %H;%M;%S"), ' ', ' in get np', e)
                






#_________________________________________________________________________________________________________________________________________________________
            


        

        

            

#student.student_login('311020104013', '25112002')
#student.fees_login('20cs008')
#student.get_photo(uid = user_id_)
#print(student.get_name('20cs008'))
#student.get_marks(uid = user_id_)
#student.search('20', 'ashif', ['cs'])
#print(student.get_name('20cs008'))
#student.search('20', 'ashif', ('cs',))


