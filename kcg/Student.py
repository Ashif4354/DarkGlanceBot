import requests
import os
from selenium import webdriver

user_id_ = None
browser = None

class student:
    
    def student_login(user_id, user_dob):

        global user_id_, browser
        user_id_ = user_id #simply

        browser = webdriver.Chrome()
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
        print('hello')
        browser = webdriver.Chrome()
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
        path = r"c:\Users\{}\Desktop\collected_pics".format(os.getlogin())
        with open('{}\{}.png'.format(path, uid), 'wb') as file:
            img_src = browser.find_element_by_xpath('//*[@id="Imagestudent"]').get_attribute("src")
            browser.get(img_src)
            
            pic_ = browser.find_element_by_xpath('/html/body/img')
            
            file.write(pic_.screenshot_as_png)
        browser.quit()

            

#kcg_student.student_login('311020104013', '25112002')
#kcg_student.get_photo(path = os.getcwd(), uid = user_id_)
#kcg_student.fees_login('20cs008')
#print(kcg_student.get_name('20cs008'))


