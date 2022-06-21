#decorator without arguements 
def make_pretty(func):
    def inner():
        print("I am decorated!")
        func()
    return inner 

def ordinary():
    print("I am ordinary!")

#decorator old fashioned way
pretty=make_pretty(ordinary)
pretty()

#python syntactic sugar for the decorator
@make_pretty
def ordinary():
    print("I am ordinary")

print(ordinary())

#Decorators with 2 arguements
def smart_divide(func):
    def inner(a,b):
        print(f"Dividing {a} by {b}.")
        if b==0:
            print("Whoops cannot divide!")
            return  
        return func(a,b)
    return inner 

@smart_divide
def divide(a,b):
    print(a/b) 

print(divide(3,4))
print(divide(3,0))

#Decorators with any number of arguements
def star(func):
    def inner(*args,**kwargs):
        print("*"*30)
        func()
        print("*"*30)
    return inner 

def hash(func):
    def inner(*args,**kwargs):
        print("#"*30)
        func()
        print("#"*30)
    return inner

@star
@hash 
def print_message():
    print('Hello World!')

print(print_message())