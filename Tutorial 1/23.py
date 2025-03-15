# Write a Python program to print all prime factors of a given number.
num = int(input("Enter a number: "))
print("Prime Factors of", num, ":")
factor = 2
while num > 1:
    while num % factor == 0:
        print(factor, end=" ")
        num //= factor
    factor += 1
