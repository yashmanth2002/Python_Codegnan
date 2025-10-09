lst = [1, 10, 4, 5, 11, 9]
min_val = lst[0]
for i in range(1, len(lst)):
    if min_val > lst[i]:
        max_val = lst[i]
print(min_val)