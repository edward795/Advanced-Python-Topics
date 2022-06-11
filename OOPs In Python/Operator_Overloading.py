#operators behave differently in different situations
print(1+2)

l1=[1,2,3]
l2=[3,4,5]
print(l1+l2)

print("apple" + "orange")

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

p1=Point(2,3)
p2=Point(3,4)
#print(p1+p2) -> TypeError: unsupported operand type(s) for +: 'Point' and 'Point' 

class Point:
    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y 

    def __str__(self):
        return '{0} {1}'.format(self.x,self.y)

    def __add__(self,other):
        x=self.x+other.x 
        y=self.y+other.y
        return Point(x,y)

    def __lt__(self,other):
        mag_x=self.x **2 + self.y **2 
        mag_y=other.x **2 + other.y **2 
        return mag_x < mag_y



p1=Point(2,3)
p2=Point(3,4)

#magic function or special function for add -> '__add__'
print(p1+p2)

#magic function or special function for less than -> '__lt__'
print(p1<p2)
print(p2<p1)