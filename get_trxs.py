#Script để tải truyện từ trxs
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_trxs.txt
#Version: 1.0.1
#Dung module cloudscraper, pip install cloudscraper, pip install cloudscraper -U
#pip install lxml
#pip install bs4

from bs4 import BeautifulSoup
import cloudscraper
import fileinput
import random
import time
import os
import array as arr

#Duong dan den chuong truyen
strURLStory='https://www.trxs.cc/tongren/7522/'
StartChapter=74 #So chuong bat dau
EndChapter=368 #So chuong ket thuc >>701


x=StartChapter    
filenameTXT ="Ketqua_trxs.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+".html"  
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
    response=scraper.get(ChapterURL)
    filenameHTML = str(x)+".html"  
    bCheckLink=0
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML) as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:
            #Luu tieu de
            StrippedContent = ""
           
            #Lay noi dung chuong
            div= soup.find(id="readContent_set")             
            #Loai bo tag p
            for elem in div.find_all("p"):
                elem.replace_with(elem.text + "\n")
              
            #Luu Noi dung chuong
            StrippedContent=div.text+"\n"
            bCheckLink=1
            
        except:
            print('Khong ton tai Chuong: '+str(x))
            bCheckLink=0
    if bCheckLink==1:  
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
    if(os.path.exists(filenameHTML)):
        os.remove(filenameHTML)
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(10, 15)
    time.sleep(SleepTime)

print('Hoan tat!')
