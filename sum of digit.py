n = int(input("enter the number"))
s = 0
while n > 0:
    digit = n % 10
    n = n // 10
    s +=digit
print(s)