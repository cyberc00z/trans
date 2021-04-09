import os
import time
from google_trans_new import google_translator
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from PyPDF2 import PdfFileReader


lang =input("Enter the target language: ")

def get_translated_page_content(reader, lang):
    num_pages = reader.numPages
    page_content = []
    translator = google_translator(timeout=10)
    for p in range(num_pages):
        page = reader.getPage(p)
        text = page.extractText()
        t_text = translator.translate(text.strip(), lang)
        result_text = t_text.text.replace("\n", "").replace("W", "")
        page_contents.append(result_text)
    return page_contents


def translated_pdf(path_to_pdf, lang):
    fp = open(path_to_pdf, 'rb')
    reader = PdfFileReader(fp)
    page_contents = get_translated_page_content(reader, lang)

    page_text = []
    name = f'{lang}_{path}'
    pdf = SimpleDocTemplate(name, pagesize=letter)

    for text in page_contents:
        page_text.append(
                  Paragraph(text, encoding='utf-8', style=regular))

        pdf.build(page_text)


if __name__ == '__main__':
    path_to_pdf = "./source/old.pdf"
    translated_pdf(path_to_pdf , lang)


