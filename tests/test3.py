# standard libraries
import os
import time

# installed libraries
from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
from PyPDF2 import PdfFileReader


pool = ThreadPool(8)	

#lang = input("Enter language first two letter in which you want to translate : ")

def noOfPage():
    pdfFileObj = open(f'old.pdf', 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    print(num_pages)

noOfPage()
