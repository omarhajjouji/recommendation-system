import requests
from bs4 import BeautifulSoup
import random
import sqlite3
import traceback
import pandas

import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

site="https://towardsdatascience.com/tagged/"
labels=["data-science","ai","deep-learning","machine-learning","artificial-intelligence"]
path_to_chromedriver = r"C:\Users\amrou\Google Drive\python work\chromedriver.exe"
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(executable_path = path_to_chromedriver,chrome_options=options)
path=r"articles.csv"



def random_headers():
	return {'User-Agent': random.choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def indexPage(url):
	#see block note for algorithme
        browser.get(url)
        etr=0
        while etr<500:
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                etr+=1
        time.sleep(2)
        content=browser.find_elements_by_css_selector('a[class=""]')
        links=map(lambda x:x.get_attribute("href"),content)
        r=open(path,"r+")
        s=0
        for i in links:
                if(i and not(i in r)):
                        r.write(str(i)+"\n")
                        s+=1
        r.close()
        return s

count=0
for label in labels:
        count+=indexPage(site+label)
browser.quit()
print(count)