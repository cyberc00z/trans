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

print(""" %s


                       PRINT THE MOST UGLY BANNER
  

                                      tttt
                                      t  t
                                      t  t                                             
                                 tttttt  tttttt   %s  rrrrrrrrr        aa                  nn
                                                                                        n    n            ssssssssss
                               ttttttt %s ttttttt   rrrrrrrrrr      aaa  aa           nn      nn          s      
                                      t  t          rrr          aaa      aa         nn        nn         s   s    
                                      t  t          rrr          aa  %s   aaa        nn        nn         ssssssss 
                                      t  t          rrr          aa      aaaa        nn        nn               ss
                                                                                                                  
        
                                          (TRANSLATE PDFS AND  TEXT FILES)

                                          %sby Adhrit 
                                           twitter : https://twitter.com/xadhrit 
                                           github : https://github.com/xadhrit 
                                                 
       """%(R,Y,SB,G, P))


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
        print('Creating file for translated text in %s_%s.txt '%(name, lang))
        ft = open(result_file, "w")
        L = texts 
        #trying to write translation in good readable form
        
        results = str(results)
        #results = results.replace('',)                  
        ft.write(results)
        #ft.writelines(L)
        ft.close()
        print(G+'Done, success!')
if __name__ == "__main__":
    main()
