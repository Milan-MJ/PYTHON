# Write a python program to compute nCr using a factorial function.
import math
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print("nCr =", math.factorial(n) // (math.factorial(r) * math.factorial(n - r)))
