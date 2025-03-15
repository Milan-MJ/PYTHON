# Write a Python program to print all numbers between 100 and 1000 whose sum of digits is divisible by 9
for num in range(100, 1001):
    sum_of_digits = sum(int(digit) for digit in str(num))
    if sum_of_digits % 9 == 0:
        print(num, end=" ")
