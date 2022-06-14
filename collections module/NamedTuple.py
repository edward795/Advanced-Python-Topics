"""
Syntax:

class collections.namedtuple(typename, field_names)
"""

from collections import namedtuple

Student=namedtuple("Student",["name","age"])
s=Student("Raju",22)

#print name using index & name & getattr
print("Print name using index:",s[0])
print("Print name using name:",s.name)
print("Print name using getattr:",getattr(s,"name"))

stu=Student("Nandi",23)
li=["Manjeet",25]
di={"name":"Ram","age":27}

print("Before:",stu)
#make named tuple from list
print(Student._make(li))
#convert named tuple to dictionary
print(stu._asdict())
#make named tuple from dictionary
print(Student(**di))

#return all the fields of namepace
print(stu._fields)

#returna replaced field 
print(stu._replace(name="Karan"))