import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"
processed = "Processed"

types = ["invoice", "resume", "contract"]

for file in os.listdir(DIRECTORY):

    print("Current File: " + file)
    # join file paths
    file_dir = os.path.join(DIRECTORY, file)
    read_file = open(file_dir, "r")

    # read file
    contents = read_file.read()

    for file_type in types:
        if file_type.lower() in contents.lower():
            processed_dir = os.path.join(DIRECTORY, processed)
            if not os.path.exists(processed_dir):
                os.makedirs(processed_dir)
            

            