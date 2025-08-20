n = int(input("Enter a number: "))

print("Odd numbers from 1 to", n, "are:")

i = 1
while i <= n:
    if i % 2 != 0:  
        print(i, end=" ")
    i += 1
