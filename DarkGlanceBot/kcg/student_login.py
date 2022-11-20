from selenium import webdriver
import requests
import os

options = None
driver = None
user_id_ = None

class kcg_student:
    def open_browser():
        global options, driver
        options = webdriver.ChromeOptions()
        #options.headless = True
        driver = webdriver.Chrome(options=options)
    
    def close_browser():
        driver.quit()

    def login(user_id, user_dob):

        global user_id_
        user_id_ = user_id #simply

        kcg_student.open_browser()
        driver.get('http://studentlogin.kcgcollege.ac.in/')

        #login with register no
        if user_id[:4] == '3110':               
            register_no_button = driver.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[2]')
            register_no_button.click()


        #login with roll no
        else:                          
            roll_no_button = driver.find_element_by_xpath('//*[@id="rblOnlineAppLoginMode"]/option[1]') 
            roll_no_button.click()

        #roll/register no. input
        user__id = driver.find_element_by_xpath('//*[@id="txtuname"]')
        user__id.send_keys(user_id)

        dob = driver.find_element_by_xpath('//*[@id="txtpassword"]')
        dob.send_keys(user_dob)

        login_button = driver.find_element_by_xpath('//*[@id="Button1"]')
        login_button.click()
    
    def get_photo(path = os.getcwd(), uid = user_id_): 
        path = path + '\collected_pics'
        with open('{}\{}.png'.format(path, uid), 'wb') as file:
            img_src = driver.find_element_by_xpath('//*[@id="Imagestudent"]').get_attribute("src")

            driver.get(img_src)
            
            pic_ = driver.find_element_by_xpath('/html/body/img')
            
            file.write(pic_.screenshot_as_png)
        driver.quit()
            

#kcg_student.login('311020104013', '25112002')
#kcg_student.get_photo(path = os.getcwd(), uid = user_id_)


