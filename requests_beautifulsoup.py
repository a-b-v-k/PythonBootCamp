import requests
from bs4 import BeautifulSoup
   
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html.parser')
   
quotes=[]  
   
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quotes.append(quote)

for quote in quotes:
    print('Theme:', quote['theme'])
    print('Quote:', quote['lines'])