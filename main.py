import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"
processed = "Processed"


invoice_field = {}
resume_field = {}
contract_field = {}

def get_invoice_data(content):
    vendor = None
    doc_type = None
    invoice_num = None
    date = None
    amount = None
    status = None

    for line in content.splitlines():
        if "document type:" in line.lower():
            doc_type_split = line.split("Document Type:")
            doc_type = doc_type_split[1]            
        if "vendor:" in line.lower():
            vendor_split = line.split("Vendor:")
            vendor = vendor_split[1]
        if "invoice number:" in line.lower():
            invoice_num_split = line.split("Invoice Number:")
            invoice_num = invoice_num_split[1]
        if "date:" in line.lower():
            date_split = line.split("Date:")
            date = date_split[1]
        if "amount:" in line.lower():
            amount_split = line.split()
            amount = amount_split[1]
        if "status" in line.lower():
            status_split = line.split()
            status = status_split[1]
            
    return doc_type, vendor, invoice_num, date, amount, status
            
def get_contract_data(content):
    doc_type = None
    contract_id = None
    client = None
    start_date = None
    end_date = None
    status = None

    for line in content.splitlines():
        if "document type:" in line.lower():
            doc_type_split = line.split("Document Type:")
            doc_type = doc_type_split[1]
        if "contract id:" in line.lower():
            contract_id_split = line.split("Contract ID:")
            contract_id = contract_id_split[1]
        if "client:" in line.lower():
            client_split = line.split("Client:")
            client = client_split[1]
        if "start date" in line.lower():
            start_date_split = line.split("Start Date:")
            start_date = start_date_split[1]
        if "end date" in line.lower():
            end_date_split = line.split("End Date:")
            end_date = end_date_split[1]
        if "status" in line.lower():
            status_split = line.split("Status:")
            status = status_split[1]


    return doc_type, contract_id, client, start_date, end_date, status

def get_resume_data(content):
    doc_type = None
    name = None
    email = None
    phone_no = None
    Skills = None
    Experience = None

    for line in contents.splitlines():
        if "document type:" in line.lower():
            doc_type_split = line.split("Document Type:")
            doc_type = doc_type_split[1]

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
            invoice_field["document_type"] = doc_type
            invoice_field["vendor"] = vendor
            invoice_field["invoice_number"] = invoice_num
            invoice_field["date"] = date
            invoice_field["amount"] = amount
            invoice_field["status"] = status
            print("file dropped is invoice")
        
        if "contract" in contents.lower():
            doc_type, contract_id, client, start_date, end_date, status = get_contract_data(contents)
            contract_field["document_type"] = doc_type
            contract_field["contract_id"] = contract_id
            contract_field["client"] = client
            contract_field["start_date"] = start_date
            contract_field["end_date"] = end_date
            contract_field["status"] = status
            print("file dropped is contract")
        
        if "resume" in contents.lower():
            pass


print(contract_field)