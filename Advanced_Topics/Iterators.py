'''A Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.'''

li=[1,2,3,4,5]
it=iter(li)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))

#For loop willwork on all iterators
for i in li:
    print(i)

#Working of for loop
def for_loop(iterable):
    iter_obj=iter(iterable)
    while True:
        try:
            element=next(iter_obj)
            print(element)
        except StopIteration:
            break

for_loop(li)

#custom itertaors
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))

#infinite iterators
class InfiniteIter:
    def __iter__(self):
        self.num=1 
        return self

    def __next__(self):
        n=self.num 
        self.num+=2
        return n

i=iter(InfiniteIter())
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))