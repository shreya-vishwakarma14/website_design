# import PyPDF2
# pdffileobject = open("information.pdf","rb")
# pdfreader = PyPDF2.PdfFileReader(pdffileobject)
# x=pdfreader.numPages
# pagesobj = pdfreader.getpage(x-1)
# text = pagesobj.extractText()

# file1 = open(r"information.pdf","a")
# file1.writelines(text)
# file1.close()



import PyPDF2
 
pdffileobj=open('information.pdf','rb')
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
#This will store the number of pages of this pdf file
x=pdfreader.numPages
#create a variable that will select the selected number of pages
pageobj=pdfreader.getPage(x+1)
text=pageobj.extractText()
file1=open(r"information.pdf","a")
file1.writelines(text)