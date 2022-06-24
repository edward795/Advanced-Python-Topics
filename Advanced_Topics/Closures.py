#nested inner functionm is able to access the 'non-local variable'
from email import message


def print_msg(msg):
    def printer():
        print(msg)
    printer()

print_msg("hello")

def print_msg(msg):
    def printer():
        print(msg) 
    return printer

message=print_msg("Hello World")
message()

#Even after deleting the parent funcon the inner func & bound variavble remains in memory
del print_msg
message()

#print_msg()

#Example application 
def make_multiplier(x):
    def multiplier(n):
        return x*n
    return multiplier   

times3=make_multiplier(3)
times4=make_multiplier(4)

print(times3(9))
print(times4(9))
print(times3(times4(9)))

#getting then closed value 
print(times3.__closure__[0].cell_contents)
print(times4.__closure__[0].cell_contents)
