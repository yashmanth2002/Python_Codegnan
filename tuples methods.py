'''t = tuple(input().split())
print(t)



#example
t = (1, 2, 3, [10, 20, 30], "codegnan")
# tuple is immutable data type
t[0] = 100


t = tuple(map(int, input().split()))
print(t)

#index based and sliceable

t = (1, 2, 3, [10, 20, 30], "Codegnan")
#print(t[2], t[-2], t[-4])
#print(t[-1:2:-1])
print(t[3:-4:-1])


#single element representation

t = (29)
t2 = (20,)
print(type(t), type(t2))

#Tuple Operations
#concatination operation

t1 = (1,2,3)
t2 = ('A',"b")
t3 = t1 + t2
print(t3)

# repetation operation

t1 = (1,2,3)
t = t1 * 3
print(t)

#tuple methods
t = (1, 2, 3, [10, 20, 30], "Codegnan")
ind = t.index(3)
count = t.count(3)
print(ind, count)


#builtin function
# len(), min(), max(), sum()
t = (1,2,3,4,5)
print(len(t), min(t), max(t), sum(t))

s = "Codegnan"
print(list(s))
print(tuple(s))
'''

# tuple to list conversion
t = (1,2,3,4,5)
print(list(t))
