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

#going to categorize and apply for each job depending on its link.
import re


def jobApplication(links:list):

    
    resume_info = '../data/resume_info.json'

    with open(resume_info,'r') as file:
        resume_data = json.load(file)

    driver = webdriver.Chrome()

    linkIssues=[]

    for link in links:
        try:
            #checking if there is an apply button we press prior to filling out our information or an apply link
            driver.get(link)
            WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//form")))



            apply_elements = driver.find_elements(By.XPATH, "//*[self::button or self::a][contains(text(), 'Apply')]")
            if apply_elements:
                apply_elements[0].click()

            
            
                #wait for form to load if happened

                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//form")))
            

            #Start the form filling...
            driver.find_element(By.NAME, 'name').send_keys(resume_data['name'])
            driver.find_element(By.NAME, 'email').send_keys(resume_data['email'])
            driver.find_element(By.NAME, 'phone').send_keys(resume_data['phone'])

            
            submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
            submit_button.click()





        except:
            print("Error processing Link")
            linkIssues.append(link)
            input("Issue Occured, press enter when issue solved.")
            continue
    
    return linkIssues



#function for Greenhouse.io jobs(Very easy to apply to thankfully)

def greenhouse(link):
    #link has the pattern greenhouse.io in the website

    #format in this order:
    # first
    # last
    # email
    # phone
    # resume
    # education(
    #     school
    #     degree
    #     discipline
    #     start month/year
    #     end month/year

    # )
    # program will have to pause for now when handling personal questions and application specific questions
    None



def lever(link):
    # name jobs.lever.co
    # format in this order

    # resume
    # full name 
    # email
    # phone
    # linkedin Url   
    # other website(github)
    # grad date
    None