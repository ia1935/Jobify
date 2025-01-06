#taking links_array and filling with info, need to have json data for necessary fields in application
#need name, number, email, school, 

#also need to have logging for websites that program had errors with for manual entry
#need to also connect this to a excel spreadsheet.


import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



def jobApplication(links:list):

    
    resume_info = '../data/resume_info.json'

    with open(resume_info,'r') as file:
        resume_data = json.load(file)

    driver = webdriver.Chrome()

    linkIssues=[]

    for link in links:
        try:
            driver.get(link)

        except:
            print("Error processing Link")
            linkIssues.append(link)
            continue
    
    return linkIssues


