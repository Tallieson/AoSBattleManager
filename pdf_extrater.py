import PyPDF2
import re

FILE_PATH = 'Generals_handbook_2019.pdf'

# open the pdf file
PDFobject = PyPDF2.PdfFileReader(FILE_PATH)
print(PDFobject)
# get number of pages
NumPages = PDFobject.getNumPages()
print(NumPages)

# define keyterms
# String = "Battleplan"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = PDFobject.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText() 
    print(Text)
    # ResSearch = re.search(String, Text)
    # print(ResSearch)