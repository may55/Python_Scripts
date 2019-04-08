from selenium import webdriver
from bs4 import BeautifulSoup as bs
#import re

class result:
    def __init__(self):
        self.name = ''
        self.cgpa = ''


driver = webdriver.Chrome('/home/mayank/Documents/Projects/Python/Course/chromedriver')



soup = bs(driver.page_source , 'lxml')
#print(soup.text)
#roll = '1605210026'
fh = open('resultCSEL.csv', 'wb')
x = 1705210901
l= []
for roll in range(x,x+12):
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
    #name = tr[0]
    td_cgpa = tr[20].find_all('td')
    cgpa = td_cgpa[1]
    
    
#    fh.write(cgpa.text.encode())
    l.append([cgpa.text,name.text])
    r = result()
    r.name = name.text
    r.cgpa = cgpa.text

    print(r.name, r.cgpa)

driver.quit()

l.sort(reverse = True)

for i in l:
    fh.write((str(i[0])+','+str(i[1])+'\n').encode())

fh.close()
