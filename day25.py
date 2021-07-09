from datetime import datetime, date, timedelta

#   Write a Python program to convert a string to datetime 
date_object = datetime.strptime('Jul 9 2021 2:43PM', '%b %d %Y %I:%M%p')
print(date_object)

#	Write a Python program to subtract five days (last working day) from current date
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)


#	Write a Python program to convert the date to datetime using a function
dt = datetime.combine(date.today(), datetime.min.time())
print(dt)

#	Write a Python program to print next 7 days (week) starting from today
base = datetime.today()
for x in range(0, 7):
      print(base + timedelta(days=x))

