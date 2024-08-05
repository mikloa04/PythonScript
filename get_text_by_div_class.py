#Script để tải truyện từ các website truyen
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Version: 1.0.2
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

LinkFile = "link2.txt"
filenameTXT ='NL-lo-thuoc-tang-hinh-33.txt' #"Ketqua2.txt"
filelog ="log2.txt"
chapter = 0
source_dict = {
    'foxaholic': 'reading-content', 
    'mtlreader': 'chapter-content', 
    'ttv': 'box-chap',
    'xianqihaotianmi': 'panel-body content-body content-ext',
    'shuhaige': 'content',
    'truyensex': 'ndtruyen',
    
}
#change key to set class value
_key = ''
_val = ''
f = open(LinkFile, "r")
#init Chrome webdriver --headless -disable logging
options = webdriver.ChromeOptions()
chrome_install = ChromeDriverManager().install()
folder = os.path.dirname(chrome_install)
chromedriver_path = os.path.join(folder, "chromedriver.exe")
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('log-level=3')
driver = webdriver.Chrome(service=ChromeService(chromedriver_path), options=options)
driver.implicitly_wait(0.5)
retry = 0
for x in f:
    if "http" in x:
        bCheckLink=0
        StrippedContent=""
        downloaded=""
        ChapterURL=x
        filenameHTML =str(chapter)+".html"
        if _key == '':
            for key in source_dict.keys():
                if key in ChapterURL:
                    _key = key
                    _val = source_dict[_key]
                    break
            if _key == '' and _val == '':
                print('This host is not supported yet!')
                break
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
                    #downloaded = soup.title.string
                    #StrippedContent= downloaded+"\n"                
                    
                    #Lay noi dung chuong
                    div= soup.find('div', class_=_val)
                    for elem in div.find_all("p"):
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
        SleepTime=random.randint(1, 3)
        time.sleep(SleepTime)
driver.quit()
f.close()

print('Finished!')
