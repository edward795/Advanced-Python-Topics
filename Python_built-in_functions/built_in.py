#abs() 
print(abs(-10))
print(abs(-2))


print(-20)
print(abs(-20))

#all() 
print(all([1,5,6,1]))
print(all([5,3,0,1,1]))

#any()
print(any([2,3,0,1]))
print(any([0,0,0,0]))

#bin()
print(bin(4))

#bool()
print(bool([]))
print(bool(1))
print(bool(0))

#bytes()
s="Hello World!"
bytes_obj=bytes(s,'utf-8')
print(bytes_obj)

#callable()
x=8 

print(callable(x))

def printHello():
    return "Hello World!"

print(callable(printHello))

#compile() & exec()
code_str="""

def print_Hello():
    print("Hello World!")

print_Hello()

"""
code=compile(code_str,'print_hello.py','exec')
print(type(code))
exec(code)


#sum()
print(sum([1,2,3,4,5]))
print(sum([1,2,5],10))

#ascii()
print(ascii("The \ndoom!! has spelled"))
print("The \ndoom!! has spelled")

#bytearray()
print(bytearray('Hello World!','utf-8'))

#eval()
print(eval("1+2+3+4"))
print("1+2+3+4")

#float()
print(float(9))
print(float("10"))
print(float("-7.9\n"))

#format()
print(format(10,"b"))
print(format(1.23456,"3.2f"))

#frozenset()
s=("a","a","b","c","d")
f=frozenset(s)
print(f)

#getattr()
class Details:
    name="Ram"
    age=10
    marks=75.6

d=Details()
print(getattr(d,"age"))

#hasattr()
print(hasattr(d,"age"))

#delattr()
delattr(Details,"marks")

#setattr()
setattr(d,"type","college")
print(d.type)

#globals()
print(globals())
print(globals()['s'])

#iter()
li=[1,2,3,4,5,6,7]
iterator=iter(li)

print(next(iterator))
print(next(iterator))

#len()
str1='Python'
print(len(str1))

#list()
print(list(str1))

#map()
li=[1,2,3,4,5]

def double(x):
    return 2*x 

li1=map(double,li)
li2=list(li1)
print(li2)

#memoryview()
randomByteArray=bytearray("ABC",'utf-8')
mv= memoryview(randomByteArray)
print(mv)
print(list(mv))

#object()
python=object()
print(type(python))
print(dir(python))

#chr()
print(chr(97))

#ord()
print(ord('a'))

#complex()
a=complex(1)
b=complex(1,2)
c=complex('1+2j')
print(a)
print(b)
print(c)

#dir()
res=divmod(10,2)
print(res)

#enumerate()
e=enumerate([1,2,3,4,5])
print(e)
print(list(e))

#dict()
res=dict()
res1=dict(name="Raju",age=10)
print(res,res1)

#filter()
def filteredData(x):
    if x>5:
        return x
res=filter(filteredData,[1,2,3,4,5,6,7,8,9])
print(list(res))

#hash()
h1=hash(21)
h2=hash(22.22)
print(h1)
print(h2)

#help()
#help()
help(filter)

#min()
print(min(1,2,3,4,5))

#max()
print(max(1,2,3,4,5))

#set()
print(set((1,2,3,4,4,5,5)))
print(set("Python Programming"))

#hex()
print(hex(12))
print(float.hex(23.456))

#id()
a=123
b=123
a=45
print(id(a))
print(id(b))
print(id(a))

#slice()
a=[9,8,7,6,5,4,3,2,1]
x=slice(5)
y=slice(0,4,2)
print(a[x])
print(a[y])

#sorted()
l=[22,55,88,33,55,77]
a=sorted(l)
b=sorted(l,reverse=True)
print(a)
print(b)

#next()
l=[1,2,3,4,5]
iterator=iter(l)
print(next(iterator))
print(next(iterator))

#input()
x=input("Enter a Value:")
print(x)

#int()
a=int(10)
b=int(10.22)
c=int('1056')
print(a,b,c)

#isinstance()
class Student:
    age=10 
    name="Ram"

    def __init__(self,age,name):
        self.age=age 
        self.name=name

student=Student(23,"Raju")
lst=[1,2,3,4,5]

print(isinstance(student,Student))
print(isinstance(lst,Student))

#oct()
val=oct(10)
print(val)

#ord()
print(ord("A"))
print(ord("B"))

#pow()
print(pow(2,4))
print(pow(2,4,2))

#print()
print("Hello")

#range()
print(list(range(10)))

#reversed()
l=[1,2,3,4,5]
print(reversed(l))
print(list(reversed(l)))

#round()
print(round(10.87))
print(round(10.87,1))

#issubclass()
class Shape:
    def __init__(self,name):
        self.name=name

class Rectangle(Shape):
    def __init__(self,age):
        super().__init__(self.name)
        self.age=age


print(issubclass(Rectangle,Shape))

#str()
a=2
print("The Number is:"+str(a)+"!")

#tuple()
a=tuple([1,2,3,4])
b=tuple("Apple")
c=tuple({"a":"apple","b":"orange"})
print(a)
print(b)
print(c)

#type()
print(type(2))
print(type({1:"one"}))
print(type(Student))
print(type(student))
print(type(filteredData))
print(type(filter))

#vars()  -- note: student is an instance of Student class
print(vars(student))

#zip()
numl=[1,2,3]
namel=["one","two","three"]

res=zip(numl,namel)
print(res)
print(list(res))
print(set(res))