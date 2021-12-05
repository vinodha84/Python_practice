
import time
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

password = driver.find_element_by_xpath("//a[contains(text(),'Forgot Password / Email')]")
# KEY POINT: Send text to an element using send_keys method
password.click()

# Find the email field using xpath with id
email = driver.find_element_by_xpath("//input[@id='inp_emailid']")
# KEY POINT: Send text to an element using send_keys method
email.send_keys('abbiehobbs@yopmail.com')
time.sleep(5)

#find the continue field using xpath with id
cont = driver.find_element_by_xpath("//button[contains(text(),'Continue')]")
# KEY POINT: Send text to an element using send_keys method
cont.click()

# Verify user is taken to Qxf2 tutorial redirect url
#if (driver.cont==("//button[contains(text(),'Continue']")):
    #driver.cont.click()
#else:
    #driver.login ==("//a[contains(text(),'Log In')]")
    #driver.login.click()



