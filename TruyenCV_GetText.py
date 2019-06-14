#Script để tải truyện từ Truyencv
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua.txt

from bs4 import BeautifulSoup
import requests
import fileinput
import random
import time
import os

headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.0; App Runtime for Chrome Dev Build/54.5021.629.0)',
    'Accept-Encoding': 'gzip'
}

#Khoi tao 
StartChapter=1 #So chuong bat dau 
EndChapter=1315  #So chuong Ket thuc 
x=StartChapter

strURLStory='Đường-dẫn-đến-chương-truyện'
#Sample: strURLStory='https://truyencv.com/pokemon-he-thong-thanh-tuu-dai-su/chuong-'

filenameTXT ="Ketqua.txt" 

while (x<= EndChapter):
  StrippedContent=""
  ChapterURL=strURLStory+str(x)+'/'    
  response=requests.get(ChapterURL,headers=headers)
  filenameHTML =str(x)+".html"  
  
  open(filenameHTML, 'wb').write(response.content)
  with open(filenameHTML, encoding="utf-8") as fp:
    soup = BeautifulSoup(fp,"lxml")
    #Luu tieu de  
    StrippedContent='C'+str(x).zfill(4)+' - '+ soup.title.string+'\n'
    
    div= soup.find(id="js-truyencv-content")
    
    #Loai bo tag br
    for elem in div.find_all("br"):
      elem.replace_with(elem.text + "\n")
      
    #Luu Noi dung chuong
    StrippedContent=StrippedContent+'\n'+div.text
    
  with open(filenameTXT, 'a', encoding="utf-8") as handle:    
    handle.write(StrippedContent)
  print('Đã tai ('+str(x)+'/'+str(EndChapter)+')' )    
  x+=1        
  os.remove(filenameHTML) 
  
  #Tam dung mot chut    
  SleepTime=random.randint(5, 10)
  time.sleep(SleepTime)

print('Hoan tat!')
