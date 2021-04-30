# https://www.blog.pythonlibrary.org/2018/05/03/exporting-data-from-pdfs-with-python/

import io, sys
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    laparams = LAParams()
    codec = 'utf-8'
    converter = TextConverter(resource_manager,fake_file_handle,codec=codec,
        laparams=LAParams(line_margin=2))
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
    
    if text:
        return text
    
if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.replace('pdf','csv')

    t = extract_text_from_pdf(input_file)
    f = open(output_file, 'w')
    f.write(t)
    f.close()