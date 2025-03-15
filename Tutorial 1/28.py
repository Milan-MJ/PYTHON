# Write a Python program to display the sum of odd numbers between a programmer specified upper and lower limit.
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
sum_of_odds = sum(num for num in range(low, high+1) if num % 2 != 0)
print("Sum of odd numbers:", sum_of_odds)
