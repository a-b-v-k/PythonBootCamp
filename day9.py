#!/usr/bin/env python
# coding: utf-8

# ### Write a program to loop through a list of numbers and add +2 to every value to elements in list


l = [1, 2, 3, 4, 5]
l = [ele+2 for ele in l]
print(l)


# ### Write a program to get the below pattern
# ### 54321
# ### 4321
# ### 321
# ### 21
# ### 1


for r in range(5, 0, -1):
    for c in range(r, 0, -1):
        print(c, end='')
    print()


# ### Python Program to Print the Fibonacci sequence



def fib(n):
    a = 0
    b = 1
    if(n == 0 or n == 1):
        print(0)
    elif(n == 2):
        print(1)
    else:
        print(0)
        print(1)
        for i in range(2, n):
            print(a+b)
            c = a + b
            a = b
            b = c
n = int(input("Enter a number:"))
fib(n)


# ### Explain Armstrong number and write a code with a function
# A positive integer is called an Armstrong number of order n if
# 
# abcd... = an + bn + cn + dn + ...
# In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:
# 
# 153 = 1*1*1 + 5*5*5 + 3*3*3  
# 153 is an Armstrong number.



num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# ### Write a program to print the multiplication table of 9



for i in range(1, 11):
    print("9 x", i, "=", 9*i)


# ### Check if a program is negative or positive



n = int(input("Enter a number"))
if n > 0:
    print('Positive')
elif n < 0:
    print('Negative')


# ### Write a program to convert the number of days to ages



d = int(input("Enter number of days:"))
print(d//365, 'year(s) and', d%365, 'days')


# ### Solve Trigonometry problem using math function write a program to solve using math function

import math

x = 0.75 

print("math.cos(",x,"): ", math.cos(x))
print("math.sin(",x,"): ", math.sin(x))
print("math.tan(",x,"): ", math.tan(x))
print("math.acos(",x,"): ", math.acos(x))
print("math.asin(",x,"): ", math.asin(x))
print("math.atan(",x,"): ", math.atan(x))
y = 2
print("math.atan2(",y,",",x,"): ", math.atan2(y,x))
print("math.hypot(",x,",",y,"): ", math.hypot(x,y))


# ### Create a calculator only on a code level by using if condition (Basic arithmetic calculation)


a, b = input("Enter two numbers:").split()
a = int(a)
b = int(b)

c = input("Enter the operation symbol:")

if c == '+':
    print(a, c, b , '=', a+b)
elif c == '-':
    print(a, c, b , '=', a-b)
elif c == '*':
    print(a, c, b , '=', a*b)
elif c == '/':
    print(a, c, b , '=', a/b)
elif c == '%':
    print(a, c, b , '=', a%b)
elif c == '//':
    print(a, c, b , '=', a//b)

