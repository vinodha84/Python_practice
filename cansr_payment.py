

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

# Find the usernam field using xpath with id
username = driver.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
username.send_keys('abbie1hobbs@yopmail.com')
time.sleep(3)

# Find the password field using xpath with id
password = driver.find_element_by_xpath("//input[@id='inp_password']")
# KEY POINT: Send text to an element using send_keys method
password.send_keys('Abbieh@1')
time.sleep(3)

# Find the phone no field using id
login = driver.find_element_by_xpath("//button[text()='Login']")
login.click()
time.sleep(5)



#find the continue field using xpath with id
cont = driver.find_element_by_xpath("//u[contains(text(),'Click here to continue')]")
# KEY POINT: Send text to an element using send_keys method
cont.click()
time.sleep(10)

#find the purchase field using xpath with id
purchase = driver.find_element_by_xpath("//a[@id='PKGCOS001']")
# KEY POINT: Send text to an element using send_keys method
purchase.click()
time.sleep(5)

#find the consent field using xpath with id
consent = driver.find_element_by_xpath("//input[@id='consentCheckBox']")
# KEY POINT: Send text to an element using send_keys method
consent.click()
time.sleep(5)

#find the submit field using xpath with id
agree = driver.find_element_by_xpath("//button[@id='agreeConsentId']")
# KEY POINT: Send text to an element using send_keys method
agree.click()
time.sleep(5)

#find the Registerfield using xpath with id
cardnumber= driver.find_element_by_xpath("//input[@id='cardNumber']")
cardnumber.send_keys(4242424242424242)
time.sleep(3)

#find the expiry month using xpath with id
month = driver.find_element_by_xpath("//select[@id='expiryMonth']")
month.send_keys('February')
time.sleep(0.8)

#find the expiry year using xpath with id
year = driver.find_element_by_xpath("//select[@id='expiryYear']")
year.send_keys(2022)
time.sleep(0.8)

#find the security code using xpath with id
code = driver.find_element_by_xpath("//input[@id='securityCode']")
code.send_keys(345)
time.sleep(0.8)


#find the address1 using xpath with id
address1 = driver.find_element_by_xpath("//input[@id='cardHolderBilAddr1']")
address1.send_keys(24)

address2 = driver.find_element_by_xpath("//input[@id='cardHolderBilAddr2']")
address2.send_keys('stroude road')
time.sleep(0.8)

#find the country using xpath with id
country = driver.find_element_by_xpath("//select[@id='countryId']")
country.send_keys('United kingdom')
time.sleep(0.8)

#find the post code using xpath with id
postcode = driver.find_element_by_xpath("//input[@id='billingPostCode']")
postcode.send_keys('KW174RW')
time.sleep(0.8)


# find the confirm using xpath with id
confirm = driver.find_element_by_xpath("//a[@id='confirmPaymentId']")
confirm.click()
time.sleep(0.8)

#find the agree and continue using xpath
agree = driver.find_element_by_xpath("//button[@id='payNowButtonId']")
agree.click()
time.click(1)

# find the continue to register using xpath
cont = driver.find_element_by_xpath("//a[contains(text(),'Continue to Registration')]")
cont.click()
time.click(2)

#driver.close()





