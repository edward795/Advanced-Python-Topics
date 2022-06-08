class Person:
    '''This is a Person Class.It stores a person's name & age.'''
    species='HomoSapein'
    def __init__(self,name,age):
        self.name=name 
        self.age=age 

    def display(self):
        print(f'The person is {self.name} and he is {self.age} years old.')

#Class attributes
print(Person.__doc__)
print(Person.display)
print(Person.species)

#instance attributes
ramu=Person("Ramu",25)
kumar=Person("Kumar",30)

ramu.display()
kumar.display()

#modifying attributes as by default the class variables have public access specifiers
ramu.name="Ram Kumar"
ramu.age=27
ramu.display()

print(ramu.__class__)
print(ramu.species)
print(ramu.__class__.species)
print(ramu.__class__.__name__)
print(ramu.__class__.display)


