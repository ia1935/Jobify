#Main script to run bot

import time


from scraper import WebScraper, printLinks

from dataRetrieval import GetUserInfo, resumeScraper


def main():

    



#implementation of user input resume to parse and enter info in job link. For scalability in future for others to use this can be implemented

    # #grabbing filename
    # file_name = GetUserInfo()
    # if not file_name:
    #     print("No File entered. Ending program")
    #     return


    # extracted_data = resumeScraper(file_name)
        
    # if extracted_data:
    #     print("Extracted Resume Data:")
    #     # print(extracted_data)
    # else:
    #     print("No data extracted.")

    applyLinks = WebScraper()

    #need to now pass this array to my application function to apply for jobs
    
    







if __name__ == '__main__':
    main()
