#Script để tải truyện từ wikidich
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt

from bs4 import BeautifulSoup
import cfscrape
import fileinput
import random
import time
import os
import array as arr


LinkFile = "link.txt" #file chua link tap hop chuong truyen
filenameTXT ="Ketqua.txt"
chapter = 0
f = open(LinkFile, "r")
for x in f:   
    if "http" in x:
        StrippedContent=""
        ChapterURL=x
        scraper = cfscrape.CloudflareScraper()
        response= scraper.get(ChapterURL)
        filenameHTML =str(chapter)+".html"  
        bCheckLink=0
        open(filenameHTML, 'wb').write(response.content)
        with open(filenameHTML, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp,"lxml")
            try:        
                #Luu tieu de  
                downloaded = soup.title.string
                StrippedContent="\n"+ downloaded+"\n"                
                
                #Lay noi dung chuong
                div= soup.find(id="bookContentBody")             
                for elem in div.find_all("p"):
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
        SleepTime=random.randint(1, 5)
        time.sleep(SleepTime)
f.close()
print('Hoan tat!')
