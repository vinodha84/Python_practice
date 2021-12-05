

import time
#from captcha.image import ImageCaptcha
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


signup = driver.find_element_by_xpath("//a[contains(text(),'Sign Up')]")
# KEY POINT: Send text to an element using send_keys method
signup.click()

# Find the firstname field using xpath with id
firstname = driver.find_element_by_xpath("//input[@id='inp_firstName']")
# KEY POINT: Send text to an element using send_keys method
firstname.send_keys('Abbie')

# Find the lastname field using xpath with id
Lastname = driver.find_element_by_xpath("//input[@id='inp_LastName']")
# KEY POINT: Send text to an element using send_keys method
Lastname.send_keys('Hobbs')

# Find the email field using xpath with id
email = driver.find_element_by_xpath("//input[@id='email']")
# KEY POINT: Send text to an element using send_keys method
email.send_keys('abbie1hobbs@yopmail.com')

#find the postcode field using xpath with id
postcode = driver.find_element_by_xpath("//input[@id='postcode']")
#Key point : send text to an element using send_keys method
postcode.send_keys('KW174RW')

#find the date field using xpath with id
date = driver.find_element_by_xpath("//select[@id='dobDate']")
#Key point : send text to an element using send_keys method
date.send_keys('8')


#find the month field using xpath with id
month = driver.find_element_by_xpath("//select[@id='dobMonth']")
#Key point : send text to an element using send_keys method
month.send_keys('November')


#find the year field using xpath with id
year = driver.find_element_by_xpath("//select[@id='dobYear']")
#Key point : send text to an element using send_keys method
year.send_keys('1964')

#find the cache field using xpath with id
captcha = driver.find_element_by_xpath("//input[@id='txtInput']")
#Key point : send text to an element using send_keys method
#captcha.send_keys('uAtr')
time.sleep(20)

# KEY POINT: Locate the checkbox and click on it
checkbox = driver.find_element_by_xpath("//input[@id='signup-consent']")
checkbox.click()

time.sleep(10)

submit = driver.find_element_by_xpath("//button[@id='SignupBut_signup']")
submit.click()

time.sleep(3)

# Close the browser window
driver.close() 
 

















