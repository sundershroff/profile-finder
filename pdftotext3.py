import PyPDF2
import re

pdf_file = open('abi.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
string = []
phda=0
data =[]
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    #print(page)
    lines = page.extractText().splitlines()
    for line in lines:
        string.append(re.sub(r'[^a-zA-Z0-9-/: ]', '', line))
        #print(line)


for i in string:
    if i.strip() != '':
        data.append(i)


for a in data:
    if a.isdigit() and len(a) == 10:
        #print(a)
        phda = data.index(a)
    

# if  data[9].isdigit():
#     phone = data[9]
#     aadhar = data[10]
# else:
#     phone = data[10]
#     aadhar = data[11]
if len(data) > 1:
    name = data[2]
    father_name = data[3].split(" ")[1].strip()
    address = data[4]+"\n"+data[5]+"\n"+data[6]+"\n"+data[7]
    phone = data[phda]
    aadhar = data[phda+1]
    dob = data[phda+9].split(":")[1].strip()
    gender = data[phda+10].split("/")[1].strip()
    district = data[-7].split("-")[0].strip()
    pincode = data[-7].split("-")[1].strip()

    print("Name :",name)
    print("Father Name :",father_name)
    print("Address : ",address)
    print("Phone : ",phone)
    print("Aadhar : ",aadhar)
    print("Dob : ",dob)
    print("Gender : ",gender)
    print("District :",district)
    print("Pincode :",pincode)

else:
    print("Enter Correct PDF Format")