from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Selenium WebDriver (this will download and set up ChromeDriver for you)
driver = webdriver.Chrome() 

# Go to the page URL
driver.get('https://github.com/cvrve/Summer2025-Internships?tab=readme-ov-file')

# Wait for the page to load and JavaScript to execute. This can be changed depending on load time
time.sleep(5)

# Now scraping once JS loaded
# Find all the <a> tags for 'Apply' button on github repo
links = driver.find_elements(By.TAG_NAME, 'a')

# List to hold links
apply_links = []

# Iterate through all the links and find those with an image with alt='Apply'
for link in links:
    try:
        img = link.find_element(By.TAG_NAME, 'img')  # Find the image inside the <a> tag
        alt_text = img.get_attribute('alt')  # Get the 'alt' attribute of the image
        
        if alt_text == 'Apply':  # Check if the image's alt text is 'Apply'
            apply_links.append(link.get_attribute('href'))  # Get the link, add it to apply_links
    except:
        continue  # on to the next link

if apply_links:
    for apply_link in apply_links:
        print(apply_link)
else:
    print("No links found with 'Apply' image.")

# Close the browser when done
driver.close()
