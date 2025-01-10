#Script để tải truyện từ Metruyencv
#Script tải html từng chương truyện về, sau đó extract lấy text, ghi vào file Ketqua_mtc.txt
#Version: 1.6.0
#Dung module playwright, pip install playwright, pip install playwright -U
#playwright install
#pip install PyMuPDF


import fitz
from playwright.sync_api import sync_playwright
import fileinput
import os
import array as arr

#Duong dan den chuong truyen
strURLStory='https://metruyencv.com/truyen/{ten-truyen}/chuong-'
StartChapter = 1 #So chuong bat dau
EndChapter = 999 #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua_mtc.txt"
filelog ="log_mtc.txt"

while (x<= EndChapter):
    StrippedContent=""
    ChapterURL=strURLStory+str(x)+'/'   
    filenameHTML =str(x)+".pdf"      
    #Get html from url, save as pdf file
    try:    
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(ChapterURL)
            page.wait_for_timeout(9000)
            page.emulate_media(media="screen")
            page.pdf(path=filenameHTML)
            browser.close()
        #Lấy text từ file pdf và lưu lại
        doc = fitz.open(filenameHTML)
        for page in doc:
            text = page.get_text()            
            StrippedContent = StrippedContent +"\n" + text
        doc.close()
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)

    except:
        StrippedContent = 'Error download '+ChapterURL+'\n'
        with open(filelog, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)

    if(os.path.exists(filenameHTML)):
            os.remove(filenameHTML)
    print('Downloaded ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1
    #Tam dung mot chut    
    SleepTime=random.randint(10, 15)
    time.sleep(SleepTime)

print('Finished!')
