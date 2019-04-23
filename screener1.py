## this the first script used to extract and view text inside a pdf
## this script extracts the requested number of pages and put it in a file
from pdf2image import convert_from_path
import pytesseract

## specify the first and last pages
first_page = input("What is the starting page?   ")
first_page = int(first_page)
last_page = input("What is the last page?   ")
last_page = int(last_page)

print("***** starting, standby..... *****")

## set the target file variable name 4/21/19 ##
## Mike's Comment ##
target_file = "/Users/dave/files/report.pdf"

def pdf2txt(target_file, num_pages=100):
    ##use pdf2image to keep the pages in memory
    pages = convert_from_path(target_file, 500, first_page, last_page)
    docs = []
    ## iterate through each page saving the text and page number
    for i,page in enumerate(pages):
        d = {}
        text = pytesseract.image_to_string(page) 
        d['page'] = i+1 ## index from 0
        d['text'] = text 
        ##create list of dictionaries
        docs.append(d)
    print("***** Done *****")
    return docs
text = pdf2txt(target_file,10)
print(text)
f = open( 'file.txt', 'w' )
f.write( repr(text) )
f.close()

