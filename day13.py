import re
def prog1(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

def prog2(text):
    patterns = '\w*ab.\w*'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

def prog3(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

def prog4(text):
    results = re.finditer(r"([0-9]{1,3})", text)
    print("Number of length 1 to 3")
    for n in results:
        print(n.group(0))

def prog5(text):
    patterns = '^[A-Z]+$'
    if re.match(patterns,  text):
            return 'Found a match!'
    else:
            return('Not matched!')


if __name__ == '__main__':
    print(prog1("ABCDEFabcdef123450")) 
    print(prog1("*&%@#!}{"))

    print(prog2("abcd"))
    print(prog2("acd"))

    print(prog3('abcdef'))
    print(prog3('abcdef6'))

    prog4("1, 12, 13, and 345")

    print(prog5("hello world"))
    print(prog5("PYTHON"))
