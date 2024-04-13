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
SEARCH_URL = "https://sfsu.co1.qualtrics.com/jfe/form/SV_4Sd9RKfbQDoHg1g"

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
        print(url)

        br = mechanize.Browser()
        # cj = mechanize.CookieJar()
        # br.set_cookiejar(cj)
        # br.set_handle_equiv(True)
        # br.set_handle_redirect(True)
        # br.set_handle_referer(True)
        br.set_handle_robots(False)  # ignore robots
        # br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        br.addheaders = [('User-agent', 'Mozilla/5.0')]
        br.open(SEARCH_URL)
        forms = list(br.forms())
        print(forms)
        # page = requests.get(url, headers=USER_AGENT)
        # soup = BeautifulSoup(page.text,"html.parser")
        
        
        # res = set(self.scrape_search_result(soup))
        # self.card_links.append(res)
        # print(res)
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

    a.search()
