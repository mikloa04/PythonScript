#Script để tải truyện từ drxsw
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_uutxt.txt
#Version: 1.0.0
#Dung module selenium, pip install selenium, pip install selenium -U

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import codecs
import fileinput
import random
import time
import os
import array as arr

LinkFile = "link_drxsw.txt"
filenameTXT ="Ketqua_drxsw.txt"
filelog ="log_uutxt.txt"
chapter = 0
f = open(LinkFile, "r")
#init Chrome webdriver --headless -disable logging
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('log-level=3')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(0.5)
retry = 0
for x in f:   
    if "http" in x:
        bCheckLink=0
        StrippedContent=""
        downloaded=""
        ChapterURL=x
        filenameHTML =str(chapter)+".html"         
        try:    
            #Get content from url, save as html file
            driver.get(ChapterURL)
            h = driver.page_source
            source = codecs.open(filenameHTML, "w", "utf−8")
            source.write(h)
            source.close()
            #Lấy text từ file html và lưu vào file Ketqua_uutxt           
            with open(filenameHTML, encoding="utf-8") as fp:
                soup = BeautifulSoup(fp,"lxml")
                try:        
                    #Luu tieu de  
                    downloaded = soup.title.string
                    StrippedContent= downloaded+"\n"                
                    
                    #Lay noi dung chuong
                    div= soup.find(id="TextContent")             
                    for elem in div.find_all("br"):
                        elem.replace_with(elem.text + "\n") 
                    _text = div.text
                    #Luu Noi dung chuong
                    StrippedContent="\n"+StrippedContent+"\n"+_text+"\n"
                    bCheckLink=1                    
                except:
                    bCheckLink=0
        except:
            bCheckLink=0
        
        if bCheckLink==1:  
            with open(filenameTXT, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
            chapter+=1
            retry = 0
            print('Downloaded: '+ChapterURL)
        else:
            retry += 1
            if (retry == 4):
                StrippedContent = 'Error download '+ChapterURL+'\n'
                with open(filelog, 'a', encoding="utf-8") as handle:    
                    handle.write(StrippedContent)
                chapter+=1
                retry = 0
                print('Error Downloaded!' )
        if(os.path.exists(filenameHTML)):
            os.remove(filenameHTML)

        #Tam dung mot chut    
        SleepTime=random.randint(5, 10)
        time.sleep(SleepTime)
driver.quit()
f.close()

print('Finished!')