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


from dataRetrieval import GetUserInfo
#going to categorize and apply for each job depending on its link.
import re


driver = webdriver.Chrome()


# resume_info = '../data/resume_info.json'
# with open(resume_info,'r') as file:
#     resume_data = json.load(file)




resume_data={
    "name": "Name",
    "email": "mail@gmail.com",
    "phone": "123-456-7890",
    "location": "Boston, MA",
    "skills": [
        "What","Skills","Do I have"
    ],
    "education": [
      {
        "degree": "Bachelor of Science",
        "field_of_study": "Computer Science",
        "university": "Boston College",
        "location":"Boston, MA",
        "graduation_month":"May",
        "graduation_year": "2026"
      }
    ],
    "work_experience": [
      {
        "job_title": "Job title",
        "company": "Job",
        "start_date": "2024-10-26",
        "end_date": "Present",
        "location": "San Francisco, CA",
        "responsibilities": [   
          "Place responsibilities here","More responsibilities"
        ]
      }
    ],
    "social_links": {
      "linkedin": "https://www.linkedin.com/",
      "github": "https://github.com/"
    }
  }


#this is the file path for our resume. Jobs ask for this so we need to keep file of it.
resume_file = GetUserInfo()


def identify_platform(url):
    patterns = {
        "Workday": r"workdayjobs\.com|\.workday\.",
        "Greenhouse": r"boards\.greenhouse\.io",
        "Lever": r"lever\.co"
    }
    for platform, pattern in patterns.items():
        if re.search(pattern, url):
            return platform
    return "Unknown"

def jobApplication(links:list):

    
    



    linkIssues=[]

    for link in links:
        try:
            
            
          
            platform = identify_platform(link)
            print(f"URL: {link}\nPlatform: {platform}\n")
            if platform == "Unknown":  # Pause on unknown platform
                print("Pausing for manual intervention...")
                input("Press Enter to continue after resolving the issue.")



            #Checking if there is an apply button we press prior to filling out our information or an apply link
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
            try:

                #need to see what type of site it is for the proper function call:

                submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
                submit_button.click()
            except:
                input("Issue Occured, press enter when issue solved.")
                continue





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
    split_name = resume_data['name'].split(0)
    print(split_name)
    driver.find_element(By.NAME,'First Name').send_keys(split_name[0])
    driver.find_element(By.NAME, 'Last Name').send_keys(split_name[1])

    driver.find_element(By.NAME,'email').send_keys(resume_data['email'])
    
    driver.find_element(By.NAME,'phone').send_keys(resume_data['phone'])

    driver.find_element(By.NAME,"Resume/CV").send_keys(resume_file)

    #inputting job info

    for education in resume_data["education"]:

      driver.find_element(By.NAME, "School").send_keys(education['university'])
      driver.find_element(By.NAME,'Degree').send_keys(education['degree'])

      driver.find_element(By.NAME,'Discipline').send_keys(education['degree'])
      driver.find_element(By.NAME,'End Month/Year').send_keys(education['graduation_month'],education['graduation_year'])

      



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