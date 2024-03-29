#Script để tải truyện từ truyendam.org, tuoinung.com
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Version: 2.0
#Bỏ qua DDOS protection
#Dung module cfscrape, cai dat bang cau lenh: pip install cfscrape, pip install -U cfscrape
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
strURLStory='https://truyendam.org/ten-truyen/'
StartChapter=1 #So chuong bat dau
EndChapter=N #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'    
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
    response=scraper.get(ChapterURL)
    filenameHTML =str(x)+".html"  
    bCheckLink=0
    StrippedContent=""
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:                   
            #Extract Title               
            if x == StartChapter :
                downloaded = soup.title.string
                StrippedContent = downloaded +"\n"
            #Extract content
            for data in soup.find_all("p"):
                StrippedContent = StrippedContent + "\n" + data.get_text() + "\n"                        
            bCheckLink=1
            
        except:
            print('Khong ton tai Chuong: '+str(x))
            bCheckLink=0
    if bCheckLink==1:  
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
        os.remove(filenameHTML)     
    print('Downloaded ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(1, 3)
    time.sleep(SleepTime)

print('Finished!')
