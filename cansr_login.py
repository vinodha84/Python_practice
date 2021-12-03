
from selenium import webdriver

# Create an instance for chrome webdriver
browser = webdriver.Chrome()

# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('https://www.cansrdev.com/clinical/login?logout')

if(browser.title=="Cansr | Login"):
    print ("Success: Qxf2 Tutorial page launched successfully")
else:
    print ("Failed: Qxf2 Tutorial page Title is incorrect") 

# Quit the browser window
browser.quit()
