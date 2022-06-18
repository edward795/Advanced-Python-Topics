from collections import UserDict

d={"a":1,"b":2}
userd=UserDict(d)

print(userd.data)

userd=UserDict()
print(userd.data)


#creating custom behaviour for the dictionary

class MyDict(UserDict):
    def __del__(self):
        raise RuntimeError('Deletion not allowed')

    def pop(self,s=None):
        raise RuntimeError('Deletion not allowed')

    def popitem(self,s=None):
        raise RuntimeError('Deletion not allowed')

d=MyDict({"a":1,"b":2,"c":3})

d.pop(1)
del d['a']