"""
Syntax:

class collections.ChainMap(dict1, dict2)
"""

from collections import ChainMap

d1={"a":1,"b":2}
d2={"b":4,"d":4}
d3={"e":5,"f":6}
c=ChainMap(d1,d2,d3)
print(c)

#accessing values

print(list(c.values()))
print(list(c.keys()))
print(c.maps)
print(c['a'])   

#adding new child
d4={"g":7,"h":8}
new_c=c.new_child(d4)
print(new_c)

#reversing relative ordering 
print('Before reversing:',c['b'])
c.maps=reversed(c.maps)
print('after reversing:',c['b'])
