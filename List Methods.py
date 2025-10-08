# To read list of integers from users
'''
l = list(map (int, input().split()))
print(l)

l = list(map (int, input().split(',')))
print(l)

strings = list(map (str, input().split(',')))
print(strings)

# single element add to a list

l = [1,2,3,4]
ele = 10
print( l + [ele])
'''

# List Methods

l = [1,2,3,4]
l.append(10)
print("After Append 10:" , l)
l.extend([20,30,40])
print("After Extend Operation:", l)
