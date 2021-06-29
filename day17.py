import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****",
  database="sample",
  buffered = True,
)
# Create a connection for DB and print the version using a python program
print(mydb._server_version) 


dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)


# Create a multiple tables & insert data in table
dbse.execute('Create table student(id integer)')
dbse.execute('Create table staff(id integer)')

dbse.execute('Insert into student values(1)')
dbse.execute('Insert into student values(2)')
dbse.execute('Insert into student values(3)')

dbse.execute('Insert into staff values(1)')
dbse.execute('Insert into staff values(2)')
dbse.execute('Insert into staff values(3)')


dbse.execute('Show tables')
for entry in dbse:
    print(entry)

dbse.execute('Select * from student')
print(list(dbse.fetchall()))

dbse.execute('Select * from staff')
print(list(dbse.fetchall()))

#Create a employee table and read all the employee name in the table using for loop
dbse.execute('Create table employee(name text, id integer)')

dbse.execute('Insert into employee values(\'John\', 1)')
dbse.execute('Insert into employee values(\'Alex\', 2)')

dbse.execute('Select * from employee')
for entry in dbse:
    print(entry)