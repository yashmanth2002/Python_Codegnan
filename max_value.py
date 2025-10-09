lst = [1, 10, 4, 5, 11, 9]
max_val = lst[0]
for i in range(1, len(lst)):
    if max_val < lst[i]:
        max_val = lst[i]
print(max_val)