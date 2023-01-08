#Script để tải truyện từ truyen35
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_truyen35.txt
#Version: 1.0
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
strURLStory='https://truyen35nb.com/[ten-truyen]/chuong-'
StartChapter=X #So chuong bat dau
EndChapter=Y #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua_truyen35.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'    
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
    response=scraper.get(ChapterURL)
    filenameHTML =str(x)+".html"  
    bCheckLink=0
    open(filenameHTML, 'wb').write(response.content)
    with open(filenameHTML, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp,"lxml")
        try:
            #Luu tieu de
            StrippedContent = ""
            for title in soup.find_all('title'):
                downloaded  =   title.get_text()
                break
            StrippedContent = "\n"+ downloaded
            
            #Lay noi dung chuong
            div= soup.find(id="js-truyenkk-read-content")             
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
        if(os.path.exists(filenameHTML)):
            os.remove(filenameHTML)
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(10, 15)
    time.sleep(SleepTime)

print('Hoan tat!')
