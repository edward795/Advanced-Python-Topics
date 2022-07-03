import threading ,time

def print_Hello():
    for i in range(5):
        print("Hello")

def print_Hi():
    for i in range(5):
        print("Hi")

print_Hello()
print_Hi()

t1=threading.Thread(target=print_Hello)
t2=threading.Thread(target=print_Hi)
t1.start()
t2.start()


#use time.sleep() - The sleep() function suspends execution of the current thread for a given number of seconds.

def print_Hello1():
    time.sleep(2)
    for i in range(5):
        print("Hello")

def print_Hi1():
    for i in range(5):
        print("Hi")


t1=threading.Thread(target=print_Hello1)
t2=threading.Thread(target=print_Hi1)
t1.start()
t2.start()

