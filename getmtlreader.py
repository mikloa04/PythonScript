#Script để tải truyện từ mtlreader.com
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_novelhall.txt
#Version: 2.0
#Bỏ qua DDOS protection
#Dung module cfscrape, cai dat bang cau lenh: pip install cfscrape

from bs4 import BeautifulSoup
import cloudscraper
import fileinput
import random
import time
import os
import array as arr


LinkFile = "mtlreader_link.txt"
filenameTXT ="Ketqua_mtlreader.txt"
chapter = 0
f = open(LinkFile, "r")
for x in f:   
    if "http" in x:
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
                   break
                StrippedContent="\n"+ downloaded+"\n"                
                
                #Lay noi dung chuong
                div= soup.find('div', class_='chapter-content')             
                          
                for elem in div.find_all("<br><br>"):
                    elem.replace_with(elem.text + "\n\n") 
                _text = div.text
                #Luu Noi dung chuong
                StrippedContent="\n"+StrippedContent+"\n"+_text+"\n"
                bCheckLink=1
                
            except:
                print('Khong ton tai Chuong: '+str(x))
                bCheckLink=0
        if bCheckLink==1:  
            with open(filenameTXT, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
            os.remove(filenameHTML)     
        print('Da tai ('+downloaded+')' )    
        chapter+=1             
        #Tam dung mot chut    
        SleepTime=random.randint(5, 10)
        time.sleep(SleepTime)
f.close()
print('Hoan tat!')