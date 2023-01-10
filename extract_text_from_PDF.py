#Script extract lấy text từ file pdf, ghi vào file Ketqua_pdf.txt
#Version: 1.0.1
#pip install PyMuPDF


import fitz
import fileinput
import array as arr

#Duong dan den chuong truyen

StartChapter=a #So chuong bat dau
EndChapter=z #So chuong ket thuc
x=StartChapter    
filenameTXT ="Ketqua_pdf.txt"

while (x<= EndChapter):
    StrippedContent=""    
    filenameHTML =str(x)+".pdf"      
    try:    

        #Lấy text từ file pdf và lưu lại
        doc = fitz.open(filenameHTML)
        for page in doc:
            text = page.get_text()            
            StrippedContent = StrippedContent +"\n" + text
        doc.close()
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
    except:
        print('Khong ton tai Chuong: '+str(x))
    print('Da tai ('+str(x)+'/'+str(EndChapter)+')' )    
    x+=1

print('Hoan tat!')
