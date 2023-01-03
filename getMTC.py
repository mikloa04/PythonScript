#Script để tải truyện từ Metruyencv
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_mtc.txt
#Version: 2.0
#Dung module playwright, pip install playwright, pip install playwright -U
#playwright install
#pip install lxml
#pip install bs4

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import fileinput
import random
import time
import os
import array as arr

#Duong dan den chuong truyen
strURLStory='https://metruyencv.com/truyen/[ten-truyen]/chuong-'
StartChapter=0 #So chuong bat dau
EndChapter=999 #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua_mtc.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'   
    filenameHTML =str(x)+".html"      
    bCheckLink=0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(ChapterURL)        
        soup = BeautifulSoup(page.content(),"html.parser")
        try:        
            #Luu tieu de  
            StrippedContent="\n"
            for each_div in soup.findAll('div',{'class':'h1 mb-4 font-weight-normal nh-read__title'}):
                StrippedContent="\n"+StrippedContent+"\n"+each_div.text+"\n"
            
            #Lay noi dung chuong
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
        browser.close()
    if bCheckLink==1:  
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)        
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(5, 10)
    time.sleep(SleepTime)

print('Hoan tat!')
