import io, sys
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_from_pdf(pdf_path, num_pages):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    laparams = LAParams()
    codec = 'utf-8'
    converter = TextConverter(resource_manager,fake_file_handle,codec=codec,
        laparams=LAParams(line_margin=2))
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    with open(pdf_path, 'rb') as fh:
        for num,page in enumerate(PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True), 1):

            if num <= int(num_pages):                                      
                page_interpreter.process_page(page)
            
            
            
        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()
    
    if text:
        return text


def get_text_from_file(input_file):
    input_file = sys.argv[1]  
    text = extract_text_from_pdf(input_file, num_pages)
    return text

    
if __name__ == '__main__':
    
    input_file = sys.argv[1]
    num_pages = sys.argv[2]
    result = get_text_from_file(input_file)
    print(result)
    
    