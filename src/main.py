#Main script to run bot

import time


from scraper import WebScraper, printLinks

from dataRetrieval import GetUserInfo


def main():
    #grabbing filename
    file_name = GetUserInfo()
    if not file_name:
        print("No File entered. Ending program")
        return


    
    # print("Getting links from GitHub Page:\n")
    # apply_links = WebScraper()
    
    # print("Printing Links:")
    # printLinks()







if __name__ == '__main__':
    main()
