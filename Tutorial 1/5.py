# Program to find the roots of a quadratic equation.
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
D = b**2 - 4*a*c
if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Two distinct real roots: {root1:.2f} and {root2:.2f}")
elif D == 0:
    root = -b / (2 * a)
    print(f"One real root: {root:.2f}")
else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(abs(D)) / (2 * a)
    print(f"Complex roots: {real_part:.2f} ± {imag_part:.2f}i")
