
def prog1():
    d1 = {'a':1, 'b':2, 'c':3}
    d2 = {'d':4, 'e':5, 'f':6}

    d1.update(d2)
    print(d1)

def prog2():
    l = [12, 34, 23, 1, 56 ,45, 89, 67]
    l.sort(reverse = True)
    print(l)

def prog3():
    d = {'b':2, 'a':1, 'c':3, 'e':5, 'd':4}
    l = list(d.keys())
    l1 = l
    l.sort()
    print("Using sort function:" , l)
    for i in range(len(l1)-1):
        for j in range(i+1, len(l1)):
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
    print("Without using function:" , l1)

def prog4():
    s = input("enter a string:")
    rep, sub = input("enter what word to replace with what substitute:").split()
    s = s.replace(rep, sub, 1)
    print(s)

def prog5():
    s = input("enter a string:")
    sub = input("enter a substring:")
    s = s.replace(sub, sub.capitalize())
    print(s)

def prog6():
    l = [1,2,3,2,1,5,6,5,5,5]
    s = set()
    dup = []
    for ele in l:
        if ele not in s:
            s.add(ele)
        elif ele not in dup:
            dup.append(ele)
    print("Repeated elements are:", dup)

def prog7():
    a, b, c = input("Enter three numbers:").split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(input("Divide by:"))
    print((a+b+c)/d)

def prog8():
    a, b, c = input("Enter three numbers:").split()
    a = int(a)
    b = int(b)
    c = int(c)

    mean = (a+b+c)/3
    print("Mean:", mean)

    l = [a, b, c]
    x = min(l)
    y = max(l)

    print("Median:", sum(l)-x-y)

    k = []

    for ele in l:
        if ele not in k:
            k.append(ele)
    v = [l.count(ele) for ele in k]

    d = dict(zip(k, v))

    print("Repeated elements:", [k for k, v in d.items() if d[k] == max(d.values()) and d[k] != 1])

def prog9():
    s = input("Enter a string:")
    s = s.swapcase()
    print(s)

def prog10():
    n = int(input("Enter a number:"))
    print("Binary:", str(bin(n))[2:])
    print("Octal:", str(oct(n))[2:])

if __name__ == '__main__':
    prog1()
    prog2()
    prog3()
    prog4()
    prog5()
    prog6()
    prog7()
    prog8()
    prog9()
    prog10()