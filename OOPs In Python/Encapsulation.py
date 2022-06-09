class Computer:
    def __init__(self,price,tax):
        self.__price=price   #__price is a private attribute
        self._tax=tax        #_tax is a protected attribute

    def sell(self):
        print(f'The price is {self.__price} & tax is {self._tax}:So total = {self.__price+self._tax}')
       

    def setPrice(self,new_price):
        self.__price=new_price 

    def setTax(self,new_tax):
        self._tax=new_tax

c=Computer(900,5)
c.sell()

#setting new price via instance  --- bnot going to work as '__price' is a private variable
c.__price=1200
c.sell()

#setting new price via setter func()
c.setPrice(1200)
c.sell()

#setting protected variable '_tax'
c._tax=12
c.sell()

c.setTax(12)
c.sell()