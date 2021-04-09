import time
from pdfminer.high_level import extract_text
from PyPDF2 import PdfFileReader
from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(8)

lang = input("Enter target language : ")

def request(text):
    translator = google_translator(timeout=10)
    new_file = translator.translate(text.strip(), lang)
    return new_file

def main():
    time_now = time.time()
    #opening pdf
    fp = open('tor-design.pdf', "rb")
    reader = PdfFileReader(fp)
    no_of_pages = reader.numPages
    print("Pdf contents pages {} ".format(no_of_pages))

    #extracting text
    text = extract_text('tor-design.pdf')
    time_here = time.time()
    print("Extracting text from tor-design.pdf file, it will take %s seconds "%(time_here-time_now))
    #print(text)

    #writing in text file
    fw = open('new.txt', 'w')
    fw.write(text)

    #start translating stuff
    with open('new.txt', 'r') as fn:

        lines = fn.readlines()
        #print(lines)
        try:
            results = pool.map(request, lines)
            pass
        except Exception as error:
            raise error
        pool.close()
        pool.join()

        time_then = time.time()
        print("Translating %s lines in a total of %s seconds"%(len(lines), time_then-time_now))
        fn.close()
        final_file = f'{lang}_file.txt'
        result_file = open(final_file, "w")
        result_file.write(str(results))
        result_file.close()


if __name__ == "__main__":
    main()






