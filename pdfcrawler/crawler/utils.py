import re
import PyPDF2


def extract_urls_from_pdf(file_obj):
    pdf_obj = PyPDF2.PdfFileReader(file_obj)
    pages = pdf_obj.getNumPages()
    match_uri_regex =\
        r'\b((http|https):\/\/?)[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|\/?))'
    for page_num in range(pages):
        current_page = pdf_obj.getPage(page_num)
        page_obj = current_page.getObject()
        annotations = page_obj.get('/Annots')
        if annotations is not None:
            for annotation in annotations:
                node = annotation.getObject()
                uri = node.get('/A', {}).get('/URI')
                if uri is not None and re.match(match_uri_regex, uri):
                    yield uri
