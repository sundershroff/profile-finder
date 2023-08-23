# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('angel.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
text = pageObj.extractText()
for line in text.split("\n"):
    # if "Name:" in line:
    #     name = line.split(":")[1].strip()
    # el
    #if "Address:" in line:
        address = line.split(":")[1].strip()
    
        # Print the name and address
        print("Name:", name)
        print("Address:", address)

# closing the pdf file object
pdfFileObj.close()
