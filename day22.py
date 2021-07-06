from PIL import Image
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader
import requests
from bs4 import BeautifulSoup
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****",
  database="sample",
  buffered = True,
)

dbse = mydb.cursor()
  

def prog1():
    img = Image.open('logo.jpg')
    img.show()
    print(img.format)
    print(img.mode)

def prog2():
    mergedObject = PdfFileMerger()
    mergedObject.append(PdfFileReader('first.pdf', 'rb'))
    mergedObject.append(PdfFileReader('second.pdf', 'rb'))
    mergedObject.write("mergedfilesoutput.pdf")

def prog3():
    URL = "http://www.values.com/inspirational-quotes"
    r = requests.get(URL)    
    soup = BeautifulSoup(r.content, 'html.parser')    
    quotes=[]      
    table = soup.find('div', attrs = {'id':'all_quotes'}) 

    dbse.execute('Drop table web_data')
    dbse.execute('Create table web_data(theme text, quote text, url text)')

    query = """Insert into web_data (theme, quote, url) values (%s, %s, %s)"""
    
    for row in table.findAll('div', attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
        quote = {}
        quote['theme'] = row.h5.text
        quote['url'] = row.a['href']
        quote['lines'] = row.img['alt'].split(" #")[0]
        quotes.append(quote)

        dbse.execute(query, (quote['theme'], quote['lines'], quote['url']))

def prog4():
    dbse.execute('Select quote from web_data where theme = \'hard work\'')
    data = list(dbse.fetchall())
    for d in data:
        print(d[0])

if __name__ == '__main__':
    prog1()
    prog2()
    prog3()
    prog4()