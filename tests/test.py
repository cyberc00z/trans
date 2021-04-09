from PyPDF2 import PdfFileReader, PdfFileWriter
from google_trans_new import google_translator

pdfFileObj = open("tor-design.pdf", "rb")
pdfReader = PdfFileReader(pdfFileObj)

lang = input('Enter target language : ')

# no of pages
num_pages = pdfReader.numPages
print( "No of pages" , num_pages)
t = google_translator(timeout=10)
page_content=[]
#extracting text from each  page
for p in range(num_pages):
    page = pdfReader.getPage(p)
    text = page.extractText()
    text = text.readlines()
    print(text)
    #translation = t.translate(text.strip(" "), lang)
    #print(len(translation))
    #print(translation)
    """for line in range(len(translation)):
        result_text = translation[line].replace("\n\n", " ")
        page_content.append(result_text)
        print(page_content)
    """
   






