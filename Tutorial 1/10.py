# Python program to find the sum of even numbers from N given numbers.
N = int(input("Enter how many numbers: "))
sum_of_evens = 0
for i in range(N):
    num = int(input("Enter a number: "))
    if num % 2 == 0:  
        sum_of_evens += num
print("Sum of even numbers:", sum_of_evens)
