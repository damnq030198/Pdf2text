# txtfile = filename+ '.txt'

from PyPDF2 import PdfFileReader
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        # get the first page
        page = pdf.getPage(1)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        print(text)
if __name__ == '__main__':
    filename =  'Sachvui.Com-lap-trinh-ngon-ngu-tu-duy-carolyn-boyes'
    pdffile = filename+ '.pdf'
    text_extractor(pdffile)
