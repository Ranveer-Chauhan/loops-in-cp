n = int(input("Enter a number: "))

print("Even numbers from 1 to", n, "are:")

i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
