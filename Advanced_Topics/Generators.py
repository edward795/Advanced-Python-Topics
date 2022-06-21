#simple generator
def my_gen():
    print("This is printed first!")
    yield 1 

    print("This is printed second!")
    yield 2

    print("This is printed third!")
    yield 3

i=my_gen()
print(next(i))
print(next(i))
print(next(i))

#for loop implementation
for i in my_gen():
    print(i)

#generators using for loop
def rev_str(my_str):
    length=len(my_str)
    for i in range(length-1,-1,-1):
        yield my_str[i]


for i in rev_str("hello"):
    print(i,end=" ")

#generator expressions

x=[x for x in range(5)]
g=(x for x in range(5))

print(x)
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

gen=(x**2 for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#generators can be passed as arguement to a function whithout the '()'
print(sum(x**2 for x in range(5)))
print(max(x for x in range(22)))
