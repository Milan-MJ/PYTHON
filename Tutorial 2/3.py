# Write a python script for palindrome checking without reversing the string.
s = input("Enter a string: ")
n = len(s)
is_palindrome = all(s[i] == s[n - i - 1] for i in range(n // 2))
print("Palindrome" if is_palindrome else "Not a Palindrome")