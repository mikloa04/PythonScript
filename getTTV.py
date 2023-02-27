#Script để tải truyện từ Tangthuvien
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt
#Version: 2.0
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
strURLStory='https://truyen.tangthuvien.vn/doc-truyen/{ten-truyen}/chuong-'
StartChapter=x #So chuong bat dau
EndChapter=y #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua_ttv.txt"
filelog ="log_ttv.txt"

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
            #Lay tieu de chuong
            for each_div in soup.findAll('a',{'class':'more-chap'}):
                StrippedContent="\n"+StrippedContent+"\n"+each_div.text+"\n"
                
            #Lay noi dung chuong
            for each_div in soup.findAll('div',{'class':'box-chap'}):
                StrippedContent="\n"+StrippedContent+"\n"+each_div.text+"\n"                       
              
            bCheckLink=1
            
        except:
            print('Khong ton tai Chuong: '+str(x))
            bCheckLink=0
    if bCheckLink==1:  
        #Luu Noi dung chuong
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
    else:
        StrippedContent = 'Error download '+ChapterURL+'\n'
        with open(filelog, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
    if(os.path.exists(filenameHTML)):
        os.remove(filenameHTML)
    print('Downloaded: ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1             
    #Tam dung mot chut    
    SleepTime=random.randint(10, 15)
    time.sleep(SleepTime)

print('Finished!')
