#Script để tải truyện từ doctruyen69vn.net
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
strURLStory='https://truyensex.vip/{ten-truyen}/'
StartChapter=0 #So chuong bat dau
EndChapter=0 #So chuong ket thuc
x=StartChapter    
filenameTXT ="ket-qua.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'    
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
    response=scraper.get(ChapterURL)
    filenameHTML =str(x)+".html"  
    bCheckLink=0
    open(filenameHTML, 'wb').write(response.content)
    StrippedContent=""
    with open(filenameHTML, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:        
            #Extract content
            #for each_div in soup.findAll('div',{'class':'singular-post-content'}):
            for each_div in soup.findAll('div',{'class':'ndtruyen'}):
                StrippedContent="\n"+StrippedContent+"\n"+each_div.text+"\n"    
            bCheckLink=1
            
        except:
            print('Khong ton tai Chuong: '+str(x))
            bCheckLink=0
    if bCheckLink==1:  
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
        os.remove(filenameHTML)     
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(1, 3)
    time.sleep(SleepTime)

print('Hoan tat!')
