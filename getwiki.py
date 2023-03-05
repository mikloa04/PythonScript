#Script để tải truyện từ wikidich
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Version: 3.0
#Bỏ qua DDOS protection
#Dung module cfscrape, cai dat bang cau lenh: pip install cfscrape
#Dung module cloudscraper, pip install cloudscraper, pip install cloudscraper -U

from bs4 import BeautifulSoup
import cfscrape
import fileinput
import random
import time
import os
import array as arr


LinkFile = "link.txt"
filenameTXT ="Ketqua_wiki.txt"
filelog ="log_wiki.txt"
chapter = 0
f = open(LinkFile, "r")
for x in f:   
    if "http" in x:
        StrippedContent=""
        ChapterURL=x
        scraper = cfscrape.create_scraper(delay=15)
        response= scraper.get(ChapterURL)
        filenameHTML =str(chapter)+".html"  
        bCheckLink=0
        open(filenameHTML, 'wb').write(response.content)
        with open(filenameHTML, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp,"lxml")
            try:        
                #Save title  
                downloaded = soup.title.string
                StrippedContent="\n"+ downloaded+"\n"                
                
                #Get content
                div= soup.find(id="bookContentBody")             
                for elem in div.find_all("p"):
                    elem.replace_with(elem.text + "\n\n") 
                _text = div.text
                #Save content
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
        #Waiting time    
        SleepTime=10
        time.sleep(SleepTime)
f.close()
print('Finished!')
