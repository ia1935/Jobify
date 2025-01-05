#grabbing user data to input in applications

#storing info as json and going to parse a text pdf resume
import json
from PyPDF2 import PdfReader
import os
import re


#allowing user to browse disk instead of typing file location:
import tkinter as tk
from tkinter import filedialog


def GetUserInfo():
    #making root window 
    root = tk.Tk()
    #hide main window
    root.withdraw()

    print("Please enter a valid text PDF Resume")


    # opening file browser to get a valid pdf file
    pdf_path = filedialog.askopenfilename(
        title="Select a PDF Resume",
        filetypes=[("PDF files", "*.pdf")]  # PDF ONLY
    )


    if not os.path.exists(pdf_path):
        print("File not found. Please provide a valid path.")
    elif not pdf_path.lower().endswith('.pdf'):
        print("The file is not a PDF. Please provide a valid PDF file.")
    else:
        print("File Validated.")
        return pdf_path
    

#extracting info from pdf and returning it as text
def textExtractorPDF(pdf_path):
    reader = PdfReader(pdf_path)

    text=""

    for page in reader.pages:
        text+=page.extract_text()

    return text

#taking in text from above function to parse for resume data
def resumeParse(text):
    #dictionary to place extracted info in
    resumeData={}

    #Grabbing name
    name_match = re.search(r"([A-Z][a-z]* [A-Z][a-z])(?=\n)", text)
    if name_match:
        resumeData['name'] = name_match.group(1)
    else:
        resumeData['name'] = "Not Found"

    #grabbing email:
    email_match = re.search(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
    if email_match:
        resumeData['email'] = email_match.group(0)
    else:
        resumeData['email'] = "Not Found"
    
    #Grabbing Phone Number

    phone_match = re.search(r"(\+?[1-9]\d{1,2}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4})", text)
    if phone_match:
        resumeData['phone'] = phone_match.group(0)
    else:
        resumeData['phone'] = "Not Found"
    





    #returing our resume Data after extracting info.
    return resumeData
    


    


def resumeScraper(file:str):

    
    None



    