

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
Registraion=driver.find_element_by_xpath("//a[@id='newmyProfileLinkRenamed']")
Registraion.click()
time.sleep(3)

#click next
next=driver.find_element_by_xpath("//a[@href='#next']")
next.click()
time.sleep(3)


#cansr info
cansr_info=driver.find_element_by_xpath("//a[@id='steps-uid-0-t-2']")
cansr_info.click()
time.sleep(3)

#cans/info(1/4)
infor =driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/section[3]/div[1]/div[1]/ul[1]/li[1]")
time.sleep(10)

#cans1
#cans1=driver.find_element_by_xpath("//li[contains(text(),'Please select your current cancer diagnosis')]")
#time.sleep(7)

#q1
dropdown_Q1=driver.find_element_by_xpath("//select[@id='SubType']")
dropdown_Q1.click()
dropdown_Q1.send_keys('Colon')
time.sleep(3)

#2question
#cans2=driver.find_element_by_xpath("//span[@id='cancer_display_with']")time.sleep(3)

#q2
q2=driver.find_element_by_xpath("//select[@id='diagnosedMonth']")
q2.send_keys('August')
time.sleep(1)

#year
year=driver.find_element_by_xpath("//select[@id='diagnosedYear']")
year.send_keys('1992')
time.sleep(1)

#cancer stage
stage_q3 = driver.find_element_by_xpath("//input[@id='no_cancer_stage']")
stage_q3.click()
time.sleep(3)

#colon cansr spread
colon_q4 = driver.find_element_by_xpath("//input[@id='no_cancer_spread']")
colon_q4.click()
time.sleep(3)

next = driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[3]/ul[1]/li[2]/a[1]")
next.click()
time.sleep(3)

#cans/info(2/4)
infor =driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/section[3]/div[1]/div[1]/ul[1]/li[2]")
time.sleep(5)

# current Treament
treatment_q5 = driver.find_element_by_xpath("//input[@id='yes_cancer_under']")
treatment_q5.click()
time.sleep(3)

















