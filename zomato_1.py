import numpy as np
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib
import requests

url = 'https://www.zomato.com/kochi/fort-house-restaurant-fort-kochi/reviews'

headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
urlopen = response.text
soup = bs(urlopen,"html.parser")
s2 = soup.findAll('a',{'class':'grey-text'})

sa = []
for i in range(32):
    ss1 = str(s2[i].get('href'))
    if "review" in ss1:
        if ss1 not in sa:
            sa.append(ss1)
            #print (ss1)

date = []
time = []
name = []
for i in sa:
    url1 = i
    response1 = requests.get(url1, headers=headers)
    urlopen1 = response1.text
    soup1 = bs(urlopen1,"html.parser")
    s3 = soup1.find('h1',{'class':'section-title mbot pbot0'})
    s4 = soup1.find('time')
    dt = s4.get('datetime')
    s3 = s3.text.strip()
    spl = s3.split("'")
    dt = dt.split(" ")
    date.append(dt[0])
    time.append(dt[1])
    name.append(spl[0])
    #print(dt)
#print (date)
#print(time)
#print(name)

review = []
for i in sa:
    url2 = i
    response2 = requests.get(url2, headers=headers)
    urlopen2 = response2.text
    soup2 = bs(urlopen2,"html.parser")
    s2 = soup2.find('div',{'class':'rev-text mbot0 '})
    rev = s2.text.strip()
    rev = rev.split('Rated')
    review.append(rev[1].encode('utf-8').strip())
#print(review)

d = {'Name':name, 'Date':date, 'Time':time, 'Review':review}
df1 = pd.DataFrame(data=d)
df1.to_csv('zom.csv')