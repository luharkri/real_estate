import time
import json
from bs4 import BeautifulSoup
from time import sleep
import requests   
from random import randint
from html.parser import HTMLParser
from pprint import pprint
import csv
import mechanize

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
# SEARCH_URL = "https://www.duckduckgo.com/html/?q="
SEARCH_URL = "https://www.redfin.com/county/321/CA/Los-Angeles-County"

class Analyzer:
    def __init__(self):
        print("starting class")
        self.card_links = set()


    def search(self, sleep=False):
        if sleep: # Prevents loading too many pages too soon
            t = randint(1,7)
            print("sleeping for : ", t, " seconds")
            time.sleep(t)
        
        url = SEARCH_URL
        page = requests.get(url, headers=USER_AGENT)
        soup = BeautifulSoup(page.text,"html.parser")
        page = self.scrape_page_number(soup)
        print("page text  -  ", page)
        
        for p in range(page):
            print(p)
            add_url = url + "/page-" + str(p)
            print(add_url)
            # soup = self.get_soup(add_url)
            # res = set(self.scrape_search_result(soup))
            # self.card_links.append(res)

        return

    def get_soup(self, add_url):
        try:
            print("success")
            url = SEARCH_URL + str(add_url)
            print(url)
            page = requests.get(url, headers=USER_AGENT)
            soup = BeautifulSoup(page.text,"html.parser")
            return soup
            
        except:
            print("error")
        

    def scrape_search_result(self, soup):
        raw_results = soup.find_all("a",attrs = {"class" : "link-and-anchor visuallyHidden"})
        # print(raw_results)
        results = []
        for result in raw_results:
            link = result.get('href')
            if link not in results:
                results.append(link)   
        return results    
    
    def scrape_page_number(self, soup):
        raw_results = soup.find_all("span",attrs = { "data-rf-test-name" : "download-and-save-page-number-text"})
        raw_results = str(raw_results)
        raw_results = raw_results.split("Viewing page 1 of")
        page = raw_results[1].split("<!")[0].strip()
        return int(page)
    
    def clean_links(self, in_arr):
        ret_arr = []
        for link in in_arr:
            clean1 = link.split("://")[1]
            cleansed = clean1.split("www.")[len(clean1.split("www."))-1]
            if cleansed[-1] == '/':
                cleansed = cleansed[:-1]
            # print(cleansed)
            ret_arr.append(cleansed)
        return ret_arr
    


if __name__ == '__main__':
    print("hello world")
    a = Analyzer()

    a.search(False)
