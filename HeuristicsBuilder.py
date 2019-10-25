# -*- coding: utf-8 -*-
'''
from tika import parser

raw = parser.from_file("F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf")
print(raw['content'])
'''
'''
import textract
text = textract.process("F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf")
'''
'''

import PyPDF2
import collections
pdf_file = open('F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
c = collections.Counter(range(number_of_pages))
for i in c:
   page = read_pdf.getPage(i)
   page_content = page.extractText()
   print (page_content.encode('base64'))
'''
'''
f = open('F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf', encoding='cp720')
print()
'''
#print(f.read())
'''
from magic import libmagic
import magic


blob = open('F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf').read()
m = magic.open(magic.MAGIC_MIME_ENCODING)
m.load()
encoding = m.buffer(blob)  # "utf-8" "us-ascii" 

'''

'''

import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# This function will extract and return the pdf file text content.
def extractPdfText(filePath=''):

    # Open the pdf file in read binary mode.
    fileObject = open(filePath, 'rb')

    # Create a pdf reader .
    pdfFileReader = PyPDF2.PdfFileReader(fileObject)

    # Get total pdf page number.
    totalPageNumber = pdfFileReader.numPages

    # Print pdf total page number.
    print('This pdf file contains totally ' + str(totalPageNumber) + ' pages.')

    currentPageNumber = 1
    text = ''

    # Loop in all the pdf pages.
    while(currentPageNumber < totalPageNumber ):

        # Get the specified pdf page object.
        pdfPage = pdfFileReader.getPage(currentPageNumber)

        # Get pdf page text.
        text = text + pdfPage.extractText()

        # Process next page.
        currentPageNumber += 1

    if(text == ''):
        # If can not extract text then use ocr lib to extract the scanned pdf file.
        text = textract.process(filePath, method='tesseract', encoding='utf-8-sig')
       
    return text



pdfFilePath = 'F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf'
   
pdfText = extractPdfText(pdfFilePath)
print('There are ' + str(pdfText.__len__()) + ' word in the pdf file.')
print(pdfText)
'''
pdfFilePath = 'F:\\Current Semester\\FYP\\Heuristics\\IslamAurJadeedFalsafaeHayat.pdf'

'''
# modules for 
import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open(pdfFilePath, 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(100)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())
'''

from xpdf_python import to_text

pdf_location = pdfFilePath
text = to_text(pdf_location)