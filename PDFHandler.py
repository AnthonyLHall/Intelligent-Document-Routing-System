from pdf2image import convert_from_path
import pytesseract
import pymupdf
import os

directory = "/Users/anthonyhall/Desktop/ML Project Storage/Intelligent-Document-Routing-System/Intelligent-Document-Routing-System/Resumes PDF"

for folder in os.listdir(directory):
    print(folder)


"""pages = convert_from_path("/Users/anthonyhall/.cache/kagglehub/datasets/hadikp/resume-data-pdf/versions/1/Resumes PDF/Accountant/0.pdf")

text = ""
for page in pages:
    text += pytesseract.image_to_string(page)

print(text)"""