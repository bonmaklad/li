from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from threading import currentThread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.element import Tag
from time import sleep
import csv
from parsel import Selector
import numpy

  
# Creating a webdriver instance
driver = webdriver.Chrome(executable_path=r'linkedin3/chromedriver')
# This instance will be used to log into LinkedIn
  
# Opening linkedIn's login page
driver.get("https://www.linkedin.com/")
  
# waiting for the page to load
time.sleep(5)
  
# entering username
username = driver.find_element_by_id('session_key')
  
# In case of an error, try changing the element
# tag used here.
  
# Enter Your Email Address
username.send_keys("Michael@acv.co.nz")  
  
# entering password
pword = driver.find_element_by_id('session_password')
# In case of an error, try changing the element 
# tag used here.
  
# Enter Your Password
pword.send_keys("73s95dFG")        
  
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element_by_class_name('sign-in-form__submit-button').click()
# In case of an error, try changing the
# XPath used here.

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/michael-law-74010a39/"
  
driver.get(profile_url)        # this will open the link




src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
  


# In case of an error, try changing the tags used here.
  
name_loc = intro.find("h1")
  
# Extracting the Name
name = name_loc.get_text().strip()
# strip() is used to remove any extra blank spaces
  
works_at_loc = intro.find("div", {'class': 'text-body-medium break-words'})
  
# this gives us the HTML of the tag in which the title is present
# Extracting the Company Name
works_at = works_at_loc.get_text().strip()
  
intro2 = soup.find('div', {'class': 'pb2 pv-text-details__left-panel'})

location_loc = intro2.find("span", {'class': 'text-body-small inline t-black--light break-words'})
  
# Ectracting the Location
# The 2nd element in the location_loc variable has the location
location = location_loc.get_text().strip()
  


# waiting for the page to load
time.sleep(2)


      
start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 5 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 5:
        break

profile_urlexp = profile_url + "details/experience/"
driver.get(profile_urlexp)        # this will open the link




start = time.time()
  
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
  
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
  
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
  
    end = time.time()
  
    # We will scroll for 15 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break


src = driver.page_source
  
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')


# Getting the HTML of the Experience section in the profile
allexperiene = soup.find('div', {'class': 'scaffold-finite-scroll__content'})
experience = allexperiene.find('ul', {'class': 'pvs-list'})
#lis = []
lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
#latestjobtitle = lis[0].find_all("span")[0].find_all("span")[0].get_text().strip()
#latestjobcompany = lis[1].find_all("span")[0].find_all("span")[0].get_text().strip()





jobCompany =[]
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('span', {'class': 't-14 t-normal'})
    for li in lis:
        jobCompany.append(li.text)
        print(li.text)


lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})

maindata = []
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('div', {'class': 'display-flex align-items-center'})
    print(lis)
    for li in lis:
        maindata.append(li.text)
lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})



typeOFJob =[]



lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})





jobtitle = []
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('span', {'class': 't-bold mr1'})
    for li in lis:
        jobtitle.append(li.text)
lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
typeOFJob =[]



lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
startDate = []
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('span', {'class': 't-14 t-normal t-black--light'})
    for li in lis:
        startDate.append(li.text)
        print(li.text)

lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
endDate = []

lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
duration =[]


lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
jobWhere =[]
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('span', {'class': 't-14 t-normal t-black--light'})
    for li in lis:
        jobWhere.append(li.text)
        

lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
jobDescription = []
for li in lis:
    newsoup = BeautifulSoup(str(li), 'html.parser')
    lis = newsoup.find_all('div', {'class': 'display-flex align-items-center t-14 t-normal t-black'})
    for li in lis:
        jobDescription.append(li.text)
        
lis = experience.findAll('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})


# The function below stores scraped data into a .csv file
from itertools import zip_longest
d = [name, works_at, location, maindata, jobCompany, startDate,  jobDescription]
export_data = zip_longest(*d, fillvalue = '')

f = open('project.csv', 'w')
# create the csv writer
writer = csv.writer(f)
writer.writerow(export_data)
f.close()

























