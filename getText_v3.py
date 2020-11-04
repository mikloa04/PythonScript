#Script để tải truyện từ Truyencv
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Version: 2.0
#Bỏ qua DDOS protection
#Dung module cfscrape, cai dat bang cau lenh: pip install cfscrape

from bs4 import BeautifulSoup
import cfscrape
import fileinput
import random
import time
import os
import array as arr

#Duong dan den chuong truyen
strURLStory='https://metruyenchu.com/truyen/van-co-de-nhat-con-re/chuong-'
StartChapter=1 #So chuong bat dau
EndChapter=100 #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'    
    scraper = cfscrape.CloudflareScraper()
    response=scraper.get(ChapterURL)
    filenameHTML =str(x)+".html"  
    bCheckLink=0
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:        
            #Luu tieu de  
            StrippedContent="\n"+ soup.title.string+"\n"
            div= soup.find(id="js-read__content")             
              
            #Loai bo tag br
            for elem in div.find_all("br"):
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
        os.remove(filenameHTML)     
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(10, 15)
    time.sleep(SleepTime)

print('Hoan tat!')
