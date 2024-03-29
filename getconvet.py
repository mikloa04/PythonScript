#Script để tải truyện từ truyenconvet
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Dung module cfscrape, cai dat bang cau lenh: pip install cfscrape

from bs4 import BeautifulSoup
import cfscrape
import fileinput
import random
import time
import os
import array as arr


LinkFile = "link_convet.txt"
filenameTXT ="Ketqua_convet.txt"
filelog ="log_convet.txt"
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
            downloaded=''
            try:        
                #Luu tieu de  
                downloaded = soup.find('h1', {'id': 'chapter-heading'}).text                
                StrippedContent="\n"+ downloaded+"\n"                
                
                #Lay noi dung chuong
                div= soup.find('div', class_='reading-content')             
                          
                for elem in div.find_all("p"):
                    elem.replace_with(elem.text + "\n\n") 
                _text = div.text
                #Luu Noi dung chuong
                StrippedContent="\n"+StrippedContent+"\n"+_text+"\n"
                bCheckLink=1
            except:

                bCheckLink=0
        if bCheckLink==1:  
            with open(filenameTXT, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
        else:
            StrippedContent = 'Error download '+ChapterURL+'\n'
            with open(filelog, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
        if(os.path.exists(filenameHTML)):
            os.remove(filenameHTML)
        print('Downloaded: ('+downloaded+')' )    
        chapter+=1             
        #Tam dung mot chut    
        SleepTime=random.randint(5, 10)
        time.sleep(SleepTime)
f.close()
print('Finished!')
