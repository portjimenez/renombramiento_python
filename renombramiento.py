from logging import root
import os #libreria que me permite manipular archivos de windows
from tkinter import filedialog
import PyPDF2

root.directory = filedialog.askdirectory()

route = root.directory+'/'

constancias = os.listdir(route)

for constancia in constancias:
    pdfFileObject = open(route+constancia, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    pageObject = pdfReader.getPage(0)
    text = pageObject.extractText()
    textLegnth = len(text)
    Uni = ""
    for letter in range(textLegnth):
        #en el "if" puedo designar (por letras) que parte del pdf le servira para renombrar
        if text[letter]=="N" and text[letter+1]=="o" and text[letter+2]=="m" and text[letter+3]=="b" and text[letter+4]=="r" and text[letter+5]=="e" and text[letter+6]=="  :":
            Uni = text[letter+7:letter+29]
            Uni = Uni.strip()
            pdfFileObject.close()

            os.rename(route+constancia, route+Uni+'.pdf')
