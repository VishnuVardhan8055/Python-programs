from PyPDF2 import PdfFileReader

def pdfread(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        page_numbers = pdf.getNumPages()

    txt = f"""
    
    Author : {information.author}
    Pages:{page_numbers}"""
    print(txt)
    return information
path = input("Enter your path:")
pdfread(path)