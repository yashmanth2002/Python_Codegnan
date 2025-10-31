#Armstrong number 
# An Armstrong numbers is numbers that is equal to sum of equal to sum of its own digits raised by its own powern = int(input("Enter a number: "))

n = int(input())
temp = n
sum = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    sum += digit ** digits
    n //= 10

if temp == sum:
    print(temp, "is an Armstrong number")
else:
    print(temp, "is not an Armstrong number")
