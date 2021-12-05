

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

cont_register = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
cont_register.click()
time.sleep(5)

next = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(1)

# Find the communication field using xpath with id
communication = driver.find_element_by_xpath("//a[@id='steps-uid-0-t-1']")

communication.click()
time.sleep(5)

# Find the address field using xpath with id
address = driver.find_element_by_xpath("//input[@id='pr_firstline']")
# KEY POINT: Send text to an element using send_keys method
address.send_keys('24 stroude road')
time.sleep(1)

#town/city
town= driver.find_element_by_xpath("//input[@id='pr_countrydist']")
town.send_keys('Skaill')
time.sleep(3)

#zipcode
#zipcode=driver.find_element_by_xpath("//input[@id='pr_postcode']")
#zipcode.send_keys('KW174RW')
#time.sleep(4)

#country
country = driver.find_element_by_xpath("//select[@id='pr_country']")
country.send_keys('United Kingdom')
time.sleep(3)

country_code = driver.find_element_by_xpath("//select[@id='country_code']")
country_code.send_keys('+44')
time.sleep(3)

country_code = driver.find_element_by_xpath("//input[@id='pr_mobile']")
country_code.send_keys('077 4023 3434')
time.sleep(3)

next = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)












