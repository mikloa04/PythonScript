#Script extract lấy text từ file pdf, luu thanh file txt
#Version: 1.1
#pip install PyMuPDF


import fitz
import fileinput
import os
import array as arr

filenameTXT ="Ketqua_pdf.txt"

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if os.path.exists(f) and f.endswith('.pdf'):
        StrippedContent = ""          
        try:    
            #extract text from file pdf
            doc = fitz.open(f)
            for page in doc:
                text = page.get_text()            
                StrippedContent = StrippedContent +"\n" + text
            doc.close()
            #save to text file
            filenameTXT = f + ".txt"
            with open(filenameTXT, 'a', encoding="utf-8") as handle:    
                handle.write(StrippedContent)
            #delete pdf file
            os.remove(f)
            print('Complete file: '+f)
        except:
            print('Error convert file: '+ f)

print('Finished!')