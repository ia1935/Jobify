#Implemented file uploading for Scalability


#grabbing user data to input in applications

#storing info as json and going to parse a text pdf resume
import json
from PyPDF2 import PdfReader
import os


from pydparser import ResumeParser


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
    

def resumeScraper(file:str):

    # Step 1: Extract the text from the PDF

    data = ResumeParser(file).get_extracted_data()

    return data