# Write a Python program to print the factorial of a number using recursion.
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter number: "))
print("Factorial:", factorial(n))
