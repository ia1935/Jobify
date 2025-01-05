#grabbing user data to input in applications

#storing info as json and going to parse a text pdf resume
import json
from PyPDF2 import PdfReader
import os

#allowing user to browse disk instead of typing file location:
import tkinter as tk
from tkinter import filedialog


def GetUserInfo():

    print("Please enter a valid text PDF Resume")

    pdf_path=input("Enter the PDF path of the file: ").strip()

    if not os.path.exists(pdf_path):
        print("File not found. Please provide a valid path.")
    elif not pdf_path.lower().endswith('.pdf'):
        print("The file is not a PDF. Please provide a valid PDF file.")
    else:
        print("File Validated.")
        return pdf_path
    

def resumeScraper(file:str):

    None




    