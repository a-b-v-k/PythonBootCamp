n = int(input("Enter the value of n:"))
l = []

print("Enter", n, "values:")
for i in range(n):
    l.append(int(input()))

print(l)

#add an element in to the list
l.append(100)
print(l)

#remove an element
l.pop()
print(l)

#store the maximum and minimum values in a and b
a = max(l)
b = min(l)

#create a tuple
t = (1, 2, 3)

#print the tuple from the end
print(t[::-1])

#convert the tuple to a list
t = list(t)
print(t)
