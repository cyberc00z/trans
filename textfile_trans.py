import os
from google_trans_new import google_translator
from multiprocessing.dummy import Pool as ThreadPool
import time
from rich.console import Console
from pyfiglet import Figlet



# start here !!

pool = ThreadPool(8) 

pc = Console()

lang= input( "Enter the target language :  ")

_path = input(str( "Enter target file's path : "))


def clearConsole():
    cmd = 'clear'
    if os.name is ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)

def request(text):
    t = google_translator(timeout=5)
    new_pdf = t.translate(text.strip(), lang)
    return new_pdf

def banner():
    clearConsole()
    banner = Figlet(font='graffiti', justify='right')
    pc.print(banner.renderText("TRANS"), style="yellow")


def main():
    # banner
    banner()
    time1 = time.time()
    pc.print( "This method is good enough for big text files", style="yellow")
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
        pc.print( "Translating %s sentenctes, a total of %ss"%(len(texts), time2-time1), style="red")
        fp.close()
        result_file = f'{name}_{lang}.txt'
        pc.print('Creating file for translated text in %s_%s.txt '%(name, lang), style="bright_cyan")
        ft = open(result_file, "w")
        L = texts 
        #trying to write translation in good readable form
        
        results = str(results)
        #results = results.replace('',)                  
        ft.write(results)
        #ft.writelines(L)
        ft.close()
        pc.print('Done, success!', style="green")
if __name__ == "__main__":
    main()
