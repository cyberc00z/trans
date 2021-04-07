from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
import time

pool = ThreadPool(8) 

def request(text):
    lang="en"
    t = google_translator(timeout=5)
    ttext = t.translate(text.strip(), lang)
    return ttext

def main():
    time1 = time.time()
    with open('./xadhrit.txt', 'r') as fp:
        texts = fp.readlines()
        try:
            results = pool.map(request, texts)
        except Exception as error:
            raise error
        pool.close()
        pool.join()

        time2 = time.time()
        print("Translating %s sentenctes, a total of %ss"%(len(texts), time2-time1))
        fp.close()

        ft = open('./t.txt', "w")
        L = texts
        ft.write(str(results))
        #ft.writelines(L)
        ft.close()

if __name__ == "__main__":
    main()
