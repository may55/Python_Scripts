from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re

class result:
    def __init__(self):
        self.name = ''
        self.cgpa = ''


driver = webdriver.Chrome('/home/mayank/Documents/Projects/Python/Course/chromedriver')



soup = bs(driver.page_source , 'lxml')
#print(soup.text)
#roll = '1605210026'
fh = open('result3rdyear.txt', 'wb')
x = 1505210001
for roll in range(x,x+60):
    driver.get('http://result.ietlucknow.ac.in/')
    roll = str(roll)
    roll_no = driver.find_element_by_xpath('//*[@id="node-6"]/div/div/div/div/div/form/input[1]')
    roll_no.send_keys(roll)
    
    butt = driver.find_element_by_xpath('//*[@id="node-6"]/div/div/div/div/div/form/input[2]')
    butt.click()
    
    #driver.get('http://result.ietlucknow.ac.in/ODD201718')
    soup2 = bs(driver.page_source, 'lxml')
    
    
    tbody  = soup2.find('tbody')
    if not tbody:
        continue
    
    tr = tbody.find_all('tr')
    name = tr[0]
    td_name = tr[0].find_all('td')
    name = td_name[1]
    
    cgpa = tr[20]
    
    
    fh.write(name.text.encode())
    fh.write(cgpa.text.encode())
   
    r = result()
    r.name = name.text
    r.cgpa = cgpa.text
    #driver.get()
    
    #print(tbody.text)
    print(r.name, r.cgpa)

driver.quit()
fh.close()

