"""
Commonly used classes in the datetime module are:

date Class  
time Class
datetime Class
timedelta Class

"""

#datetime class
from datetime import datetime
print(datetime.now())
print(datetime.today())

a=datetime(2018,11,28)
print(a)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(a.year)
print(a.month)
print(a.day)
print(a.hour)
print(a.minute)
print(a.timestamp())

#date class

from datetime import date 
d=date(2019,8,13)
print(d)

today=date.today()
print(today)

timestamp=date.fromtimestamp(1326244364)
print("Date From timestamp:",timestamp)

today=date.today()
print(today.year)
print(today.month)
print(today.day)

#time

from datetime import time 

a=time()
print("a=",a)

b=time(11,34,56)
print("b=",b)

c=time(hour=11,minute=34,second=56)
print("c=",c)

d=time(11,34,56,234566)
print("d=",d)

a=time(11,34,56)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)

#timedelta object

a=date(2018,11,23)
b=date(2022,5,11)
c=b-a

t1 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t2 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t3=t2-t1

print(c)
print(t3)

print(type(c))
print(type(t3))

from datetime import timedelta
t1=timedelta(weeks=2,days=5,hours=1,seconds=55)
t2=timedelta(days=4,hours=11,  minutes=4,seconds=54)
t3=t1-t2 
print(t3)

#printing negative timedelta object 

t1=timedelta(seconds=33)
t2=timedelta(seconds=54)
t3=t1-t2 
print(t3)
print(abs(t3))

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print(t.total_seconds())