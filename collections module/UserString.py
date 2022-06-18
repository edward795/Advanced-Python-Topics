from collections import UserString

seq=1234
s=UserString(seq)
print(s.data)

s=UserString("")
print(s.data)

#create a custom string

class MyString(UserString):
    def append(self,s):
        self.data+=s

    def remove(self,s):
        self.data=self.data.replace(s,"")

s1=MyString("Geeks")
print(s1.data)

s1.append(" For Geeks")
print(s1.data)

s1.remove(" For Geeks")
print(s1.data)