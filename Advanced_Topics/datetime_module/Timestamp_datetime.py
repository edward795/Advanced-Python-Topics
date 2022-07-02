from datetime import datetime 

#timestamp to date object conversion
timestamp = 1545730073
date_obj=datetime.fromtimestamp(timestamp)
print(date_obj)
print(type(date_obj))

#datetime to timestamp 
now=datetime.now()
timestamp=datetime.timestamp(now)
print(timestamp)
print(type(timestamp))




