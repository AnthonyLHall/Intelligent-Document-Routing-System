import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"
processed = "Processed"


invoice_field = {}
resume_field = {}
contract_field = {}

def get_invoice_data(content):

    global vendor
    global doc_type
    global invoice_num
    global date
    global amount
    global status

    vendor = None
    doc_type = None
    invoice_num = None
    date = None
    amount = None
    status = None

    for line in content.splitlines():
        if "Document Type:".lower() in line.lower():
            doc_type_split = line.split("Document Type:")
            doc_type = doc_type_split[1]            
        if "Vendor:".lower() in line.lower():
            vendor_split = line.split("Vendor:")
            vendor = vendor_split[1]
        if "invoice number:".lower() in line.lower():
            invoice_num_split = line.split("Invoice Number:")
            invoice_num = invoice_num_split[1]
        if "date:".lower() in line.lower():
            date_split = line.split("Date:")
            date = date_split[1]
        if "amount:".lower() in line.lower():
            amount_split = line.split()
            amount = amount_split[1]
        if "status".lower() in line.lower():
            status_split = line.split()
            status = status_split[1]
            
    return doc_type, vendor, invoice_num, date, amount, status
            

processed_dir = os.path.join(DIRECTORY, processed)
if not os.path.exists(processed_dir):
    os.makedirs(processed_dir)

for file in os.listdir(DIRECTORY):
    if file != processed:
        print("Current File: " + file)
        # join file paths
        file_dir = os.path.join(DIRECTORY, file)

        #read file
        try:
            read_file = open(file_dir, "r")
        except:
            print("File/Folder is not Readable: " + file)

        # read file
        contents = read_file.read()
            
        if "invoice" in contents.lower():
            doc_type, vendor, invoice_num, date, amount, status = get_invoice_data(contents)
            invoice_field["document type"] = doc_type
            invoice_field["vendor"] = vendor
            invoice_field["invoice_number"] = invoice_num
            invoice_field["date"] = date
            invoice_field["amount"] = amount
            invoice_field["status"] = status

print(invoice_field)