from decimal import Decimal
from fractions import Fraction

#int,float,complex
print(type(1))
print(type(2.0))
print(type(2+3j)) 

#decimal
print(1.1+2.2==3.3)

print(1.1+2.2)

print(Decimal(2.2)+Decimal(1.1))

print(Decimal('2.2')+Decimal('1.1'))

##Final Result
print(float(Decimal('1.1')+Decimal('2.2'))==3.3)

#Fractions
print(Fraction(1,3))
print(Fraction(5))
print(Fraction(1.5))

print(Fraction(1.1))
print(Fraction('1.1'))

#opeations with Fraction datatype

print(Fraction(1,3)+Fraction(1,3))
print(Fraction(1,3)*Fraction(2,3))
print(1/Fraction(5,6))
print(Fraction(-3,5)>0)
print(Fraction(-3,5)<0)