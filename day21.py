def prog1(l1, l2):
    print(list(zip(l1, l2)))

def prog2(l):
    print(list(zip(l, range(1, 9))))

def prog3(l):
    print(sorted(l))

def prog4(l):
    print(list(filter(lambda x : x%2 != 0, l)))

if __name__ == '__main__':
    l1 = [2, 7, 1, 9, 0]
    l2 = [1, 2, 3, 4, 5]
    prog1(l1, l2)
    prog2([1, 6, 9, 4, 2, 8, 3, 7])
    prog3(l1)
    prog4(l1)
