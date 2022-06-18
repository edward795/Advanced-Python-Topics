from collections import UserList

l=[1,2,3,4,5]
ul=UserList(l)
print(ul.data)

ul=UserList()
print(ul.data)

#modifying the default behaviour of list

class MyList(UserList):
    def remove(self,s=None):
        raise RuntimeError("Deletion not allowed")

    def pop(self,s=None):
        raise RuntimeError('Deletion not allowed')

li=MyList([1,2,3,4,5])

li.remove(3)

li.pop()