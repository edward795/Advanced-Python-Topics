from datetime import datetime
import pytz

local=datetime.now()
print("local time: ",local.strftime("%m/%d/%Y,%H:%M:%S %p"))

tz_NY=pytz.timezone('America/New_York')
newyork_time=datetime.now(tz_NY)
tNY=newyork_time.strftime("%d/%m/%Y, %H:%M:%S %p")

tz_london=pytz.timezone('Europe/London')
london_time=datetime.now(tz_london)
tln=london_time.strftime("%d/%m/%Y, %H:%M:%S %p")

print("New York Time: ",tNY)
print("London Time: ",tln)