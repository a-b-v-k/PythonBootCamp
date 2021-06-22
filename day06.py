d1 = {'a':1, 'b':2, 'c':3}
d2 = {'d':4, 'e':5, 'f':6}

#Merge two dictionaries
d1.update(d2)
print(d1)

#Delete a key
del d1['a']
print(d1)

l1 = ['x', 'y', 'z']
l2 = [1, 2, 3]

#Mapping two lists into a dictionary
dic = dict(zip(l1, l2))
print(dic)

#Printing the length of a set
s1 = {'a', 'b', 'c', 'd'}
print(len(s1)) 

s2 = {'c', 'd', 'e', 'f'}

#Removing intersection of set elements from s1
for ele in s1.intersection(s2):
    s1.discard(ele)
print(s1)
