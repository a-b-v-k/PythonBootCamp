import requests
from bs4 import BeautifulSoup
import xlsxwriter
   
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

'''for quote in quotes:
    print('Theme:', quote['theme'])
    print('Quote:', quote['lines'])'''

workbook = xlsxwriter.Workbook('write_data.xlsx')
sheet = workbook.add_worksheet()

column = 0  

content = ['Theme', 'Quote']     
      
for item in content :       
    sheet.write(0, column, item, workbook.add_format({'bold': True}))   
    column += 1

row = 1
column = 0

for quote in quotes:
    sheet.write(row, column, quote['theme'])
    sheet.write(row, column + 1, quote['lines'])
    column = 0
    row += 1

workbook.close()

