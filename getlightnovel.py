#Script để tải truyện từ lightnovelpub.com
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_lnp.txt
#Version: 2.0
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
strURLStory = 'https://www.lightnovelpub.com/novel/name/chapter-'
StartChapter = 1 #So chuong bat dau
EndChapter = 200 #So chuong ket thuc
x = StartChapter    
filenameTXT  = "Ketqua_lnp.txt"

while (x <=  EndChapter):
    StrippedContent = ""
    ChapterURL = strURLStory+str(x)+'/'    
    scraper  =  cloudscraper.create_scraper(browser = {'browser': 'firefox','platform': 'windows','mobile': False})
    response = scraper.get(ChapterURL)
    filenameHTML  = str(x)+".html"  
    bCheckLink = 0
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML, encoding = "utf-8") as fp:
        soup  =  BeautifulSoup(fp,"lxml")
        try:        
            #Luu tieu de  
            StrippedContent = "\n"
            for title in soup.find_all('title'):
                downloaded  =   title.get_text()
                break
            StrippedContent = "\n"+ downloaded+"\n"                
            
            #Lay noi dung chuong
            div =  soup.find(id = "chapter-container")             
            #Loai bo tag br
            for elem in div.find_all("p"):
                elem.replace_with(elem.text + "\n")
              
            #Luu Noi dung chuong
            StrippedContent = "\n"+StrippedContent+"\n"+div.text+"\n"
            bCheckLink = 1
            
        except:
            print('Khong ton tai Chuong: '+str(x))
            bCheckLink = 0
    if bCheckLink == 1:  
        with open(filenameTXT, 'a', encoding = "utf-8") as handle:    
            handle.write(StrippedContent)
        os.remove(filenameHTML)     
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x += 1             
    #Tam dung mot chut    
    SleepTime = random.randint(10, 15)
    time.sleep(SleepTime)

print('Hoan tat!')
