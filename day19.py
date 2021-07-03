import mysql.connector
import xlrd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="******",
  database="sample",
  buffered = True,
)

book = xlrd.open_workbook("Exams list.xls")
sheet = book.sheet_by_name("Sheet1")

dbse = mydb.cursor()

dbse.execute('Drop table sampledata')
dbse.execute("Create table sampledata(name text, subject text, Examdate text, points text)")
query = """INSERT INTO sampledata (name, subject, Examdate, points) VALUES (%s, %s, %s, %s)"""

for r in range(1, sheet.nrows):
    name = str(sheet.cell(r, 0).value)
    subject = str(sheet.cell(r, 1).value)
    Examdate = str(sheet.cell(r, 2).value)
    points = str(sheet.cell(r, 3).value)

    dbse.execute(query, (name, subject, Examdate, points))

dbse.execute("Select * from sampledata")

rows = dbse.fetchall()

for row in rows:
    print()
    print('Name:', row[0])
    print('Subject:', row[1])
    print('Exam date:', row[2])
    print('Points:', row[3])