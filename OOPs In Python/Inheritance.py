#Example 1

from re import T


class Bird:
    def __init__(self):
        print("Bird is ready.")

    def WhoIsThis(self):
        print("This is Bird")

class Parrot(Bird):
    def __init__(self):
        super().__init__()   #calling parent class constructor
        print("Parrot is ready.")

    def WhoIsThis(self):
        print("This is Parrot")

    def Fly(self):
        print("Parrot is flying.")

p=Parrot()
print("--------------------------------")
p.WhoIsThis()
p.Fly()


#Example 2 

class Polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(self.n)]

    def inputSides(self):
        self.sides=[float(input("Enter side "+str(i+1)+":")) for i in range(self.n)] 

    def displaySides(self):
        for i in range(self.n):
            print("Side "+str(i+1)+": "+str(self.sides[i]))

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def findArea(self):
            a, b, c = self.sides
            # calculate the semi-perimeter
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print('The area of the triangle is %0.2f' %area)

t=Triangle()
t.inputSides()
t.displaySides()
t.findArea()

#checking inheritance using isintance() & issubclass()

print(isinstance(t,Triangle))
print(isinstance(t,Polygon))
print(issubclass(Triangle,Polygon))
print(issubclass(Polygon,Triangle))