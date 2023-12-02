# import PyPDF2

# pdfFileObject = open("information.pdf",'rb')

# pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

# print(f"No of Pages: {pdfReader.numPages}")

# pageObject = pdfReader.getPage(0)

# text = pageObject.extractText()

# pdfFileObject.close()

# with open("information.txt","w") as file:
#     pass



#updated 
import PyPDF2

pdfFileObject=open("information.pdf","rb")
pdfReader=PyPDF2.PdfReader(pdfFileObject)
print(f"No of Pages:{len(pdfReader.pages)}")
pageObject=pdfReader.pages[0]
text=pageObject.extract_text()
pdfFileObject.close()

with open("information.txt","w") as file:
    file.write(text)
