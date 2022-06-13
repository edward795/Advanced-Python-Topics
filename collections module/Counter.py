from collections import Counter 
c1=Counter(['a','a','b','k','k','c','e'])
c2=Counter({'a':2,'b':4})
c3=Counter(a=2,k=5,l=6,c=5)
print(c1,c2,c3)

#eg 2
c=Counter()
print(c)
c.update([1,2,3,4,6,9,2,3,4])
print(c)

c1=Counter(A=2,B=4)
c2=Counter(A=4,B=1)
c1.subtract(c2)
print(c1)


