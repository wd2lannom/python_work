## from https://www.blog.pythonlibrary.org/2018/05/03/exporting-data-from-pdfs-with-python/ ##

## Create a resource manager instance. ##
## Then we create a file-like object via Python’s io module. ## 
## If you are using Python 2, then you will want to use the StringIO module. ##

import io

## Next step is to create a converter. In this case, we choose the TextConverter, ## 
##however you could also use an HTMLConverter or an XMLConverter if you wanted to. ##

from pdfminer.converter import TextConverter

## create a PDF interpreter object that will take our resource manager and converter objects and extract the text. ##

from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
 ## open the PDF and loop through each page ##

def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
 
        text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
 ## grab all the text, close the various handlers and print out the text to stdout ##
    if text:
        return text
 
if __name__ == '__main__':
    print(extract_text_from_pdf('w9.pdf'))