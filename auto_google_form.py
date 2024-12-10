# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
 
# open Chrome
options = webdriver.ChromeOptions()
chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
#options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('log-level=3')
driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)
driver.implicitly_wait(0.5)

# Open URL
current_URL = 'https://docs.google.com/forms/d/e/~/viewform'

 
# Data
LinkFile = "list.txt"
f = open(LinkFile, "r")
#datas = ['']


# Iterate through each data
for data in f:
    driver.get(current_URL)
    # wait for one second, until page gets fully loaded
    time.sleep(1)
 
    # contain input boxes
    textboxes = driver.find_element(By.CSS_SELECTOR,'input[type="email"]')
    textboxes.send_keys(data)
    
    #radio box
    rad = driver.find_element(By.XPATH,'//*[@id="i10"]')
    rad.click()
 
    # click on submit button
    submit = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    
    time.sleep(5)
 
    # fill another response
    #another_response = driver.find_element(By.LINK_TEXT, 'Submit another response')
    #another_response.click()
 
# close the window
driver.close()
