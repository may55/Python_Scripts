# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup as bs

# row players-wrapper 

#create driver

driver = webdriver.PhantomJS(executable_path = '/home/mayank/Documents/Projects/Python/NBA/NBA/phantomjs')

url='http://www.nba.com/players'

# download htlm
driver.get(url)


html_doc=driver.page_source

soup=bs(html_doc,'lxml')

#create soup

x=soup.find('div', class_ = 'row players-wrapper')

a_tags = x.find_all('a')
#print(len(a_tags))
for a in a_tags:
    print(a.text)

#print(x.prettify()) 

driver.quit()
