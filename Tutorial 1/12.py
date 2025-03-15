# Input 4 integers (+ve and −ve). Write a Python code to find the sum of negative numbers, positive numbers, and print them. Also, find the averages of these two groups of numbers and print.
nums = []
for i in range(4):
    nums.append(int(input("Enter a number: ")))
sum_positive = 0
sum_negative = 0
count_positive = 0
count_negative = 0
for num in nums:
    if num > 0:
        sum_positive += num
        count_positive += 1
    elif num < 0:
        sum_negative += num
        count_negative += 1
avg_positive = sum_positive / count_positive if count_positive > 0 else 0
avg_negative = sum_negative / count_negative if count_negative > 0 else 0
print("Sum of positive numbers:", sum_positive)
print("Sum of negative numbers:", sum_negative)
print("Average of positive numbers:", avg_positive)
print("Average of negative numbers:", avg_negative)
