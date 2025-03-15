# Write a Python program to print n’th Fibonacci number using recursion.
def fibonacci(n):
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter n: "))
print("Fibonacci number:", fibonacci(n))
