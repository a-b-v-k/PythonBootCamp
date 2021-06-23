#   Create a python module with list and import the module in another .py file and change the value in list
import day11module

li = day11module.arr()
li[2] = 5
print(li)

# 	Install pandas package (try to import the package in a python file
#   pip install pandas
import pandas as pd
print('Version:', pd.__version__)

# 	Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run
import random
num = random.randint(1, 100)
print("Random number:", num)

#	Import sys package and find the python path
import sys

for p in sys.path:
    print(p)

# 	Try to install a package and uninstall a package using pip
#   pip install numpy
#   pip uninstall numpy