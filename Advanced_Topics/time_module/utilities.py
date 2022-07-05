from collections import namedtuple
import time 

#time() func 
seconds=time.time()
print(seconds)

#ctime() func
local_time=time.ctime(1654754849.99823)
print(local_time)

#time.sleep()
print("This is printed immediately")
time.sleep(2.4)
print("This is printed after a delay of 2.4s")

#time.struct_time Class
"""
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
                    tm_hour=6, tm_min=35, tm_sec=17, 
                    tm_wday=3, tm_yday=361, tm_isdst=0)
"""

#localtime() func 
res=time.localtime(1545925769)
print(res)
print("year:",res.tm_year)
print("hour:",res.tm_hour)

#gmtime() func -- returns struct_time in UTC. 
res=time.gmtime(1545925769)
print(res)
print("year:",res.tm_year)
print("hour:",res.tm_hour)

#mktime() func
"""
mktime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument
 and returns the seconds passed since epoch in local time
"""
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time=time.mktime(t)
print(local_time)

#asctime() func
"""
asctime() function takes struct_time (or a tuple containing 9 elements corresponding to struct_time) as an argument 
and returns a string representing it
"""
t = (2018, 12, 28, 8, 44, 4, 4, 362, 0)
local_time=time.asctime()
print(local_time)

#strftime() func
named_tuple=time.localtime()
time_string=time.strftime("%m/%d/%Y, %H:%M:%S",named_tuple)
print(time_string)

#strptime() func
time_string = "21 June, 2018"
res=time.strptime(time_string,"%d %B, %Y")
print(res)