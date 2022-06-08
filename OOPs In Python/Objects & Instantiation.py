class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.i=i 
        self.r=r 

    def getData(self):
        print(f'{self.r}+{self.i}j')

c1=ComplexNumber(2,3)
c1.getData()

c2=ComplexNumber()
c2.i=5
c2.getData()

#creating new attributes on the fly with objects
c2.attr=12
print(c2.attr)   

#print(c1.attr)   -> AttributeError: 'ComplexNumber' object has no attribute 'attr'

#deleting attributes & methods
del c2.attr 
# print(c2.attr)  ->  AttributeError: 'ComplexNumber' object has no attribute 'attr'

del ComplexNumber.getData

#c1.getData() -> AttributeError: 'ComplexNumber' object has no attribute 'getData'

del c1

#print(c1.i) -> NameError: name 'c1' is not defined
