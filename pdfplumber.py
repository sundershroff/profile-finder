import pdfplumber

with pdfplumber.open("angel.pdf") as pdf:
    # Get the first page of the PDF
    first_page = pdf.pages[0]
    
    # Extract text content from the first page
    text = first_page.extract_text()
    
    # Split the text into lines and loop through each line to find the name and address
    for line in text.split("\n"):
        if "Name:" in line:
            name = line.split(":")[1].strip()
        elif "Address :" in line:
            address = line.split(":")[1].strip()
    
    # Print the name and address
    print("Name:", name)
    print("Address:", address)







