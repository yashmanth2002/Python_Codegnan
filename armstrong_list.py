lower = int(input())
upper = int(input())

for num in range(lower, upper + 1):
    digits = len(str(num))
    sum = 0
    temp = num
    
    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10
    
    if num == sum:
        print(num)
