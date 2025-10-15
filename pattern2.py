'''''rows = 4
for i in range(rows):
    for j in range(rows):
        print(chr(65 + i), end=" ")
    print()

n = 6
num = 0
for i in range(n):
    for j  in range(n):
        print(chr(65 + num), end = " ")
        num += 1
        if chr(65 + num - 1) == 'Z':
            num = 0
    print()

n = 6
for i in range(n):
    for j in range(n):
        print(i+ j + 1, end = " ")
    print()
'''
n = 6
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print("=", end = " ")
        else:
            print("+", end = " ")
    print()