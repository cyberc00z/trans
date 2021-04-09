#!/usr/bin/env python
import colorama

#colors
SB = '\033[96m'  #skyblue
P = '\033[95m'  #pink
B = '\033[94m'  #blue
Y = '\033[93m'  #yellow
G= '\033[92m'   #green
R = '\033[91m'  #red
W = '\033[90m' #white


print("""%s
        tttt
        t  t
        t  t       %s
   tttttt  tttttt     rrrrrrrrr
  tttttt %s tttttt   rrrrrrrr
        t  t        rrr
        t  t        rrr
        t  t        rrr                        ANS
        tttt        rrr

                                          (TRANSLATE PDFS AND  TEXT FILES)
                                          %sby Adhrit
                                          [twitter : https://twitter.com/xadhrit]
                                          [github : https://github.com/xadhrit]

       """%(R,Y,SB,G))


import os
from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
import time


pool = ThreadPool(8) 

lang=input( R + "Enter the target language :  ")

_path = input(str( Y  + "Enter target file's path : "))


def request(text):
    t = google_translator(timeout=5)
    new_pdf = t.translate(text.strip(), lang)
    return new_pdf

def main():
    time1 = time.time()
    print( G  +  "This method is good enough for big text files")
    name, ext = os.path.splitext(_path)     
    with open(_path, 'r') as fp:
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
        print( SB +  "Translating %s sentenctes, a total of %ss"%(len(texts), time2-time1))
        fp.close()
        result_file = f'{name}_{lang}.txt'
        ft = open(result_file, "w")
        L = texts
        ft.write(str(results))
        #ft.writelines(L)
        ft.close()
        print(G+'Done, success!')
if __name__ == "__main__":
    main()
