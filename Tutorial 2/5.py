# Write a program to slice the string into two separate strings; one with all the characters in the odd indices and one with all characters in even indices.
s = input("Enter a string: ")
odd = s[1::2]
even = s[0::2]
print("Odd index string:", odd)
print("Even index string:", even)
