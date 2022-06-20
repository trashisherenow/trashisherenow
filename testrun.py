from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get('https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail%26rlz%3D1C1VDKB_enIN998IN999%26oq%3Dgmail%26aqs%3Dchrome..69i57j0i271l2j69i61l2j69i65.5171j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
username=driver.find_element_by_id('identifierId')
username.send_keys('alphax5m')
sleep(3)
nextbutton=driver.find_element_by_id('//*[@id="identifierNext"]/div/button/div[3]')
sleep(2)
nextbutton.submit
sleep(3)
password=driver.find_element_by_id('Enter your password')
password.send_keys('6$#prime')
sleep(3)
signinbutton=driver.find_element_by_id('passwordNext')
sleep(1)
signinbutton.click
