#convert date object to string

from datetime import datetime
from time import time
now=datetime.now()

t=now.strftime("%H:%M:%S")
print(t)

s1=now.strftime("%m/%d/%Y, %H:%M:%S")
print(s1)

s2=now.strftime("%d/%m/%Y, %H:%M:%S")
print(s2)

#convert string to date object
date_string="21 June 2018"
print(datetime.strptime(date_string,"%d %B %Y"))

#Locale's representation

timestamp=datetime.fromtimestamp(1528797322)
d=timestamp.strftime("%c")
print("Locale's date & time:",d)
e=timestamp.strftime("%x")
print("Locale's date:",e)
f=timestamp.strftime('%X')
print("Locale's time:",f)