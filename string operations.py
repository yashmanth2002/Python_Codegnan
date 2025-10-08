'''s = "Codegnan"
print(s[0])
print(s[-2])
print(s[-1])
print(s[2:5])
print(s[4:])
print(s[:4])
print(s[-4::-1])
print(s[:-5:-1])
print(s[::-1])
print(s[6:2:-1])
print(s[-1:-6])
print(s[-1:6])
print(s[-8:0:6])
print(s)


#Empty string representation

s1 = ""
s2 = str() #string function
# type()-This function returns the data type
print(type(s1))
print(type(s2))


#string operations
#concatenation by using '+' operator
s1 = "Code"
s2 = "Gnan"
print(s1+s2)
print(s1+" "+ s2)


#String repetation using '*' operator
s1 = "Code "
print(s1 * 100)

s1 = "*"
print(s1*1)
print(s1*2)
print(s1*3)
print(s1*4)
print(s1*5)

#String reading from User
s = input()
print(s)


#String methods
#case conversions

s = "TechMitra"
lower_string = s.lower()
print("Lower case conv:", lower_string)
print("Upper case conv:", s.upper())
print("Title case conv:", s.title())
print("Capitalize case conv:", s.capitalize())
print("Swapcase conv:", s.swapcase())

s = "Codegnan"
print(s.find("o"))
print(s.index("o"))
print(s.count("n"))
'''

s = "     Techmitra      "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
