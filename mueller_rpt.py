from pdf2image import convert_from_path
import pytesseract

print("***** starting *****")

mueller = "/Users/dave/python_work/report.pdf"

def pdf2txt(mueller, num_pages=10):
    ##use pdf2image to keep the pages in memory
    pages = convert_from_path(mueller, 500, first_page=0, last_page=num_pages)
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
text = pdf2txt(mueller,10)
print(text)
f = open( 'file.txt', 'w' )
f.write( repr(text) )
f.close()

