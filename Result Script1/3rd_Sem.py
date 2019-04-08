from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re

class result:
    def __init__(self):
        self.name = ''
        self.total = ''


driver = webdriver.Chrome('files/chromedriver')



soup = bs(driver.page_source , 'lxml')
#print(soup.text)
#roll = '1605210026'
fh = open('resultMarksCHE.csv', 'wb')
x = 1605251001
l= []
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
    
    marks = tr[16]
    #print(marks.text)
    tr_marks = tr[17].find_all('tr')
    Mark = []
    for i in range(7, 17):
        marks_td = tr[i].find_all('td')
        mark = int(marks_td[5].text)
        print(mark)
        Mark.append(mark)
    
    total = sum(Mark)
   
    r = result()
    r.name = name.text
    r.total = str(total)
    #driver.get()
    
    
    
    l.append([str(total),name.text])
    #print(tbody.text)
    print(r.name, r.total)

driver.quit()
l.sort(reverse = True)

for i in l:
    fh.write((str(i[0])+','+str(i[1])+'\n').encode())

fh.close()

