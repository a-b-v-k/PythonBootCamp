
def prog1(y):
    return lambda x : x * y

def prog2(f):
    fib_list = [0, 1]
  
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, f)))
  
    return fib_list[:f]

def prog3(l, n):
    return list(map(lambda ele : ele * n, l))

def prog4(l):
    return list(filter(lambda ele : (ele % 9 == 0), l))

def prog5(l):
    return len(list(filter(lambda ele : (ele % 2 == 0), l)))

if __name__ == '__main__':
    var = prog1(5)
    print(var(2))
    print(prog2(5))
    print(prog3([1, 2, 3, 4, 5], 2))
    print(prog4([18, 24, 27, 35, 45]))
    print(prog5([1, 2, 3, 4, 5]))