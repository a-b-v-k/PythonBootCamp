import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Vicky@2003",
  database="sample",
  buffered = True,
)

dbse = mydb.cursor()

dbse.execute('Drop table doctor')
dbse.execute('Create table doctor(doctor_id integer, doctor_name text, patients integer)')

dbse.execute('Insert into doctor values (1, \'Adam\', 10)')
dbse.execute('Insert into doctor values (2, \'Bob\', 7)')
dbse.execute('Insert into doctor values (3, \'Charles\', 0)')

mydb.commit()

dbse.execute('Select * from doctor')

print(dbse.fetchall())


#doctors with patients > 5

dbse.execute('Select * from doctor where patients > 5')
rows = dbse.fetchall()

for row in rows:
    print('ID:', row[0])
    print('Name:', row[1])
    print('Patients:', row[2])

#doctors with no patients

dbse.execute('Select * from doctor where patients = 0')
rows = dbse.fetchall()

for row in rows:
    print('ID:', row[0])
    print('Name:', row[1])
    print('Patients:', row[2])
