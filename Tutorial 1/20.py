# Write a Python code to determine whether the given string is a Palindrome or not using slicing. Do not use any string function.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

