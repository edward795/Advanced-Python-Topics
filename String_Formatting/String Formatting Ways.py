#using % symbol
from math import pi
print("Apple,%s,mango,%s"%("grapes","jackfruit"))
print('Apple,orange,%s'%'grapes')
print("The %d boys had %d bikes with them"%(4,2))
print("The value of pi is %9.4f"%pi)

#using str.format() function
name="akash"
print("My name is {}".format(name))
print("My name is {0} and i am {1} years old".format("Ramu",24))
print('My name is {name}'.format(name=name))
print('{0:x}'.format(12))
print('{0:{1}b}'.format(4,3))

#using f string 
print(f"my name is {name}")
a=5 
b=10
print(f"my age is {((a*b)/2)}")
print(f"value of pi is:{pi:{1}.{5}}")
print(f"His age is:{(lambda x:x*2)(10)}")

#using string Template classes
from string import Template
n1='Hello'
n2='Arun'
n=Template('$n3 ! This is $n4') 
print(n.substitute(n3=n1,n4=n2))
