"""       Yield
Yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator. yield keyword in Python is less known off but has a greater utility which one can think of. 

"""

""" StrignIO
The StringIO module an in-memory file-like object. This object can be used as input or output to the most function that would expect a standard file object. When the StringIO object is created it is initialized by passing a string to the constructer. If no string is passed the StringIO will start empty. In both cases, the initial cursor on the file starts at zero.
"""
"""
from io import StringIO
from PyPDF2 import PdfFileReader

fp =  open('tor-design.pdf', "rb")
reader  = PdfFileReader(fp)
num_pages = reader.numPages
for p in range(num_pages):
    page = reader.getPage(p)
    text = page.extractText()
    new_text = text.strip()
    rtext = StringIO(new_text)
    print(rtext.read())

"""
"""
from PyPDF2 import PdfFileReader
from io import StringIO
fp = open("tor-design.pdf", "rb")
page_content = ""
reader = PdfFileReader(fp)
num_pages = reader.numPages
for p in range(num_pages):
    page = reader.getPage(p)
    page_content += page.extractText()+ "\n"
full = " ".join(page_content.replace("W",  ""))
print(full)














