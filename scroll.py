#Date = 24-03-2018

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import requests

print('enter the city')
x = raw_input()
link = "https://www.foodpanda.in/restaurants/city/" + x


driver = webdriver.Chrome(r'C:\Users\Admin\Documents\chromedriver.exe')
driver.get(link)

# ---

# scrolling

lastHeight = driver.execute_script("return document.body.scrollHeight")

#print(lastHeight)
pause = 10
tt=0
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    

    html = driver.page_source
    soup = bs(html, "html.parser")

    

    rest1 = soup.findAll('div',{'class':'vendor__details'})
   
    
    if  len(rest1) > tt:
        tt=len(rest1)
    else:    
         break

filename = '123g.csv'

f = open(filename, "w")

total_res = len(rest1)
c = soup.find('div',{'class':'homepage-headline'})
d = c.h2
f.write(str(total_res) + ',' + str(d)[16:21] + '\n')
for restaurants in rest1:
    rest2 = restaurants.findAll('span',{'class':'vendor__name'})
    res_name=rest2[0].text.strip()
    star = restaurants.findAll('span',{'class':'rating-score hide'})
    avg_star = star[0]['content']
    try:
        res_name.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        continue

    f.write(res_name + ',' + avg_star + '\n')
         
f.close()

 
