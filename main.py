import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"
processed = "Processed"

types = ["invoice", "resume", "contract"]

def get_doc_type(content):
    for line in content.splitlines():
            if "Document Type: " in line:
                doc_type = line.split("Document Type:")
                return doc_type[1]

for file in os.listdir(DIRECTORY):
    if file != processed:
        print("Current File: " + file)
        # join file paths
        file_dir = os.path.join(DIRECTORY, file)

        try:
            read_file = open(file_dir, "r")
        except:
            print("File/Folder is not Readable: " + file)

        # read file
        contents = read_file.read()
        
        for file_type in types:
            if file_type.lower() in contents.lower():
                processed_dir = os.path.join(DIRECTORY, processed)
                if not os.path.exists(processed_dir):
                    os.makedirs(processed_dir)

                # Get our Document type
                doc_type = get_doc_type(contents)
                
                    