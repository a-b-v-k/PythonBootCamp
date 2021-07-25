# CERTIFICATE GENERATOR

# Import all the necessities
import xlrd
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, date, timedelta

# Open the excel sheet to collect data
book = xlrd.open_workbook("certificate_details.xls")
sheet = book.sheet_by_name("Sheet1")


for r in range(0, sheet.nrows):
    name = str(sheet.cell(r, 0).value)
    course = 'course on ' + str(sheet.cell(r, 1).value)
    sign = str(sheet.cell(r, 3).value)
    cur_d = str(date.today().strftime("%d/%m/%Y"))


    # Open the certificate template
    im = Image.open("cert.jpg")
    d = ImageDraw.Draw(im)


    # Set the location of each field in pixels
    loc_name = (560, 314) 
    loc_course = (560, 460)
    loc_d = (296, 526)
    loc_sign = (816, 510)

    # Specify the text color    
    text_color = (0, 0, 0)


    # Write the name on the template
    font_name = ImageFont.truetype("LCALLIG.TTF", 55)
    w, h = font_name.getsize(name)
    d.text((loc_name[0]-w//2, loc_name[1]), name, fill=text_color,font=font_name)

    # Write the course on the template
    font_course = ImageFont.truetype("FTLTLT.TTF", 30)
    w, h = font_course.getsize(course)
    d.text((loc_course[0]-w//2, loc_course[1]), course, fill=text_color,font=font_course)

    # Write the date on the template
    font_date = ImageFont.truetype("FTLTLT.TTF", 30)
    w, h = font_date.getsize(cur_d)
    d.text((loc_d[0]-w//2, loc_d[1]), cur_d, fill=text_color,font=font_date)

    # Write the signature on the template
    font_sign = ImageFont.truetype("Standlist-RpBYV.ttf", 30)
    w, h = font_sign.getsize(sign)
    d.text((loc_sign[0]-w//2, loc_sign[1]), sign, fill=text_color,font=font_sign)


    # Save the final image as pdf in order of 'r'
    im.save("certificate_"+ str(r) +".pdf")