def func1():
    a, b = input('Enter two numbers:').split()
    a = int(a)
    b = int(b)
    print('Addition of two numbers:', a+b)
    print('Subtraction of two numbers:', a-b)
    print('Mutliplication of two numbers:', a*b)
    print('Division of two numbers:', a/b)

def covid():
    name = input("Enter patient's name:")
    temp = int(input("Enter body temperature:"))
    if(temp > 98):
        print("Chances of covid is high")
    else:
        print("Chances of covid is low")

if __name__ == '__main__':
    func1()
    covid()
