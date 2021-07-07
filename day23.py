from tkinter import *
from tkinter import filedialog
import json
from PIL import Image
import os
import requests
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

window = Tk()
window.geometry('500x500')
window.title("Day 23 task")

Fetch = str()
pdfs = []

head = Label(window, text="Simple converter",width=20,font=("bold", 20))
head.place(x=90, y=20)

def browse_image():
    file = filedialog.askopenfilenames()
    for i in file:
        im = Image.open(i)
        dir = os.path.dirname(i)
        fname = os.path.basename(i).split('.')[0]
        im.save(dir + '/' + 'converted_' + fname + '.png')
        print('Converted ' + fname + ' to png')

def weather_data(query):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + fetch_entry.get() + "&units=metric&appid="+'____apikey___')
    return json.loads(response.content)


def print_weather(result, Fetch):
    print("{}'s temperature: {}°C ".format(Fetch,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    print("Pressure: {} hpa".format(result['main']['pressure']))
    print("Humidity: {}%".format(result['main']['humidity']))


def weather():
    query = Fetch
    w_data=weather_data(query)
    #print(w_data)
    print_weather(w_data, Fetch)
    print()

def pdf():
    file = filedialog.askopenfilenames()
    for f in file:
        pdfs.append(f)

def merge():
    mergedObject = PdfFileMerger()
    dir = os.path.dirname(pdfs[0])
    try:
        for f in pdfs:
            file = open(f, 'rb')
            mergedObject.append(PdfFileReader(f, 'rb'))
        mergedObject.write(dir + '/' + 'merged.pdf')

        with open(dir+'/'+'merged.pdf', "rb") as input_file, open('watermark.pdf', "rb") as watermark_file:
            input_pdf = PdfFileReader(input_file)
            watermark_pdf = PdfFileReader(watermark_file)
            watermark_page = watermark_pdf.getPage(0)

            output = PdfFileWriter()

            for i in range(input_pdf.getNumPages()):
                pdf_page = input_pdf.getPage(i)
                pdf_page.mergePage(watermark_page)
                output.addPage(pdf_page)

            with open(dir + '/' + 'mergedwatermark.pdf', "wb") as merged_file:
                output.write(merged_file)
    
    except:
        print('Error during merging....')

image_but = Button(window, text='Convert images',width=20,bg='brown',fg='white', command = browse_image)
image_but.place(x=180,y=100)


fetch_but = Button(window, text='Fetch Weather',width=20,bg='brown',fg='white', command = weather)
fetch_but.place(x=180,y=150)

fetch_entry = Entry(window,textvariable = Fetch)
fetch_entry.place(x=193, y=200)

pdf1 = Button(window, text='Pdf 1', width=20, bg='brown', fg='white', command = pdf)
pdf1.place(x=180, y=250)

pdf2 = Button(window, text='Pdf 2', width=20, bg='brown', fg='white', command = pdf)
pdf2.place(x=180, y=300)

wm_but = Button(window, text='Water Mark Merge', width=20, bg='brown', fg='white', command = merge)
wm_but.place(x=180, y=350)

window.mainloop()