import requests
#import csv
from bs4 import BeautifulSoup as bs

print('enter the city name :')
c = raw_input()
urlopen = requests.get('https://www.foodpanda.in/restaurants/city/' + c).text

soup = bs(urlopen,'html.parser')

res = soup.findAll('article',{'class':'vendor list js-vendor-list-vendor-panel'})

filename = "foodpanda_pune.csv"


#headers = "name, date, review\n"

#f.write(headers)

i = 0

if len(res) == 0 :
    print('Error : No match found for given city')
    print('please enter city in folowing list')
    print('Agra Ahmedabad-Gandhinagar Amritsar Bangalore Bhopal Bhubaneswar Chandigarh Chennai Cochin Coimbatore Dehradun Delhi Durgapur Faridabad Greater Noida Gurgaon Guwahati')
    print('Howrah Hyderabad Indirapuram-Ghaziabad Indore Jaipur Jalandhar Jamshedpur Kanpur Kolkata Kota Lucknow Ludhiana Madurai Mangalore Mohali Mumbai Mumbai - Navi Mumbai Mumbai - Thane')
    print('Mumbai-Old Mysuru Nagpur Nashik Noida Panchkula Panchkula-Chandigarh-Mohali Patna Pune Rajkot Roorkee Sonipat Surat Tiruppur Udaipur Vadodara Vapi Vishakhapatnam Zirakpur')
else:
    f = open(filename, "w")
    for restaurant in res :
        url1 = restaurant.a['href']
        url = 'https://www.foodpanda.in' + url1 + '#reviews'
        #print(url)
        
        urlopen1 = requests.get(url).text
        soup = bs(urlopen1,'html.parser')
        rev = soup.findAll('li',{'class':'reviews__review'})
        i = i + 1
        x = soup.findAll('div',{'class':'message'})
        res_name = x[0].text[39:]
        f.write(res_name + '\n')
        
        l=0
        for review in rev:
        	
            date = review.div.span['content']
            name_review = review.findAll('span',{'class':'reviews__review__date__author__name'})
            name = name_review[0].text.strip()
            star = review.findAll('span',{'class':'rating-score hide'})
            review_star = star[0]['content']
            
            #print(name[35:])
            #print(date)
            #print(review_star)
            l = l +1
            

            try:
                name[35:].encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                   continue
        
            f.write( name[35:] + ',' + date + ',' + review_star + '\n' )
            if l>30 :
            	break
        f.write('\n')     
        #if i>5 :
            #break
              
    f.close()      
