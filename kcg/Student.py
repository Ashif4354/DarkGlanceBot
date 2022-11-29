import requests
import os
from selenium import webdriver
import time

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
            'mc' : ('mc', 'mechatronics', 'mechatronic'),
            'me' : ('me', 'mech', 'mechanical'),
            'it' : ('it')
            }

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

class student:
    
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
    
    def fees_login(user_id):

        global user_id_, browser
        user_id_ = user_id #simply
        browser = webdriver.Chrome(options = options)
        browser.get('http://studentonlinepayment.kcgcollege.ac.in/')

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

    
    def get_name(uid = user_id_):

        name_ = browser.find_element_by_xpath('//*[@id="lblsname"]')
        name_ = name_.text
        browser.quit()
        return name_

    
    def get_photo(uid = user_id_): 
        try:
            img_src = browser.find_element_by_xpath('//*[@id="Imagestudent"]').get_attribute("src")
        except:
            browser.quit()
            raise Exception
         
        browser.get(img_src)
            
        pic_ = browser.find_element_by_xpath('/html/body/img')

        path = r"c:\Users\{}\Desktop\collected_pics".format(os.getlogin())
        with open('{}\{}_photo.png'.format(path, uid), 'wb') as file:            
            
            file.write(pic_.screenshot_as_png)
        browser.quit()
    
    def get_marks(uid = user_id_):
        marks_detail_button = browser.find_element_by_xpath('//*[@id="pHeadermarks"]')
        marks_detail_button.click()

        time.sleep(2)
        cam_button = browser.find_element_by_xpath('//*[@id="ImageButtonCamv"]')
        cam_button.click()

        browser.execute_script("window.scrollTo(40, 500)") 
        
        path = r"c:\Users\{}\Desktop\collected_pics".format(os.getlogin())
        marks_table = browser.find_element_by_xpath('//*[@id="Fpsmarks_viewport"]/table')
        marks_table.screenshot('{}\{}_marks.png'.format(path, uid))
        browser.quit()

    def get_details(uid = user_id_):
        student_detail_button = browser.find_element_by_xpath('//*[@id="pHeaderpersonal"]')
        student_detail_button.click()

        time.sleep(2)
        bio_button = browser.find_element_by_xpath('//*[@id="ImageButtonbio"]')
        bio_button.click()

        browser.execute_script("window.scrollTo(0, 450)") 
        
        path = r"c:\Users\{}\Desktop\collected_pics".format(os.getlogin())
        marks_table = browser.find_element_by_xpath('//*[@id="Fpspersonal_viewport"]')
        marks_table.screenshot('{}\{}_details.png'.format(path, uid))
        browser.quit()
    
    def get_regno(roll_no = user_id_):
        regno_ = browser.find_element_by_xpath('//*[@id="Label15"]')
        regno_ = regno_.text
        browser.quit()
        return regno_

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


    def search(user_id, depts):
        
        corrected_depts = []

        for element in depts:
            for dept_ in departments:
                if element in departments[dept_]:
                    if dept_ not in corrected_depts:
                        corrected_depts.append(dept_)
        
        print(corrected_depts)
        





        
        



        
            


        

        

            

#student.student_login('311020104013', '25112002')
#student.get_photo(path = os.getcwd(), uid = user_id_)
#student.fees_login('20cs008')
#print(student.get_name('20cs008'))
#student.get_marks(uid = user_id_)


