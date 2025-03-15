# Write a program to remove all vowel characters from a string.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = "".join(char for char in s if char not in vowels)
print("String without vowels:", result)
