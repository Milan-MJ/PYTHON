# Program to find the sum of all even numbers in a group of n numbers entered by the user
n = int(input("Enter the count of numbers: "))  
numbers = []  

for _ in range(n):  
    num = int(input("Enter a number: "))  
    numbers.append(num)  

even_sum = sum(num for num in numbers if num % 2 == 0)  
print("Sum of even numbers:", even_sum)
