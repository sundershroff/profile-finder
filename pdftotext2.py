import PyPDF2

with open('sunderaadhar.pdf', 'rb') as pdf_file:
    # Create a PdfFileReader object to read the PDF file
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Get the first page of the PDF
    first_page = pdf_reader.getPage(0)
    
    # Extract the text content of the line that contains the name and address information
    if len(first_page.extractText().split('\n')) > 1:
        name = first_page.extractText().split('\n')[11]
        address = first_page.extractText().split('\n')[12] +"\n" +first_page.extractText().split('\n')[13]+"\n"+first_page.extractText().split('\n')[14]+"\n"+first_page.extractText().split('\n')[15]+"\n"+first_page.extractText().split('\n')[16]
        #pincode = first_page.extractText().split('\n')[17].split(" - ")[1].strip()
        # phone = first_page.extractText().split('\n')[18]
        # aadhar_no = first_page.extractText().split('\n')[19]
        # dob = first_page.extractText().split('\n')[36].split(":")[1].strip()
        # gender = first_page.extractText().split('\n')[38].split("/")[1].strip()
        # district = first_page.extractText().split('\n')[72].split(",")[0].strip()
        # State = first_page.extractText().split('\n')[73].split("-")[0].strip()
        print("Name:", name)
        print("Address:", address)
        #print("Pincode:", pincode)
        # print("Phone:", phone)
        # print("Addhar No:", aadhar_no)
        # print("DOB:", dob)
        # print("Gender:", gender)
        # print("District:", district)
        # print("State:",State)
    
    else:
        print("Enter Correct Pdf Format")
