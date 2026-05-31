import os
import shutil

# Processed File Directory
DIRECTORY = r"C:\Users\antde\OneDrive\Desktop\Intelligent-Document-Routing"

for file in os.listdir(DIRECTORY):

    # join file paths
    file_dir = os.path.join(DIRECTORY, file)
    read_file = open(file_dir, "r")

    contents = read_file.read()
    print(contents)