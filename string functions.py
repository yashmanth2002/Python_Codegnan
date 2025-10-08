'''#split(pat)- It splits the string where the pattern is match and returns as list of substrings
#sep.join(iterable) - It joins the list of string into single string with seperator

s = "The Sky is Blue and Ocean is Blue"
print(s.split())
print(s.split('Blue'))
print(s.split('u'))
print(s.split('zs'))
 

print(ord("A"))
print(chr(65))
print(ord("a"))
print(chr(78))
print(chr(128514))


print("Codegnan".islower())
print("codegnan".islower())
print("CODEGNAN".isupper())
print("Codegnan".isalpha())
print("CodeGnan".isalnum())
print("Code123Gnan".isalnum())
print("123".isalnum())
print("Codegnan".istitle())
print("1234".isdigit())

# membership operator
#in, not in
print("S" in "Codegnan")
print("S" not in "Codegnan")


#string comparision
s1 = "abcd"
s2 = "abcde"
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)
print("ABC" < 'abc')


# identity operator
#string comparision
s1 = "abcd"
s2 = "abcd"
print(id(s1), id(s2))
print(s1 == s2)
print(s1 is s2)

#some built in functions

print(len("Codegnan"))
'''
s = "Codegnan"
print(len(s))
print(min(s))
print(max(s))
print(s.replace('n', 'z'))
print(s.replace('n', 'j'))
print(s.replace('n', 'z', 1))
