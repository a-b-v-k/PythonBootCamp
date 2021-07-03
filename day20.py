import mysql.connector
import xlrd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="*****",
  database="sample",
  buffered = True,
)

dbse = mydb.cursor()

dbse.execute('drop table employee')

dbse.execute('Create table employee(emp_id int, emp_name text, emp_salary int)')

query = '''Insert into employee(emp_id, emp_name, emp_salary) values(%s, %s, %s)'''
values = [(1, 'Adam', 30000),
          (2, 'Bob', 20000),
          (3, 'Charles', 10000),
          (4, 'Daniel', 5000)]

dbse.executemany(query, values)

dbse.execute('Select * from employee')

print(dbse.fetchall())


# print min and max salary of employee

dbse.execute('Select max(emp_salary), min(emp_salary) from employee')
res = dbse.fetchall()
print('Max salary:', res[0][0])
print('Min salary:', res[0][1])

# print number of employees working in a company

dbse.execute('Select count(emp_id) from employee')
print('Number of employees:', dbse.fetchall()[0][0])

#print the first three characters of employees first names

dbse.execute('Select left(emp_name, 3) from employee')

res = dbse.fetchall()
print('First three characters of employees first names:')
for r in res:
    print(r[0])