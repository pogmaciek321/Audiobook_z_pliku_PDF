import PyPDF2
from gtts import gTTS
import os
from tkinter.filedialog import *

plik = askopenfilename(title="wybierz plik pdf",filetypes=[("Pdf files","*.pdf")])
pdfreader = PyPDF2.PdfReader(plik)
ilosc_stron = len(pdfreader.pages)

for i in range (ilosc_stron):
    strona = pdfreader.pages[i]
    tekst =  strona.extract_text()

interface = gTTS(text= tekst, lang='en',tld='us',slow=False)
interface.save("audiobook.mp3")
os.startfile("audiobook.mp3")
    
    