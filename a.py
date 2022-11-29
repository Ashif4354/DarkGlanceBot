departments = {
            'ad' : ('ad', 'aids',) , 
            'ae' : ('ae', 'aero',) ,
            'ao' : ('ao', 'aerospace', 'ase') ,
            'at' : ('at', 'auto', 'automobile') ,
            'ce' : ('ce', 'civil',) ,
            'cs' : ('cs', 'cse',),
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

fees_login_payload['txtuname'] = '20cs008'
    
    page = requests.post('http://studentonlinepayment.kcgcollege.ac.in/', data = fees_login_payload)
    if page.url != 'http://studentonlinepayment.kcgcollege.ac.in/':
        return True






















"""
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


login_button = browser.find_element_by_xpath('//*[@id="pBodypersonal"]/center').screenshot('image.png')


#time.sleep(2)
#browser.save_screenshot("image.png")
"""