import os

try:
    filepath = str(input('Enter the path of the file:'))

    newname = str(input('Enter the new name:'))

    filedir = os.path.dirname(filepath)

    filename = os.path.basename(filepath)

    newfilepath = filedir + '/' + newname

    os.rename(filepath, newfilepath)

except FileNotFoundError as e:
    print(e)