"""
Syntax: defaultdict(default_factory)
Parameters:  

default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
"""

from collections import defaultdict

dict=defaultdict(int)

l=[3,7,3,4,5,1,2]

for i in l:
    dict[i]+=1

print(dict)


#eg 2

def def_value():
    return "Not Present"

d=defaultdict(def_value)

d["a"]=1 
d["b"]=2

print(d["b"])
print(d["c"])


#default_factory is a list

d1=defaultdict(list)

for i in range(5):
    d1[i].append(i)

print("Dictionary with values as list:")
print(d1)

#Using int as default_factory

d2=defaultdict(int)

l=[1,2,3,4,5]

for i in l:
    d2[i]+=1        #since default value of int is 0.All values will be incremented by 1 and set as 1

print(d2)

















