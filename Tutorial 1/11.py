# Write a Python program which takes a positive integer n as input and finds the sum of cubes of all positive even numbers less than or equal to the number.
n = int(input("Enter a positive integer: "))
sum_of_cubes = 0
for i in range(2, n+1, 2):  
    sum_of_cubes += i**3  
print("Sum of cubes of even numbers:", sum_of_cubes)
