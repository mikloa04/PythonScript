#Script để tải truyện từ ttk.tw
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_truyen35.txt
#Version: 2.2
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
strURLStory='https://ttk.tw/novel/chapters/wohewushugewo/'
StartChapter=1 #So chuong bat dau
EndChapter=320 #So chuong ket thuc 
filenameTXT ="ta-cung-vo-so-ta-320.txt"
filelog ="log.txt"


x=StartChapter    
retry = 0
while (x<= EndChapter):
    
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'.html'    
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
            #for title in soup.find_all('title'):
             #   downloaded  =   title.get_text()
             #   break
            #StrippedContent = "\n"+ downloaded
            
            #Lay noi dung chuong
            _text = ''
            for _div in soup.find_all("div", class_="content"):
            #Loai bo tag p
                _text = _text +"\n\n"+ _div.get_text()
              
            #Luu Noi dung chuong
            StrippedContent="\n"+StrippedContent+"\n"+_text+"\n"
            bCheckLink=1
        except:
            bCheckLink=0
    
    if bCheckLink==1:  
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
        print('Downloaded: ('+str(x)+'/'+str(EndChapter)+')' )
        x+=1
        retry = 0
    else:
        retry += 1
        if (retry == 4):
            StrippedContent = 'Error download '+ChapterURL+'\n'
            with open(filelog, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
            print('Error Downloaded: ('+str(x)+')' )
            x+=1
            retry = 0

    if(os.path.exists(filenameHTML)):
        os.remove(filenameHTML)
    
                 
    #Tam dung mot chut    
    SleepTime=random.randint(3,7)
    time.sleep(SleepTime)

print('Finished!')