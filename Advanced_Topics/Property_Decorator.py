from multiprocessing.sharedctypes import Value


class Celsius:
    def __init__(self,temperature=0):
        self.set_temperature(temperature)

    def to_farenheit(self):
        return (self.get_temperature()*1.8)+32 

    def get_temperature(self):
        return self._temperature   

    def set_temperature(self,value):
        if value<-273.15:
            raise ValueError('Temperature below -273.15 not allowed.')
        self._temperature=value

c=Celsius()
c.set_temperature(23)
print(c.get_temperature())

#not possible to modify private variables
c.temperature=54
print(c.get_temperature())

#Using property object

class ModifiedCelsius:
    def __init__(self,temperature=0):
        self.temperature=temperature

    def to_farenheit(self):
        return (self.temperature*1.8)+32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self,value):
        if value<-273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature=value 

    temperature=property(get_temperature,set_temperature)

k=ModifiedCelsius()
k.set_temperature(23)
print(k.get_temperature())

#now you can access & change the temperature property
k.temperature=57
print(k.temperature)

#using @property decorator
'''
property(fget=None, fset=None, fdel=None, doc=None)
where,

fget is function to get value of the attribute
fset is function to set value of the attribute
fdel is function to delete the attribute
doc is a string (like a comment)
'''

class PropertyCelsius:
    def __init__(self,temperature=0):
        self.temperature=temperature 

    def to_farenheit(self):
        return (self.temperature*1.8)+32 

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        print("Setting value...")
        if value<-273.15:
            raise ValueError("The temperature is below -273,which is not possible.")
        self._temperature=value

human=PropertyCelsius(37)    
print(human.temperature)
print(human.to_farenheit())

coldest=PropertyCelsius(-300)

#Note:"if u use setter & getter with property decorator it will be automatically invoked on '." or dot notation call to set propoerties



