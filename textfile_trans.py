#!/usr/bin/env python



import os

from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
import time
import colorama

pool = ThreadPool(8) 

lang=input("Enter the target language :  ")
                                                 

def request(text):
    t = google_translator(timeout=5)
    new_pdf = t.translate(text.strip(), lang)
    return new_pdf

def main():
    time1 = time.time()
    print( G  +  "This method is good enough for big text files")

    with open('../source/input.txt', 'r') as fp:
        texts = fp.readlines()
        #texts = list(texts)
        try:
            results = pool.map(request, texts)
            pass
        except Exception as error:
            raise error
        pool.close()
        pool.join()

        time2 = time.time()
        print("Translating %s sentenctes, a total of %ss"%(len(texts), time2-time1))
        fp.close()

        ft = open('../source/result.txt', "w")
        L = texts
        ft.write(str(results))
        #ft.writelines(L)
        ft.close()
if __name__ == "__main__":
    main()
