import requests
import os
from selenium import webdriver
import time

user_id_ = None
browser = None
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

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
        marks_detail_button = browser.find_element_by_xpath('//*[@id="pHeaderpersonal"]')
        marks_detail_button.click()

        time.sleep(2)
        cam_button = browser.find_element_by_xpath('//*[@id="ImageButtonbio"]')
        cam_button.click()

        browser.execute_script("window.scrollTo(0, 450)") 
        
        path = r"c:\Users\{}\Desktop\collected_pics".format(os.getlogin())
        marks_table = browser.find_element_by_xpath('//*[@id="Fpspersonal_viewport"]')
        marks_table.screenshot('{}\{}_details.png'.format(path, uid))
        browser.quit()

            

#student.student_login('311020104013', '25112002')
#student.get_photo(path = os.getcwd(), uid = user_id_)
#student.fees_login('20cs008')
#print(student.get_name('20cs008'))
#student.get_marks(uid = user_id_)


