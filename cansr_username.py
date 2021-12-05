
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

# Find the name field using xpath with id
name = driver.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
name.send_keys('noahmartin25@yopmail.com')

# Find the email field using xpath without id
password = driver.find_element_by_xpath("//input[@id='inp_password']")
password.send_keys('Noahmartin@25')
time.sleep(5)

# Find the phone no field using id
login = driver.find_element_by_xpath("//button[text()='Login']")


login.click()

#submit=driver.find_element_by_xpath("//body/div[@id='main-wrapper']/div[1]/div[2]/p[1]")
#submit.click()  


# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close() 
 



