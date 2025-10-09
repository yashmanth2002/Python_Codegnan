lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
for i in range(len(lst)):
    if lst[i]%2 == 0:
        res.append(lst[i] ** 2)
    else:
        val = lst[i] ** 0.5
        res.append(round(val, 3))
print(res)