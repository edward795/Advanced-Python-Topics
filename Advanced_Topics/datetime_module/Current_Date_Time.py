#current date 
from datetime import datetime
now=datetime.now()

#method 1
today=now.strftime("%d/%m/%y")
print(today)

#method 2
now=datetime.today()
today=now.strftime("%d/%m/%y")
print(today)

#current time

#method 1 
from datetime import datetime
now=datetime.now()
t=now.strftime("%H:%M:%S")
print(t)

#method 2
today=datetime.today()
t=now.strftime("%H:%M:%S")
print(t)

#method 3
import time 
t=time.localtime()

t1=time.strftime("%H:%M:%S",t)
print(t1)

#current time of a timezone 
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))