#Script để tải truyện từ Truyenyy
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_yy.txt
#Version: 1.0.0
#Bỏ qua DDOS protection
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
strURLStory='https://truyenyy.vip/truyen/hokage-chi-uchiha-derin/chuong-'
StartChapter=1599 #So chuong bat dau
EndChapter=1812 #So chuong ket thuc
x=StartChapter    
filenameTXT ="hokage-chi-uchiha-derin-1812.txt"

while (x<= EndChapter):
    StrippedContent=""
    filenameHTML =str(x) + ".html"  
    ChapterURL= strURLStory + filenameHTML
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
    response=scraper.get(ChapterURL)   
    bCheckLink=0
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:        
            #Luu tieu de
            StrippedContent = ""
            for title in soup.find_all('title'):
                downloaded  =   title.get_text()
                break
            StrippedContent = "\n"+ downloaded+"\n"
            
            #Lay noi dung chuong
            div= soup.find(id="inner_chap_content_1")             
            #Loai bo tag br
            for elem in div.find_all("p"):
                elem.replace_with(elem.text + "\n")
              
            #Luu Noi dung chuong
            StrippedContent="\n"+StrippedContent+"\n"+div.text+"\n"
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