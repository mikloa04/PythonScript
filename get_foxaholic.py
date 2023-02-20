#Script để tải truyện từ foxaholic
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_foxaholic.txt
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

LinkFile = "link_foxalic.txt"
filenameTXT ="Ketqua_foxalic.txt"
chapter = 0
f = open(LinkFile, "r")
for x in f:   
    if "https" in x:
        StrippedContent=""
        ChapterURL=x
        scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
        response=scraper.get(ChapterURL)
        filenameHTML =str(chapter)+".html"  
        bCheckLink=0        
        open(filenameHTML, 'wb').write(response.content)
        with open(filenameHTML, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp,"lxml")
            downloaded=''
            try:        
                #Luu tieu de  
                for title in soup.find_all('title'):
                   downloaded =  title.get_text()
                StrippedContent="\n"+ downloaded+"\n"                
                
                #Lay noi dung chuong
                div= soup.find('div', class_='reading-content')
                
                #Loai bo tag p
                for elem in div.find_all("p"):
                    elem.replace_with(elem.text + "\n")
                _text = div.text
                  
                #Luu Noi dung chuong
                StrippedContent="\n"+StrippedContent+"\n"+_text+"\n"
                bCheckLink=1
                
            except:
                print('Khong ton tai Chuong: '+str(downloaded))
                bCheckLink=0
        if bCheckLink==1:  
            with open(filenameTXT, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
        if(os.path.exists(filenameHTML)):
            os.remove(filenameHTML)
        print('Da tai ('+downloaded+')' )    
        chapter+=1             
        #Tam dung mot chut    
        SleepTime=random.randint(5, 10)
        time.sleep(SleepTime)
f.close()
print('Hoan tat!')
