import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"
processed = "Processed"

types = ["invoice", "resume", "contract"]

invoice_field = {}
resume_field = {}
contract_field = {}

def get_invoice_data(content):

    global vendor
    global doc_type

    vendor = None
    doc_type = None

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
            
    return doc_type, vendor, invoice_num
            

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
            doc_type, vendor, invoice_num = get_invoice_data(contents)
            print(doc_type)
            print(vendor)
            

print(invoice_field)