# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
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
current_URL = 'https://forms.gle/4VcYwfgqCPH7D7w49'

 
# Data
LinkFile = "list2.txt"
f = open(LinkFile,  mode="r",encoding="utf-8")
#datas = ['']


# Iterate through each data
for data in f:
    driver.get(current_URL)
    split_text = data.split(';')    
    # wait for one second, until page gets fully loaded
    time.sleep(2)
    
    # contain input boxes
    textboxes = driver.find_element(By.CSS_SELECTOR,'input[type="text"]')
    textboxes.send_keys(split_text[0])
    time.sleep(0.5)
    textboxes = driver.find_element(By.CSS_SELECTOR,"textarea[class='KHxj8b tL9Q4c']")
    textboxes.send_keys(split_text[1])
    time.sleep(0.5)    
    #radio box
    rad = driver.find_element(By.XPATH,'//*[@id="i16"]')
    rad.click()
    time.sleep(0.3)
    rad = driver.find_element(By.XPATH,'//*[@id="i27"]')
    rad.click()
    time.sleep(0.3)
    rad = driver.find_element(By.XPATH,'//*[@id="i38"]')
    rad.click()    
    time.sleep(0.4)
    rad = driver.find_element(By.XPATH,'//*[@id="i49"]')
    rad.click()    
    time.sleep(0.4)
    rad = driver.find_element(By.XPATH,'//*[@id="i60"]')
    rad.click()
    time.sleep(0.3)
    rad = driver.find_element(By.XPATH,'//*[@id="i71"]')
    rad.click()    
    time.sleep(0.3)
    rad = driver.find_element(By.XPATH,'//*[@id="i82"]')
    rad.click()    
    time.sleep(0.4)
    rad = driver.find_element(By.XPATH,'//*[@id="i93"]')
    rad.click()
    time.sleep(0.3)
    # click on submit button
    submit = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    
    print(data)
    SleepTime=random.randint(2,5)
    time.sleep(SleepTime)
 
    # fill another response
    #another_response = driver.find_element(By.LINK_TEXT, 'Submit another response')
    #another_response.click()

f.close()
# close the window
driver.close()