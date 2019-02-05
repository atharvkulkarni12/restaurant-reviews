import numpy as np
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib
import requests

url = 'https://www.zomato.com/chennai/kfc-besant-nagar/reviews'

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
    date.append(dt[0].encode("utf-8"))
    time.append(dt[1].encode("utf-8"))
    name.append(spl[0].encode("utf-8"))
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

s5 = soup.findAll("div" , {"class":"item col-s-16"})
#len(s5)
#u = s5[0].a["href"]
#url2 = u.encode("utf8")
profile_urls = []
for i in range(10):
    profile_urls.append(s5[i].a["href"].encode("ascii"))
locations = []
ranks = [] 
user_reviews = []
photos = [] 
followers = []
bookmarks = []
beenthere = []
for i in profile_urls:
    url3 = i
    response3 = requests.get(url3, headers=headers)
    urlopen3 = response3.text
    soup3 = bs(urlopen3,"html.parser")

    s6 = soup3.find("div" , {"data-icon":"L"})

    loc = s6.text.strip().encode("utf-8")
    locations.append(loc)
    s7= soup3.find("span" , {"data-icon":"ú"})
    rank = s7.text.strip().encode("utf-8")
    ranks.append(rank)
    s8 = soup3.find("a" , {"data-tab":"reviews"})
    user_reviews.append(s8.div.text.strip().encode("utf-8"))
    s9 = soup3.find("a" , {"data-tab":"photos"})
    photos.append(s9.div.text.strip().encode("utf-8"))
    s10 = soup3.find("a" , {"data-tab":"network"})
    followers.append(s10.div.text.strip().encode("utf-8"))
    s11 = soup3.find("a" , {"data-tab":"bookmarks"})
    bookmarks.append(s11.div.text.strip().encode("utf-8"))
    s12 = soup3.find("a" , {"data-tab":"beenthere"})
    beenthere.append(s12.div.text.strip().encode("utf-8"))
    

d = {'user_name':name,'user_rank':ranks,'user_reviews':user_reviews, 'user_photos':photos,'user_followers':followers,'user_bookmarks':bookmarks,'user_been-there':beenthere, 'user_location':locations, 'Date':date, 'Time':time, 'Review':review}
df1 = pd.DataFrame(data=d , columns = ['user_name','user_location','user_rank','Date','Time','user_reviews','user_photos','user_followers','user_bookmarks','user_been-there','Review'])
df1.to_csv('zomato_3.csv')