# Program that accepts the length of three sides of a triangle as input and determine whether or not the triangle is a right angled triangle.
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
if side1 > side2 and side1 > side3:
    hypotenuse = side1
    base = side2
    altitude = side3
elif side2 > side1 and side2 > side3:
    hypotenuse = side2
    base = side1
    altitude = side3
else:
    hypotenuse = side3
    base = side1
    altitude = side2
if hypotenuse**2 == base**2 + altitude**2:
    print("It is a Right-Angled Triangle.")
else:
    print("It is NOT a Right-Angled Triangle.")
