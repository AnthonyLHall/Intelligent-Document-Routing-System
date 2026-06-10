import os
import shutil

# Processed File Directory

DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\IntelligentSorting"
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
            doc_type = doc_type_split[1].replace(" ", "")            
        if "vendor:" in line.lower():
            vendor_split = line.split("Vendor:")
            vendor = vendor_split[1].replace(" ", "")
        if "invoice number:" in line.lower():
            invoice_num_split = line.split("Invoice Number:")
            invoice_num = invoice_num_split[1].replace(" ", "")
        if "date:" in line.lower():
            date_split = line.split("Date:")
            date = date_split[1].replace(" ", "")
        if "amount:" in line.lower():
            amount_split = line.split()
            amount = amount_split[1].replace(" ", "")
        if "status" in line.lower():
            status_split = line.split()
            status = status_split[1].replace(" ", "")
            
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
            doc_type = doc_type_split[1].replace(" ", "")
        if "contract id:" in line.lower():
            contract_id_split = line.split("Contract ID:")
            contract_id = contract_id_split[1].replace(" ", "")
        if "client:" in line.lower():
            client_split = line.split("Client:")
            client = client_split[1].replace(" ", "")
        if "start date" in line.lower():
            start_date_split = line.split("Start Date:")
            start_date = start_date_split[1].replace(" ", "")
        if "end date" in line.lower():
            end_date_split = line.split("End Date:")
            end_date = end_date_split[1].replace(" ", "")
        if "status" in line.lower():
            status_split = line.split("Status:")
            status = status_split[1].replace(" ", "")


    return doc_type, contract_id, client, start_date, end_date, status

def get_resume_data(content):
    
    iter = 0
    lines = []
    line_numbers = [6, 9]

    doc_type = None
    name = None
    email = None
    phone_no = None
    skills = None
    experience = None

    for line in contents.splitlines():

        if "document type:" in line.lower():
            doc_type_split = line.split("Document Type:")
            doc_type = doc_type_split[1].replace(" ", "")
            
        if "name" in line.lower():
            name_split = line.split("Name:")
            name = name_split[1].replace(" ", "")
        
        if "email" in line.lower():
            email_split = line.split("Email:")
            email = email_split[1].replace(" ", "")

        if "phone" in line.lower():
            phone_split = line.split("Phone:")
            phone_no = phone_split[1].replace(" ", "")

        if "experience" in line.lower():
            pass

    for index, line in enumerate(contents.splitlines()):
        
        if "skills" in line.lower():
            lines.append(index)
            
        elif "experience" in line.lower():
            lines.append(index)

    all_lines = contents.splitlines()
    skills = [s.strip() for s in all_lines[lines[0] + 1 : lines[1]] if s.strip()]

    return doc_type, name, email, phone_no, skills

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
            print("File/Folder is not Readable And/Or Isnt a txt file.: " + file)

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
            
        
        if "contract" in contents.lower():
            doc_type, contract_id, client, start_date, end_date, status = get_contract_data(contents)
            contract_field["document_type"] = doc_type
            contract_field["contract_id"] = contract_id
            contract_field["client"] = client
            contract_field["start_date"] = start_date
            contract_field["end_date"] = end_date
            contract_field["status"] = status
        
        
        if "resume" in contents.lower():
            doc_type, name, email, phone_no, skills = get_resume_data(contents)
            resume_field["document_type"] = doc_type
            resume_field["name"] = name
            resume_field["email"] = email
            resume_field["phone_no"] = phone_no
            resume_field["skills"] = skills
        try:
            read_file.close()
            shutil.move(file_dir, processed_dir)
        except Exception as e:
            print(f"Move failed: {e}")

