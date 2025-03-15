# Write a Python program to find the value for sin(x) up to n terms using the series sin(x)=1-x^3/3!+x^5/5!..... ( sin(x) = ((-1)^n/(2n+1)!)x^(2n+1) )
import math
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

sin_x = sum((-1)**i * (x**(2*i+1) / factorial(2*i+1)) for i in range(n))
print("sin(x) =", sin_x)
