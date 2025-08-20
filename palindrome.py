N = int(input("Enter a number: "))
original = N
rev = 0

while N > 0:
    rev = rev * 10 + N % 10
    N //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
