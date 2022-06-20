import re


#findall() method    

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

pattern='\d+'
match=re.findall(pattern,string)
print(match)

#compile() method

pattern=re.compile('[a-e]')
match=pattern.findall(string)
print(match)

pattern=re.compile('\d')
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

pattern=re.compile('\d+')
print(pattern.findall("I went to him at 11 A.M. on 4th July 1886"))

pattern=re.compile('ab*')
print(pattern.findall("ababbaabbb"))

#split() method

pattern=re.compile('\W')
print(pattern.split("Words, Words, Words"))

print(re.split('\W+',"Words, Words, Words"))

print(re.split('\d+','On 12th Jan 2016, at 11:02 AM'))
print(re.split('\d+','On 12th Jan 2016, at 11:02 AM',1))


#sub() funtion
print(re.sub('Ub','~*','Subject has booked Uber already'))
