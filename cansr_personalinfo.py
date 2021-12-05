

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Create an instance for chrome webdriver
driver = webdriver.Chrome()

# KEY POINT: The driver.get method will navigate to a page given by the URL
driver.get('https://www.cansrdev.com/clinical/login?logout')

if(driver.title=="Cansr | Login"):
    print ("Success: Qxf2 Tutorial page launched successfully")
else:
    print ("Failed: Qxf2 Tutorial page Title is incorrect") 
time.sleep(2)


# Find the username field using xpath with id
username = driver.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
username.send_keys('abbie1hobbs@yopmail.com')
time.sleep(1)


# Find the firstname field using xpath with id
password = driver.find_element_by_xpath("//input[@id='inp_password']")
# KEY POINT: Send text to an element using send_keys method
password.send_keys('Abbieh@1')
time.sleep(1)

# Find the phone no field using id
login = driver.find_element_by_xpath("//button[text()='Login']")

login.click()
time.sleep(5)


#find the purchase field using xpath 
cont_register = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")

cont_register.click()
time.sleep(5)

personal_info = driver.find_element_by_xpath("//a[@id='steps-uid-0-t-0']")
personal_info.click()
time.sleep(1)

# KEY POINT: Identify the dropdown and click on it
dropdown_title = driver.find_element_by_xpath("//select[@id='pr_title']")
  
dropdown_title.send_keys('Mrs.')
#dropdown_title.click()
# Sleep is one way to pause while the page elements load
time.sleep(1)

# KEY POINT: Identify the dropdown and click on it
dropdown_gender = driver.find_element_by_xpath("//select[@id='pr_gender']")
  
dropdown_gender.send_keys('Female')
time.sleep(1)

save_exit = driver.find_element_by_xpath("//button[contains(text(),'Save & Exit')]")
save_exit.click()
time.sleep(1)

confirmation = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]")
time.sleep(3)
confirmation.send_keys('Yes')

driver.close()

#next = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
#next.click()
#time.sleep(1)











