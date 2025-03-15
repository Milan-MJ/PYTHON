# Write a python program to check Armstrong number of n digits.
# Eg:1634= 1**4+6**4+3**4+4**4=1634
num = int(input("Enter a number: "))
n = len(str(num))
sum_of_powers = sum(int(digit) ** n for digit in str(num))
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")

