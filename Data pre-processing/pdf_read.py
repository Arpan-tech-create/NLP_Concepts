import PyPDF2

data=open('C:/Users/ARPAN/Downloads/GATE-2022_brochure.pdf','rb') #-------open pdf file  object----#

reader=PyPDF2.PdfFileReader(data)

print(reader.numPages)

pageObj = reader.getPage(0)   #--------creating page object--------#
 
# extracting text from page
print(pageObj.extractText())

data.close() #--------closing the pdf file object--------------#