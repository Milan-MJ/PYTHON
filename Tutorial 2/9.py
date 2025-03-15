# Write a Program to reverse the first and second half of a string separately.
s = input("Enter a string: ")
mid = len(s) // 2
print("Modified string:", s[:mid][::-1] + s[mid:][::-1])
