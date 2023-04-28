#Script extract text from all file xhtml in current folder
#Version: 1.0.2


from bs4 import BeautifulSoup
import fitz
import fileinput
import os
import array as arr

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if os.path.exists(f) and f.endswith('.xhtml'):
        StrippedContent = ""
        filename = f[0:len(f)-len('.xhtml')]
        filenameTXT = filename+".txt"              
        with open(f, encoding="utf-8") as fp:
            soup = BeautifulSoup(fp,"lxml")
            #extract body content
            tag = soup.body
 
            #get each string recursively
            for content in tag.strings:
                StrippedContent = StrippedContent + "\n\n" + content
        
        with open(filenameTXT, 'a', encoding="utf-8") as handle:    
            handle.write(StrippedContent)
        print('Complete file: '+ f )
                    
print('Finished!')
