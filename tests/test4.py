print("***********************************Now It's my term !!!*********************")

import os
import time
from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import colorama

pool = ThreadPool(8)


## we need some colors
B = '\033[94m'  #blue 
Y = '\033[93m'  #yellow
G= '\033[92m'   #green
R = '\033[91m'  #red
W = '\033[90m'  #white


#ask for target language
lang = input( W +"Enter target language : ")

#asking for file path
_path = input(str( G +"Enter pdf's file : "))

def find_pdf():
    """If some body calls this function with a path name of pdf  """
    #_path = input(str( G +"Enter pdf's file : "))
    file_path,extension = os.path.splitext(_path)    
    #print(file_path)
    #print(extension)
    if(extension=='.pdf'):
        translator = google_translator(timeout=10) 
        #print(R +"Got the pdf: {}".format(_path))
        fp = open(_path, "rb")
        reader = PdfFileReader(fp)
        num_pages = reader.numPages
        page_content = []
        for p in range(num_pages):
            page = reader.getPage(p)
            text = page.extractText()
            translated_text = translator.translate(text.strip(), lang)
            result_text = translated_text.replace("\n", " ").replace("W", "")
            print(B+"Transalting {}'th page in {}".format(p,lang))
            page_content.append(result_text)
            print(page_content)
            new_path = f'{lang}_{_path}'
        
            pdfWriter = PdfFileWriter()
            pdfWriter.addPage(page)
            new_pdf = open(new_path,'wb' )
            pdfWriter.write(new_pdf)
            
            
            
        print(Y + "Your translated pdf is {}".format(new_pdf)) 

          
    else:
        print( R+"Invalid File , not a pdf!")
    
    return

find_pdf()
"""
def new_pdf():
 How to add text into a new pdf  """

 
