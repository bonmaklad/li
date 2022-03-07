#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a modification of the code sourced from this article: https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/?trackingId=HUfuRSjER1iAyeWmcgHbyg%3D%3D
It is a web scraper scraping google for linkedin profiles; the use case would be recruiters sourcing target candidates for recruiting purposes. 
Also copied the find_profiles function from here: https://www.pingshiuanchua.com/blog/post/scraping-search-results-from-google-search 
"""


from threading import currentThread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.element import Tag
from time import sleep
import csv
from parsel import Selector
import numpy


# Function call extracting title and linkedin profile iteratively
def find_profiles():
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href=True)
            title = None
            title = r.find('h3')
            
            # returns True if a specified object is of a specified type; Tag in this instance 
            if isinstance(title,Tag):
                title = title.get_text()
    
            description = None
            description = r.find('span', attrs={'class': 'st'})
    
            if isinstance(description, Tag):
                description = description.get_text()
    
            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '':
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
            
    
        # Next loop if one element is not present
        except Exception as e:
            print(e)
            continue
        
# This function iteratively clicks on the "Next" button at the bottom right of the search page. 
def profiles_loop():
    
    find_profiles()
    
    next_button = driver.find_element_by_xpath('//*[@id="pnnext"]') 
    next_button.click()
    
    
def repeat_fun(times, f):
    for i in range(times): f()
    
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('linkedin3/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com')
sleep(3)

# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "project coordinator" AND "Wellington"')

# .send_keys() to simulate the return key 
search_query.send_keys(Keys.RETURN)



soup = BeautifulSoup(driver.page_source,'lxml')
result_div = soup.find_all('div', attrs={'class': 'g'})
    
# initialize empty lists
links = []
titles = []
descriptions = []

# Function call x10 of function profiles_loop; you can change the number to as many pages of search as you like. 
repeat_fun(1, profiles_loop)

# Separates out just the First/Last Names for the titles variable
titles01 = [i.split()[0:2] for i in titles]
CurrentTitle = [i.split()[1:2] for i in titles]
CurrentCompany = [i.split()[2:2] for i in titles]

print(CurrentTitle)
print(CurrentCompany)










# The function below stores scraped data into a .csv file
from itertools import zip_longest
# Load titles and links data into csv
d = [titles01, links, CurrentTitle, CurrentCompany]
export_data = zip_longest(*d, fillvalue = '')

f = open('project.csv', 'w')
# create the csv writer
writer = csv.writer(f)
writer.writerows(export_data)
f.close()




