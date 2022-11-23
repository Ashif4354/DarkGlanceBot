login_button = browser.find_element_by_xpath('//*[@id="pHeadermarks"]')
login_button.click()

time.sleep(1)
login_button = browser.find_element_by_xpath('//*[@id="ImageButtonCamv"]')
login_button.click()

browser.execute_script("window.scrollTo(40, 500)") 


login_button = browser.find_element_by_xpath('//*[@id="Fpsmarks_viewport"]/table').screenshot('image.png')