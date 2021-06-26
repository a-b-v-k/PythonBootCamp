def prog1():
    print(Exception)
    print(StopIteration)
    print(SystemExit)
    print(ArithmeticError)
    print(OverflowError)
    print(FloatingPointError)
    print(ZeroDivisionError)
    print(AssertionError)
    print(AttributeError)
    print(EOFError)
    print(ImportError)
    print(KeyboardInterrupt)
    print(LookupError)
    print(IndexError)
    print(KeyError)
    print(NameError)
    print(UnboundLocalError)
    print(EnvironmentError)
    print(IOError)
    print(SyntaxError)
    print(IndentationError)
    print(SystemError)
    print(SystemExit)
    print(TypeError)
    print(ValueError)
    print(RuntimeError)
    print(NotImplementedError)

def prog2():
    [a, b] = [int(x) for x in input("Enter two numbers:").split()]
    print('Enter choice:')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    choice = int(input())
    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3:
        print(a*b)
    elif choice == 4:
        try:
            print(a/b)
        except ZeroDivisionError as e:
            print(e)
    else:
        try:
            raise ValueError('Invalid option.')
        except ValueError as v:
            print(v)

def prog3(a):
    try:
        if a == 1:
            raise NameError('Name error')
        elif a == 0:
            raise SyntaxError('Syntax error')
        else:
            raise ValueError('Value error')
    except NameError as n:
        print(n)
    except Exception as e:
        print(e)

def prog4():
    print("try except block is not required when there is not exception to be raised and not exception to be caught.")

def prog5():
    try:
        n = int(input('Enter a value:'))
        if n == 0:
            raise ValueError('Value cannot be zero')
        print('value:', n)
    except ValueError as v:
        print(v)

if __name__ == '__main__':
    prog1()
    prog2()
    prog3(1)
    prog3(0)
    prog3(-1)
    prog4()
    prog5()
