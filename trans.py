# Standard Libraries
import os  #operating system level operations
import time   #for finding time 
## installed libs
from google_trans_new import google_translator  #google api interface 
from PyPDF2 import PdfFileReader        # lib for various pdf operations
from pdfminer.high_level import extract_text   #lib for  extracting text from pdf
from multiprocessing.dummy import Pool as ThreadPool ## concurrecy and creating pools
from rich.console import Console
from pyfiglet import Figlet    #for ascii art


pool = ThreadPool(8)

## console object
pc = Console()

### asking for language in which you want to translate your pdf
lang = pc.print( "Enter target language : e.g. (en- english,zh- chienese, th-thai, de-destuche ) : ", style="bright_yellow")
input()

# asking for where is pdf file
_path = input(str("Enter pdf file path or name(if in same folder) : "))


def clearConsole():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)


def banner():
    clearConsole()
    banner = Figlet(font='graffiti', justify='right')
    pc.print(banner.renderText( " TRANS"), style="yellow")
    


def check_file(_path):
        file_path, extension = os.path.splitext(_path)
        if (extension == '.pdf'):
           pc.print('We got the pdf {}'.format(_path), style="green")

        else:
           pc.print( 'Invalid file or not a pdf ', style="red")

def request(text):
    translator = google_translator(timeout=10)
    translated_text = translator.translate(text.strip(), lang)                                                              
    return translated_text



def translate_func():
    banner()
    # open , read  and get pages from pdf
    check_file(_path)
    name, ex = os.path.splitext(_path)
    fp = open(_path, 'rb')
    reader = PdfFileReader(fp)
    num_pages = reader.numPages
    pc.print("Pdf contents {} pages".format(num_pages), style="blue")

    #extracting text
    
    time_before= time.time()
    text = extract_text(_path)
    time_after = time.time()
    pc.print("Extracting text from Each Page of {} in total of {} seconds".format(_path, time_after-time_before), style="bright_cyan")
   
    ## putting all text in one new file
    fw = open(f'{name}.txt'  , 'w')
    fw.write(text)
    
    pc.print('Successfully created text file for all text ', style="bright_black")

    ## start translating stuff
    
    time_first = time.time()

    with open(f'{name}.txt', 'r') as fn:
        lines = fn.readlines()
        try:
            results = pool.map(request, lines)
            pass
        except Exception as error:
            raise error

        pool.close()
        pool.join()

        time_second = time.time()

        print("Translating in %s  in a total of %s seconds"%(len(lines), time_second-time_first))
        fn.close()
        result_file = f'{name}_{lang}.txt'
        result = open(result_file, 'w')
        result.write(str(results))
        pc.print('  Created your %s lang translated text file of %s  '%(lang, _path), style="cyan")

def main(): 
    translate_func()


if __name__ == '__main__':
    main()


    



