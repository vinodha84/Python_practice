

import time
from selenium import webdriver

from selenium.webdriver import ActionChains

#create instance for chrome browser
driver = webdriver.Chrome()


# browser.get to navigate to page
driver.maximize_window()
driver.get('https://www.cansrdev.com/clinical/dashboard/')

#verify title of the page
if(driver.title=="Cansr | Login"):
    print("Success: Cansr page logged")
else:
    print("Failed: Cansr page cannot be opened") 
time.sleep(2)
#find email path using xpath
email=driver.find_element_by_xpath("//input[@id='inp_loginid']")

#send text to element 
email.send_keys('abbie1hobbs@yopmail.com')

#find password element using xpath
password=driver.find_element_by_xpath("//input[@id='inp_password']")

password.send_keys('Abbieh@1')
time.sleep(3)


#select login button
login = driver.find_element_by_xpath("//button[text()='Login']")
login.click()
time.sleep(5)

#my account
account=driver.find_element_by_xpath("//a[@id='newmyProfileLink-old']")
time.sleep(3)
account.click()

#click registration
cont_register=driver.find_element_by_xpath("//a[@id='newmyProfileLinkRenamed']")
cont_register.click()
time.sleep(3)

next = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)

#information 3/4
cansr_info=driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/section[3]/div[1]/div[1]/ul[1]/li[3]")
cansr_info.click()
time.sleep(3)

prev_cansr=driver.find_element_by_xpath("//input[@id='no_cancer']")
prev_cansr.click()
time.sleep(3)

family_q7=driver.find_element_by_xpath("//input[@id='no_cancer_relative']")
family_q7.click()
time.sleep(3)

family_q8=driver.find_element_by_xpath("//input[@id='no_cancer_other']")
family_q8.click()
time.sleep(3)

next=driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)








