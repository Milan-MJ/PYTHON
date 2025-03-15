# Write a python program to find X^Y or pow(X,Y) without using standard function.
x = int(input("Enter base (X): "))
y = int(input("Enter exponent (Y): "))
result = 1
for _ in range(y):
    result *= x
print(f"{x}^{y} =", result)
