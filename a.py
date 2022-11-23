from selenium import webdriver
import time
user_id_ = None
browser = None
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options = options)
browser.get('http://studentlogin.kcgcollege.ac.in/')

user_id = '20cs008'
user_dob = '25112002'

user__id = browser.find_element_by_xpath('//*[@id="txtuname"]')
user__id.send_keys(user_id)

dob = browser.find_element_by_xpath('//*[@id="txtpassword"]')
dob.send_keys(user_dob)

login_button = browser.find_element_by_xpath('//*[@id="Button1"]')
login_button.click()

######
login_button = browser.find_element_by_xpath('//*[@id="pHeaderpersonal"]')
login_button.click()

time.sleep(1)
login_button = browser.find_element_by_xpath('//*[@id="ImageButtonbio"]')
login_button.click()

browser.execute_script("window.scrollTo(0, 450)") 


login_button = browser.find_element_by_xpath('//*[@id="Fpspersonal_viewport"]').screenshot('image.png')


#time.sleep(2)
#browser.save_screenshot("image.png")